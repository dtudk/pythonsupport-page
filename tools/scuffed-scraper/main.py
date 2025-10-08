# DTU Scuffed Course Scraper
# Copyright (C) 2023 Sofus Albert Høgsbro Rose
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys

SUPPORTED_PY_MAJOR = 3
MIN_PY_MINOR_VERSION = 11
if not all(
    [
        sys.version_info.major == SUPPORTED_PY_MAJOR,
        sys.version_info.minor >= MIN_PY_MINOR_VERSION,
    ],
):
    print(f"Python 3.X minor version must be > 3.{MIN_PY_MINOR_VERSION}")
    sys.exit(1)

import enum
import json
import re
from pathlib import Path
from urllib.parse import quote as urlquote

import requests
import tomlkit
from bs4 import BeautifulSoup
from markdownify import markdownify as md

## md() stringifies HTML from course descriptions into a readable form.

COURSE_YEAR = 2020
COURSE_YEAR_STR = str(COURSE_YEAR)


class Lang(enum.StrEnum):
    ENGLISH = "en"
    DANISH = "dk"


COURSE_SCRAPES_URL = \
f"https://kurser.dtu.dk/course/{COURSE_YEAR}-{COURSE_YEAR+1}/{{course_id}}"

COURSE_SCRAPES_PATHS = {
    Lang.ENGLISH: Path(__file__).parent / COURSE_YEAR_STR / "course-scrapes" / "en",
    Lang.DANISH: Path(__file__).parent / COURSE_YEAR_STR / "course-scrapes" / "dk",
}
list(COURSE_SCRAPES_PATHS.values())[0].parent.mkdir(exist_ok=True)
for course_scrape_lang_path in COURSE_SCRAPES_PATHS.values():
    course_scrape_lang_path.mkdir(exist_ok=True)

SEARCH_SCRAPES_PATH = Path(__file__).parent / COURSE_YEAR_STR / "search-scrapes"
SEARCH_SCRAPES_PATH.mkdir(exist_ok=True)

COURSE_CONFIGS_PATH = Path(__file__).parent / COURSE_YEAR_STR / "courses"
COURSE_CONFIGS_PATH.mkdir(exist_ok=True)


####################
# - DTU Schemas
####################
class Degree(enum.StrEnum):
    BENG = enum.auto()
    BSC = enum.auto()
    MSC = enum.auto()
    PHD = enum.auto()


class CourseClassi(enum.StrEnum):
    CORE = enum.auto()  ## "Polytechnical Foundation"
    TECHNICAL_SPECIALIZATION = enum.auto()  ## "Programme-Specific Course"
    ELECTIVE = enum.auto()
    PROJECT = enum.auto()
    PHD = enum.auto()


class DTUProgramme(enum.StrEnum):
    pass


class DTUProgrammeBSC(DTUProgramme):
    GENERAL_ENGINEERING = enum.auto()


class DTUDepartment(enum.StrEnum):
    # From https://www.dtu.dk/english/research/departments-and-groups
    DTU_AQUA = "National Institute of Aquatic Resources"
    DTU_BIOENGINEERING = "Department of Biotechnology and Biomedicine"
    DTU_BIOSUSTAIN = "The Novo Nordisk Foundation Center for Biosustainability"
    DTU_CHEMICAL_ENGINEERING = "Department of Chemical and Biochemical Engineering"
    DTU_CHEMISTRY = "Department of Chemistry"
    DTU_COMPUTE = "Department of Applied Mathematics and Computer Science"
    DTU_CONSTRUCT = "Department of Civil and Mechanical Engineering"
    DTU_ELECTRO = "Department of Electrical and Photonics Engineering"
    DTU_ENERGY = "Department of Energy Conversion and Storage"
    DTU_ENGINEERING_TECHNOLOGY = "Department of Engineering Technology and Didactics"
    DTU_ENTREPRENEURSHIP = "Centre for Technology Entrepreneurship"
    DTU_FOOD = "National Food Institute"
    DTU_HEALTH_TECH = "Department of Health Technology"
    DTU_LEARN_FOR_LIFE = "DTU Learn for Life"
    DTU_MANAGEMENT = "Department of Technology, Management and Economics"
    DTU_NANOLAB = "National Centre for Nano Fabrication and Characterization"
    DTU_OFFSHORE = "Danish Offshore Technology Centre"
    DTU_PHYSICS = "Department of Physics"
    DTU_SKYLAB = "DTU Skylab"
    DTU_SPACE = "National Space Institute"
    DTU_SUSTAIN = "Department of Applied Mathematics and Computer Science"
    DTU_WIND = "Department of Wind and Energy Systems"


####################
# - Scrape Lookup Tables
####################
SCRAPE_PROGRAMME_TO_PROGRAMME = {
    "General Engineering": DTUProgrammeBSC.GENERAL_ENGINEERING,
}

SCRAPE_DEPT_TO_DEPT = {
    ## https://chat.openai.com/share/ee154f25-02f8-449c-8ab5-2ed965170196
    "01 Department of Applied Mathematics and Computer Science": DTUDepartment.DTU_COMPUTE,
    "10 Department of Physics": DTUDepartment.DTU_PHYSICS,
    "12 Department of Environmental and Resource Engineering": DTUDepartment.DTU_SUSTAIN,  # No exact match found
    "13 Department of Transport": None,  ## This Department Has no Courses
    "22 Department of Health Technology": DTUDepartment.DTU_HEALTH_TECH,
    "23 National Food Institute": DTUDepartment.DTU_FOOD,
    "24 National Veterinary Institute": None,  ## This Department Has no Courses
    "25 National Institute of Aquatic Resources": DTUDepartment.DTU_AQUA,
    "26 Department of Chemistry": DTUDepartment.DTU_CHEMISTRY,
    "27 Department of Biotechnology and Biomedicine": DTUDepartment.DTU_BIOENGINEERING,
    "28 Department of Chemical Engineering": DTUDepartment.DTU_CHEMICAL_ENGINEERING,  # No exact match but close
    "29 DTU Biosustain": DTUDepartment.DTU_BIOSUSTAIN,
    "30 National Space Institute": DTUDepartment.DTU_SPACE,
    "33 Department of Micro and Nanotechnology": None,  ## This Department Has no Courses
    "34 Department of Electrical and Photonics Engineering": DTUDepartment.DTU_ELECTRO,
    "36 DTU Bioinformatics": None,  ## This Department Has no Courses
    "38 DTU Entrepreneurship": DTUDepartment.DTU_ENTREPRENEURSHIP,
    "41 Department of Civil and Mechanical Engineering": DTUDepartment.DTU_CONSTRUCT,  # No exact match but close
    "42 Department of Technology, Management and Economics": DTUDepartment.DTU_MANAGEMENT,
    "46 Department of Wind and Energy Systems": DTUDepartment.DTU_WIND,
    "47 Department of Energy Conversion and Storage": DTUDepartment.DTU_ENERGY,
    "56 DTU Nanolab": DTUDepartment.DTU_NANOLAB,  # NOTE: Mismatch HTML ("59") value and label ("56").
    "62 Department of Engineering Technology and Didactics": DTUDepartment.DTU_ENGINEERING_TECHNOLOGY,  # No exact match but close
    "88 Other courses": None,  ## Either use "Department Involved", "External Institution", or use the Department of Course Responsible.
}

SCRAPE_CONTENT_TO_CONTENT = {
    "General course objectives": "summary",
    "Learning objectives": "objectives",
    "Content": "content",
    "CourseLiterature": "literature",
    "Last updated": "updated",
    "Remarks": "remarks",
}

SECTION_I18N = {
    "summary": True,
    "objectives": True,
    "content": True,
    "literature": False,
    "updated": False,
    "remarks": True,
}


####################
# - Download Course
####################
class LangSessionCode(enum.StrEnum):
    EN = "en-GB"
    DK = "da-DK"


LANG_TO_LANGSESSIONCODE = {
    Lang.ENGLISH: LangSessionCode.EN,
    Lang.DANISH: LangSessionCode.DK,
}


def g_session_cookies(
    lang: LangSessionCode = LangSessionCode.EN,
) -> requests.cookies.RequestsCookieJar:
    cookie_jar = requests.get("https://kurser.dtu.dk").cookies
    cookie_jar["{DTUCoursesPublicLanguage}"] = lang

    return cookie_jar


def g_course_soup(course_id: str, lang: Lang) -> BeautifulSoup:
    path_scrape_cache = COURSE_SCRAPES_PATHS[lang] / f"{course_id}.html"
    if path_scrape_cache.is_file():
        with path_scrape_cache.open() as f:
            return BeautifulSoup(f.read(), features="html.parser")

    else:
        url = COURSE_SCRAPES_URL.format(course_id=course_id)
        print(f"[{url}] GET {lang} to {path_scrape_cache}...")
        r = requests.get(
            f"{url}",
            cookies=g_session_cookies(LANG_TO_LANGSESSIONCODE[lang]),
        )

        soup = BeautifulSoup(r.text, features="html.parser")
        with path_scrape_cache.open("w") as f:
            f.write(str(soup))

        return soup


####################
# - Parse Course
####################
def parse_course_title_en(
    course_id: str,
    soup: BeautifulSoup,
):
    return (
        soup.find("h2", style=lambda val: "font-family:verdana;" in val)
        .get_text(strip=True)
        .split(course_id)[1]
        .strip()
    )


def parse_course_information(course_id: str, soups: dict[Lang, BeautifulSoup]):
    print(f"[https://kurser.dtu.dk/course/{course_id}] Scraping {course_id}...")
    course = {
        "course_id": course_id,
        "name": {},
        "classification": {},
        "assessment": {},
        "faculty": {},
        "summary": {},
        "objectives": {},
        "content": {},
        "remarks": {},
    }

    ## Find Course Information Header
    el_header_of_tables = soups[Lang.ENGLISH].find(
        "div",
        string=re.compile("^Course information$"),
    )
    if not el_header_of_tables:
        msg = "<div> with 'Course information' Not Found."
        raise RuntimeError(msg)

    ## Parse "Course Information" Tables
    (
        el_table_title,
        el_table_properties,
        el_table_department,
    ) = el_header_of_tables.find_next_siblings("table")
    if any(
        [
            not bool(el_table_title),
            not bool(el_table_properties),
            not bool(el_table_department),
        ],
    ):
        msg = "'Course information' Tables Not Found"
        raise RuntimeError(msg)

    ## Parse: Title Table
    for row in el_table_title.tbody.find_all(
        "tr",
        recursive=False,
    ):
        label = row.find("label").get_text(strip=True)

        match label:
            case "Danish title":
                course["name"][Lang.DANISH] = row.find_all("td")[1].get_text(
                    strip=True,
                )
                course["name"][Lang.ENGLISH] = parse_course_title_en(
                    course_id,
                    soups[Lang.ENGLISH],
                )

            case "Language of instruction":
                course["language"] = {
                    "English": Lang.ENGLISH,
                    "Danish": Lang.DANISH,
                }[row.find_all("td")[1].get_text(strip=True)]

            case "Point( ECTS )":
                course["ects"] = (
                    row.find_all("td")[1].get_text(strip=True).replace(",", ".")
                )

            case "Course type":
                value_cell = row.find_all("td")[1]

                ## Determine Degree (for which type is elective by default)
                scraped_degree_id = value_cell.find_all("div")[0].get_text(
                    strip=True,
                )

                if "Ph.D" in scraped_degree_id:
                    degree = Degree.PHD
                    default_degree_classi = CourseClassi.PHD

                else:
                    degree = {
                        "BSc": Degree.BSC,
                        "BEng": Degree.BENG,
                        "MSc": Degree.MSC,
                        "Parttime master": Degree.MSC,
                    }[scraped_degree_id]
                    default_degree_classi = CourseClassi.ELECTIVE

                course["degree"] = degree
                course["classification"][degree] = default_degree_classi

            # case _:
            #    print(f"unparsed title information: {label}")

    ## Parse: Title Table
    for row in el_table_properties.tbody.find_all(
        "tr",
        recursive=False,
    ):
        try:
            label = row.find("label").get_text(strip=True)
        except AttributeError:
            print("Skipping course" + str(row))
            continue

        match label:
            case "Schedule":
                course["schedule"] = row.find_all("td")[1].get_text(strip=True)

            case "Location":
                course["location"] = row.find_all("td")[1].get_text(strip=True)

            case "Type of assessment":
                course["assessment"]["type"] = row.find_all("td")[1].get_text(
                    strip=True
                )

            case "Aid":
                course["assessment"]["aid"] = row.find_all("td")[1].get_text(strip=True)

            case "Exam duration":
                course["assessment"]["duration"] = row.find_all("td")[1].get_text(
                    strip=True
                )

            case "Evaluation":
                course["assessment"]["evaluation"] = row.find_all("td")[1].get_text(
                    strip=True
                )

            # case _:
            #    print(f"unparsed properties information: {label}")

    ## Parse: Department Table
    for row in el_table_department.tbody.find_all(
        "tr",
        recursive=False,
    ):
        label = row.find("label").get_text(strip=True)

        match label:
            case "Responsible":
                el_val = row.find_all("td")[1]

                els_course_responsible_email = el_val.find_all(
                    "a",
                    href=lambda val: "mailto:" in val,
                )
                if len(els_course_responsible_email) == 1:
                    course["faculty"]["responsible"] = els_course_responsible_email[0][
                        "href"
                    ].split("mailto:")[1]

            case "Course co-responsible":
                el_val = row.find_all("td")[1]

                els_course_coresponsible_email = el_val.find_all(
                    "a",
                    href=lambda val: "mailto:" in val,
                )

                course["faculty"]["coresponsibles"] = [
                    el_course_coresponsible_email["href"].split("mailto:")[1]
                    for el_course_coresponsible_email in els_course_coresponsible_email
                ]

    ## Parse: Info, Objectives, Learning Objectives, Content, Literature, Last Updated
    els_section_header_raw = soups[Lang.ENGLISH].find_all(
        "div",
        class_="bar",
    )
    if not els_section_header_raw:
        return None

    els_section_header = [
        el_section_header
        for el_section_header in els_section_header_raw
        if el_section_header.get_text(strip=True) != "Course information"
    ]
    section_headers = [
        el_section_header.get_text(strip=True)
        for el_section_header in els_section_header
    ]
    accumulated_text = []
    section_header_iter = iter(enumerate(section_headers))
    active_section_header = next(section_header_iter)
    for el_content in els_section_header[0].parent.contents[1:]:
        if (
            el_content.get_text(strip=True)
            in section_headers[active_section_header[0] :]
        ):
            # Flush Section to Course
            course_section = SCRAPE_CONTENT_TO_CONTENT[active_section_header[1]]

            if SECTION_I18N[course_section]:
                course[course_section][Lang.ENGLISH] = md(
                    " ".join(accumulated_text),
                )
            else:
                course[course_section] = md(" ".join(accumulated_text))
            del accumulated_text[:]

            # Iterate to Next Section
            try:
                active_section_header = next(section_header_iter)
            except StopIteration:
                break
        else:
            accumulated_text.append(str(el_content).strip())

    # Flush Last Section to Course
    course_section = SCRAPE_CONTENT_TO_CONTENT[active_section_header[1]]

    if SECTION_I18N[course_section]:
        course[course_section][Lang.ENGLISH] = md(" ".join(accumulated_text))
    else:
        course[course_section] = md(" ".join(accumulated_text))

    return course


####################
# - Parse Course Search
####################
def g_course_search_home_soup(lang: Lang) -> BeautifulSoup:
    path_scrape_cache = SEARCH_SCRAPES_PATH / "search-home.html"
    if path_scrape_cache.is_file():
        with path_scrape_cache.open() as f:
            return BeautifulSoup(f.read(), features="html.parser")

    else:
        r = requests.get(
            "https://kurser.dtu.dk",
            cookies=g_session_cookies(LANG_TO_LANGSESSIONCODE[lang]),
        )

        soup = BeautifulSoup(r.text, features="html.parser")
        with path_scrape_cache.open("w") as f:
            f.write(str(soup))

        return soup


def parse_course_search_home(soup):
    el_schedule_placement_form = soup.find("select", id="SchedulePlacement")
    schedule_placements = {
        schedule_placement
        for el_schedule_placement in el_schedule_placement_form.find_all(
            "option",
        )
        for schedule_placement in el_schedule_placement["value"].split(";")
    }

    el_department_form = soup.find("select", id="Department")
    department_nums = {
        el_department_entry["value"]
        for el_department_entry in el_department_form.find_all("option")
    }

    query_parameters = (
        [
            "CourseCode=",
            "SearchKeyword=",
        ]
        + [
            f"SchedulePlacement={urlquote(schedule_placement)}"
            for schedule_placement in schedule_placements
        ]
        + [
            f"Department={urlquote(department_num)}"
            for department_num in department_nums
        ]
        + [
            "CourseType=",
            "TeachingLanguage=",
        ]
    )

    base_search_url = "https://kurser.dtu.dk/search?"
    base_print_url = "https://kurser.dtu.dk/print/courses?"

    return {
        "url_search_all": base_search_url
        + "&".join(
            [
                *query_parameters,
                "OpenUniversity=False",
                "Volume=",
            ],
        ),
        "url_print_all": base_print_url + "&".join(query_parameters),
    }


####################
# - Download All Courses
####################
def g_course_search_all_soup(url_search_all, lang: Lang):
    path_scrape_cache = SEARCH_SCRAPES_PATH / "search-all.html"
    if path_scrape_cache.is_file():
        with path_scrape_cache.open() as f:
            return BeautifulSoup(f.read(), features="html.parser")

    else:
        r = requests.get(
            url_search_all,
            cookies=g_session_cookies(LANG_TO_LANGSESSIONCODE[lang]),
        )

        soup = BeautifulSoup(r.text, features="html.parser")
        with path_scrape_cache.open("w") as f:
            f.write(str(soup))

        return soup


def parse_course_search_all(course_search_soup):
    els_course_links = course_search_soup.find_all(
        "a",
        href=lambda val: val.startswith("/course/"),
    )

    return {
        el_course_link.get_text(strip=True).split(" - ")[0]
        for el_course_link in els_course_links
    } - {"Study Planner"}


####################
# - Main
####################
if __name__ == "__main__":
    print("[https://kurser.dtu.dk/] Processing Home...")
    course_search_home_soup = g_course_search_home_soup(Lang.ENGLISH)
    course_search_urls = parse_course_search_home(course_search_home_soup)

    print("[https://kurser.dtu.dk/search?*] Processing Search for All Courses...")
    course_search_all_soup = g_course_search_all_soup(
        course_search_urls["url_search_all"],
        Lang.ENGLISH,
    )
    course_ids = parse_course_search_all(course_search_all_soup)
    print()
    print()


    # for course_id in {"28150"}:
    for course_id in course_ids:
        url = COURSE_SCRAPES_URL.format(course_id=course_id)
        print(f"[{url}] Processing Course {course_id}...")

        course_soups = {
            Lang.ENGLISH: g_course_soup(course_id, Lang.ENGLISH),
            Lang.DANISH: g_course_soup(course_id, Lang.DANISH),
        }
        try:
            course_config = parse_course_information(course_id, course_soups)
        except (RuntimeError, KeyError):
            print(f"[{url}] Could not find information, we'll skip the course...")
            continue

        def reparse_toml(toml_string):
            lines = toml_string.split("\n")

            reparsed_lines = []
            for line in lines:
                line_match = re.match(
                    r"(?P<indent>\s*)(?P<lang>en|dk)\s*=\s*\"(?P<line_string>.*)\"",
                    line,
                )
                if line_match and "\\n" in line_match["line_string"]:
                    line_string = (
                        line_match["line_string"]
                        .replace("\\n*", "  \\n*")
                        .replace(
                            "A student who has met the objectives of the course will be able to: *",
                            "A student who has met the objectives of the course will be able to:  \\n*",
                        )
                    )
                    real_lines = [
                        real_line.replace("\\n", " ").strip()
                        for real_line in line_string.split("  \\n")
                    ]
                    real_lines = [
                        (
                            real_line[:2] + real_line[2:].capitalize()
                            if real_line.startswith("* ")
                            else real_line
                        )
                        for real_line in real_lines
                    ]

                    reparsed_lines += [
                        line_match["indent"] + line_match["lang"] + ' = """',
                        *[line_match["indent"] + real_line for real_line in real_lines],
                        line_match["indent"] + '"""',
                    ]

                else:
                    reparsed_lines.append(line)

            return "\n".join(reparsed_lines)

        path_course_config = COURSE_CONFIGS_PATH / f"{course_id}.toml"
        with path_course_config.open("w") as f:
            toml_string = tomlkit.dumps(course_config)
            f.write(reparse_toml(toml_string))

        print(f"[{url}] Wrote to {path_course_config}...")
        print()
        print()
