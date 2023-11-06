"""Time table automatic creator

This time table creator will automatically
create the input for the timetable to ensure it is
always up to date.

In conjunction with running the web-page on a weekly basis
we can automatically ensure that the information is up to date.

It does this by reading a configuration file at the top of the documentation
and calculating the current week, and comparing this to the semester week.

The current week *preferred* will be listed depending on the build-time of the
document.
After 18 on a Friday, the preferred week-number will be the following week.
"""
import datetime
from pathlib import Path

def fill_defaults(semester, periods):
    """ Fill defaults into the `semester` dictionary """
    # fill non-filled data from the generic periods
    for name, defaults in periods:
        period = semester[name]
        for key in ("weeks", "name"):
            if key not in period:
                # update field
                period[key] = defaults[key]


def get_period(periods, semester, week):
    """ Returns the period from `periods` where the current week is located in the semester

    Parameters
    ----------
    periods : tuple of (str, dict)
        name of period, and information about period
    """
    closests = [None, 0]
    for name, period in periods:
        sem = semester[name]
        weeks = sem["weeks"]
        start = sem["week-start"]
        breaks = sem.get("week-breaks", [])
        if not isinstance(breaks, list):
            breaks = [breaks]

        last = start + weeks + len(breaks) - 1
        if start <= week and week <= last:
            return (name, period)

        # check if this could be the closests one
        if week < start:
            diff = start - week
            if closests[0] is None:
                closests[0] = (name, period)
                closests[1] = diff
            elif closests[1] < diff:
                closests[0] = (name, period)
                closests[1] = diff

    return closests[0]


def get_weekdates(year, week):
    start = datetime.datetime.strptime(f"{year} {week} 1", "%G %V %u").date()
    end = datetime.datetime.strptime(f"{year} {week} 5", "%G %V %u").date()
    return start, end


def create_time_table(semester_info, out=Path("timetable/timetable.rst")):
    """Parse the `semester` information (basically a dictionary) and create an upto date
    timetable with tabs so it is easy for the students.

    Parameters
    ----------
    semester : dict
        contains information related to the current semester. It contains details such as:
        - semester start (ISO-8601 week number)
        - semester breaks (also ISO-8601 week numbers). Generally, only Easter and autumn break
    out : Path or str
        where to write the information
    """

    # Get today
    today = datetime.datetime.today()
    # TODO use env to enable dev for checking dates
    #today = datetime.datetime.strptime("2023 9 5", "%Y %m %d")

    print(f"timetable: will create an on-the-fly updated timetable in {out!s}")
    print(f"timetable: the current time will be: {today.isoformat(' ', 'minutes')}")

    # Determine the week (added in 3.6)
    year, week, day, hour = map(int, today.strftime("%G %V %u %H").split())
    print(f"timetable: parsed time: {year} {week} {day} {hour}")

    # perhaps some logic here.
    # Get the number of weeks in each period

    period_names = [
        "january",
        "spring",
        "june",
        "autumn",
    ]
    # default information for a given semester
    periods = [(period, semester_info[period]) for period in period_names]

    # retrieve current semester based on the current year...
    semester = semester_info[f"{year}"]
    fill_defaults(semester, periods)
    period = get_period(periods, semester, week)
    if period is None:
        print("Failed current semester, trying next year, this will likely fail!")
        # reset year
        year += 1
        week = day = hour = 1
        semester = semester_info[f"{year}"]
        fill_defaults(semester, periods)
        period = get_period(periods, semester, week)

    # now choose the exact semester from the chosen period
    semester = semester[period[0]]

    # correct if we are past a new day
    # Basically this will only influence Friday's
    # since then it should show for next week!
    if hour >= 18:
        day += 1
    if day > 5:
        week += 1

    # get semester information
    name = semester["name"]
    week_start = semester["week-start"]
    weeks = semester["weeks"]
    week_breaks = semester["week-breaks"]
    if not isinstance(week_breaks, list):
        week_breaks = [week_breaks]

    def count_weeks_after_breaks(week, week_breaks):
        count = 0
        for week_break in week_breaks:
            if week_break <= week:
                count += 1
        return count


    # get week
    offset_week = week - week_start
    offset_week -= count_weeks_after_breaks(week, week_breaks)

    # start writing out
    f = open(out, 'w')

    # open the tabs
    if offset_week < -1:
        f.write(f"The {name} semester will start in {-offset_week} weeks.\n\n")
    elif offset_week == -1:
        f.write(f"The {name} semester will start in {-offset_week} week.\n\n")
    elif offset_week < weeks:
        if day > 5:
            f.write(f"The current/coming {name} semester week is {offset_week+1}.\n\n")
        else:
            f.write(f"The current {name} semester week is {offset_week+1}.\n\n")

    # Now produce the content
    f.write(".. tab-set::\n")
   
    timetable_path = Path("timetable").resolve()

    def indent(s, indent=8):
        indent = " " * indent
        return indent + s.replace("\n", f"\n{indent}") + "\n"

    # ensure we will not use older weeks
    first = "Week "
    for sem_week in range(max(0, offset_week), weeks):
        iso_week = week_start + sem_week
        iso_week += count_weeks_after_breaks(iso_week, week_breaks)

        start, end = get_weekdates(year, iso_week)
       
        f.write(indent(f"""\
.. tab-item:: {first}{sem_week+1}

""", 4))

        # add dates, note this REQUIRES AN EXTRA newline!
        f.write(indent(f"| *Dates*: {start.strftime('%d/%m')} -- {end.strftime('%d/%m')}"))
        f.write(indent(f"| *Danish week #*: {iso_week}\n"))

        if (timetable_path / f"{year}{iso_week}.rst").exists():
            f.write(indent(f".. include:: /timetable/{year}{iso_week}.rst"))
        else:
            f.write(indent(f"To be determined, come back later!"))
        f.write("\n")
        
        # signal nothing for the first one
        first = ""

    f.close()


    
    
