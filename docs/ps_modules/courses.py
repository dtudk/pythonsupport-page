"""Automatic course content creator.

An automatic scraper for course details in the course folder.

It will automatically create the necessary rst files when building
the documentation.
"""

import tomllib
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Any, Dict, Self

__all__ = ["create_courses"]


class PeriodsEnum(StrEnum):
    """Base for enumerated options for periods

    Members are declared as
    ``NAME = "long-name", "short-name"``.
    """

    _short_name: str

    def __new__(cls, long_name: str, short_name: str):
        obj = str.__new__(cls)
        obj._value_ = long_name
        obj._short_name = short_name
        return obj

    @property
    def long_name(self) -> str:
        return self.value

    @property
    def short_name(self) -> str:
        return self._short_name

    def __str__(self) -> str:
        return f"{self!s}({self.short_name})"


class Period(PeriodsEnum):
    JANUARY = "january", "jan"
    SPRING = "spring", "F"
    JUNE = "june", "jun"
    AUGUST = "august", "aug"
    AUTUMN = "autumn", "E"
    SPRING_AUTUMN = "spring & autumn", "F+E"


@dataclass(frozen=True)
class CourseSchedule:
    year: int
    """The year it's running."""
    period: Period
    """The period in the year."""
    path: Path
    """The path for the schedule."""

    @property
    def years(self) -> str:
        """Return the two years it's running in"""
        if self.period.value in ("august", "autumn", "spring & autumn"):
            first = self.year
        else:
            first = self.year - 1
        return f"{first}-{first+1}"

    @property
    def short_year(self) -> int:
        return self.year - 2000

    def __eq__(self, other):
        return self.year == other.year

    def __lt__(self, other):
        return self.year < other.year

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year

    def __le__(self, other):
        return self.year <= other.year


@dataclass(frozen=True)
class Course:
    number: str
    schedules: list[CourseSchedule]
    name: str | None

    def runs(self, year: int) -> bool:
        """Check if the course runs in the year"""
        return any([schedule.year == year for schedule in self.schedules])

    def remove(self, year: int) -> Self:
        """Return the same course, but removing `year` from the schedule"""
        schedules = list(filter(lambda schedule: schedule.year != year, self.schedules))
        return type(self)(self.number, schedules, self.name)

    def __add__(self, other):
        """Merge two course schedules"""
        assert self == other
        return type(self)(self.number, self.schedules + other.schedules, self.name)

    def sort_schedules(self) -> None:
        """Sorts the schedules, in-place"""
        self.schedules.sort()

    def __eq__(self, other):
        return self.number == other.number

    def __lt__(self, other):
        return int(self.number) < int(other.number)

    def __le__(self, other):
        return int(self.number) <= int(other.number)

    def __gt__(self, other):
        return int(self.number) > int(other.number)

    def __ge__(self, other):
        return int(self.number) >= int(other.number)


def parse_data(path: Path) -> Dict[str, Any]:
    """Parse toml files with applicable defaults for the year"""

    defaults = {}
    default = path.parents[0] / "default.toml"
    if default.exists():
        defaults = tomllib.load(default.open("rb"))
    meta = {**defaults, **tomllib.load(path.open("rb"))}
    return meta


def parse_course(path: Path) -> Course:

    meta = parse_data(path)

    # Default to the name of the rst document
    period = getattr(Period, meta.get("period").upper())

    # Determine the year from the current directory
    years = path.parents[0].stem.split("-")
    # TODO create a function to extract the correct year!
    if period.value in ("august", "autumn", "spring & autumn"):
        year = int(years[0])
    else:
        year = int(years[1])

    number = (meta.get("number") or path.stem).strip()
    name = meta.get("name")  # optional
    year = meta.get("year", int(year))

    schedule = CourseSchedule(year, period, path)

    return Course(number, [schedule], name)


def scrape_courses(path: Path) -> list[Course]:
    """Determine all unique courses and when they run."""

    courses = {}

    def add_course(course):
        nonlocal courses
        if course.number not in courses:
            courses[course.number] = course
        else:
            courses[course.number] = courses[course.number] + course

    for p in path.iterdir():
        if p.is_dir():
            for course in scrape_courses(p):
                add_course(course)

        elif "default" in p.stem:
            # The default is parsed separately
            continue

        elif p.suffix == ".toml":
            add_course(parse_course(p))

    courses = list(courses.values())

    return courses


def _COURSE_REF(*, schedule, course, **kwargs):
    return f".. _course-{schedule.years}-{course.number}:"


def _COURSE_HEADER(*, schedule, course, period, **kwargs):
    return f"""
{course.number} --- {period.short_name}{schedule.year}
=================================================================
"""


def _COURSE_OTHER_YEARS_HEADER(**kwargs):
    return f"""
.. dropdown:: Looking for other years?
    :icon: hourglass
"""


def _COURSE_OTHER_YEARS_ENTRY(*, schedule, course, period, **kwargs):
    return f"""\
    * :ref:`{period.value.title()} {schedule.year} ({period.short_name}{schedule.short_year}) <course-{schedule.years}-{course.number}>`
"""


def _COURSE_DEFAULT(*, schedule, course, **kwargs):
    return f"""
.. _course-{course.number}:
"""


def build_course(course, current_years) -> None:
    """Create the rst file in the respective directories"""
    if not course.schedules:
        print(f"course {course.number} has no schedules?...")
        return
    course.sort_schedules()

    for schedule in course.schedules:
        parts = []

        kwargs = {
            "schedule": schedule,
            "period": schedule.period,
            "course": course,
        }

        parts.append(_COURSE_REF(**kwargs))
        parts.append(_COURSE_HEADER(**kwargs))

        other_schedules = course.remove(schedule.year).schedules
        if other_schedules:
            # We have other, create links to other years
            # Since this is created from the sorted list, we know it's still
            # sorted.
            parts.append(_COURSE_OTHER_YEARS_HEADER(**kwargs))
            for other in other_schedules:
                parts.append(
                    _COURSE_OTHER_YEARS_ENTRY(
                        course=course, schedule=other, period=other.period
                    )
                )

        template = parse_data(schedule.path)["template"]
        parts.append(template.format(**kwargs))

        out = schedule.path.with_suffix(".rst")
        with open(out, "w") as fh:
            fh.write("\n".join([":orphan:", ""] + parts))

        last_schedule: CourseSchedule = schedule

    # Create the top-level course
    out = last_schedule.path.parents[1] / f"{course.number}.rst"
    parts[0] = _COURSE_DEFAULT(schedule=last_schedule, course=course)
    open(out, "w").write("\n".join(parts))


def create_courses(app, current_years):
    """Create all the courses"""
    print(f"course-database: will create the course database")
    src = Path(app.srcdir)
    course_dir = src / "course"

    # Extract all courses
    courses = scrape_courses(course_dir)

    for course in courses:
        build_course(course, current_years)

    print(f"course-database: done creating the course database")
