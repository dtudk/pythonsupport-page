# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


print("vvvvv INITIALIZING conf.py vvvvv")

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from pathlib import Path
import os
import datetime
import sys

html_logo = "_static/DTU_logo_Coral_RGB.png"


_cwd = Path().resolve()

# add the exts folder
sys.path.insert(1, str(_cwd))
from ps_modules.pageredirects import *
from ps_modules.create_timetabs import create_time_table

if sys.version_info >= (3, 11):
    import tomllib as toml
else:
    import toml


def version2tuple(vers):
    """Convert a `vers` to a tuple"""
    if isinstance(vers, tuple):
        return vers

    if isinstance(vers, str):
        vers = vers.split(".")
        v = []
        for vv in vers:
            try:
                v.append(int(vv))
            except:
                return tuple(v)
        return tuple(v)

    raise NotImplementedError()


year = datetime.date.today().year

project = "DTU Python support"
# conf.py
html_title = ""
html_short_title = ""

copyright = f"{year}, DTU Python support"
author = "DTU Python support developers"

# when we have a guideline:
_pref_symbol = ":fas:`ranking-star`"



# _pref_symbol = ""


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    # allow shorthands for links
    "sphinx.ext.extlinks",
    # allows to view code directly in the homepage
    "sphinx.ext.viewcode",
    # toggle-button on info/warning/...
    "sphinx_togglebutton",
    # create tabs and grouped tabs
    "sphinx_inline_tabs",
    # allow emoji's in the documentation
    "sphinxemoji.sphinxemoji",
    # allow copybutton on code-blocks
    "sphinx_copybutton",
    # design, grids etc.
    "sphinx_design",
    # enable target=_blank via jquery
    "sphinxcontrib.jquery",
]


# Add the spelling extension if available
try:
    import sphinxcontrib.spelling

    # spell checking
    extensions.append("sphinxcontrib.spelling")
except ImportError:
    print("cannot do spell checks! sphinxcontrib.spelling cannot be imported")

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

sphinxemoji_style = "twemoji"

templates_path = ["_templates"]
exclude_patterns = [
    "python/poetry.rst",
    "python/pipenv.rst",
    "python/pyenv.rst",
]


# Determine the standard year of the current semester
# I.e. this requires an update every 6 months to update correctly
def get_current_years():
    today = datetime.date.today()
    year = today.year
    year = (year - 1, year, year + 1)
    if today.month >= 7:
        # we are in the autumn, so it is *this* year and the next one
        year = year[1:]
    else:
        year = year[:2]
    return year


_year = get_current_years()

print(
    f"""\
ps: Links to DTU's course database will be to the year:
ps:      {_year[0]}-{_year[1]}"""
)


# Read in all the content from the course configuration.
# This is much simpler to maintain and we could allow other
# details as well.
_conf_toml = toml.load(open("ps_configuration.toml", "rb"))
_pythonsupport = _conf_toml["pythonsupport"]

url = _pythonsupport["homepage"]

_coursepages = HomepageFormatter()
# Add all courses here
# These will be used to format the homepages
# I.e. this class can be used in extlinks
for course, info in _conf_toml["course"].items():
    _coursepages.add(course, info["home"])

extlinks = {
    # easy mails
    "mail": ("mailto:%s", "%s"),
    # easy show the entire link without duplicating the string
    # I don't know if it can work in other ways
    "full-link": ("%s", "%s"),
    # direct links to the course documentation @ pythonsupport.dtu.dk
    "course": (":doc:`/course/%s/index`", "%s"),
    # direct links to DTU's course database for the course
    # When courses changes numbers etc. some might
    "course-base": (
        Coursebase(_conf_toml["dtu"]["course-base"] + "/course"),
        CourseStrip(),
    ),
    # direct links to DTU's course database for the course
    # When courses changes numbers etc. some might
    "course-home": (_coursepages, "%s"),
    # Links to issues on this webpage:
    "gh-issue": ("https://github.com/dtudk/pythonsupport-page/issues/%s", "%s"),
    # Links to issues on this webpage:
    "gh-disc": ("https://github.com/dtudk/pythonsupport-page/discussions/%s", "%s"),
}

_discord_general = _pythonsupport["discord-channel"]
_discord_invite = _pythonsupport["discord-invite"]


# Add common links to all
rst_epilog = f"""\

.. _ps-discord-general: {_discord_general}
.. _ps-discord-invite: {_discord_invite}

.. _python-org: https://www.python.org
.. _python-org-down: https://www.python.org/downloads/
.. _python-org-down-win: https://www.python.org/downloads/windows
.. _python-org-down-mac: https://www.python.org/downloads/macos
.. _python-org-down-linux: https://www.python.org/downloads/linux
.. _python-org-rec: {_pythonsupport['python-org-recommended']}
.. _pypi-org: https://pypi.org
.. _pip-org: https://pip.pypa.io/en/stable

.. _numpy: https://numpy.org/doc/stable
.. _scipy: https://docs.scipy.org/doc/scipy
.. _matplotlib: https://matplotlib.org

.. _anaconda: https://www.anaconda.com/
.. _anaconda-down: https://www.anaconda.com/download#downloads
.. _miniconda: https://docs.conda.io/en/latest/miniconda.html
.. _mamba: https://mamba.readthedocs.io/

.. _env-venv: https://docs.python.org/3/library/venv.html
.. _env-conda: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
.. _env-virtualenv: https://virtualenv.pypa.io/en/latest/
"""


# do not allow to collapse the tabs (always show one tab)
sphinx_tabs_disable_tab_closing = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static", "../images"]

# this move will work regardless of hover...
_fa_move = "shake-hover"


windows_link = [
{
    "name": "Windows",
        "url": "https://www.microsoft.com/windows",
        "icon": "fa-brands fa-windows",
        "type": "fontawesome", }
]


_icon_links = [
    {
        "name": "Chat with us on Discord",
        "url": _discord_invite,
        "icon": f"fa-brands fa-discord {_fa_move}",
        "type": "fontawesome",
    },
    {
        "name": "Contact us by mail",
        "url": f"mailto:{_pythonsupport['mail']}",
        "icon": f"fa-solid fa-envelope {_fa_move}",
        "type": "fontawesome",
    },
#    {
#       "name": "DTU help | External pages",
#       "url": "#;",
#       "icon": "fa-solid fa-ellipsis-vertical",
#       "type": "fontawesome",
#   },
#   {
#       "name": "Official Python homepage",
#       "url": "https://www.python.org",
#       "icon": f"fa-brands fa-python {_fa_move}",
#       "type": "fontawesome",
#   },
#   {
#       "name": "Conda documentation",
#       "url": "https://docs.conda.io/en/latest/index.html",
#       "icon": "_static/anaconda_logo.svg",
#       "type": "local",
#   },
#   {
#       "name": "PyPi package installation repository",
#       "url": "https://pypi.org/",
#       "icon": "_static/logo-small.2a411bc6.svg",
#       "type": "local",
#   },
]


html_theme_options = {
    "navbar_center": ["logo_button.html", "navbar-nav"],
    "navbar_end": ["theme-switcher"],
    "icon_links": _icon_links,
    "header_links_before_dropdown": 10,
    "back_to_top_button": True,
    "use_repository_button": True,
    "repository_provider": "github",
    "repository_url": _pythonsupport["repository"],
}


_course_json_url = "_static/course_switcher.json"
if False:
    html_theme_options["switcher"] = {
        "json_url": _course_json_url,
        "version_match": "courses",
    }
    html_theme_options["switcher"][
        "json_url"
    ] = "file:///home/nicpa/dcc/python-support/ps-webpage/build/html/_static/course_switcher.json"
    html_theme_options["navbar_center"].append("version-switcher")

html_js_files = ["js/external_tab.js", "js/custom.js"]

html_css_files = [
    ("css/bannerStyles.css", {"priority": 999}),
    ("css/questionairStyles.css", {"priority": 999}),
    ("css/popupStyles.css", {"priority": 999}),
    ("css/custom_styles.css", {"priority": 998}),
    "css/colors.css",
]


import pydata_sphinx_theme

if version2tuple(pydata_sphinx_theme.__version__) >= (0, 14):
    print("ps: will use fontawesome 6 css")
    html_css_files.append("css/fontawesome6.css")
else:
    print("ps: will use fontawesome 5 css")
    html_css_files.append("css/fontawesome5.css")


# Include summary of the search stuff
html_show_search_summary = True

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

# TODO add custom codes to make this false when releasing
# Some kind of env-variable
_include_todos = os.environ.get("PS_INCLUDE_TODOS", "False")
if len(_include_todos) > 0:
    _include_todos = _include_todos[0].lower()
    _include_todos = _include_todos in ("1", "t", "y")

if _include_todos:
    todo_include_todos = True
    print("ps: Will SHOW TODOS")
else:
    todo_include_todos = False
    print("ps: Will NOT SHOW TODOS")


# Spell checking
spelling_lang = "en_US"
tokenizer_lang = "en_US"


# Automatically call the switcher creator
def course_switcher(out=_course_json_url):
    """Create a course switcher based on the available courses

    This small snippet will automatically search the directories in:
    `courses/` and add any course to the file
    """
    from pathlib import Path
    import json

    # current path
    cwd = Path(__file__).parent

    # Now search directories in the /courses folder

    courses = cwd / "courses"

    data = [
        {
            "name": "courses",
            "version": "courses",
            # "url": f"pathto(courses/index.html, 1)",
            "url": f"courses/index.html",
            "preferred": True,
        }
    ]

    for course in courses.glob("*"):
        if not course.is_dir():
            continue  # only search directories

        if not (course / "index.rst").exists():
            continue  # not a valid course

        data.append(
            {
                "name": course.name,
                "version": course.name,
                # "url": f"pathto(courses/{course.name}/index.rst, 1)",
                "url": f"courses/{course.name}/index.rst",
            }
        )

    json.dump(data, open(out, "w"), indent=4)


course_switcher()


create_time_table(_conf_toml["semester"])

# Now exclude the years that are not going to be used
week = int(datetime.date.today().strftime("%V"))
for y in range(2023, year + 1):
    if y < year:
        week_end = 54
    else:
        week_end = week
    for w in range(1, week_end):
        if (_cwd / "timetable" / f"{y}{w}.rst").is_file():
            exclude_patterns.append(f"timetable/{y}{w}.rst")


# Determine the days we are open online
_week_days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
_week_days_dict = dict((day, i) for i, day in enumerate(_week_days))

_days = _pythonsupport["online-days"]
_days = [_week_days_dict[day] for day in _days]
_days.sort()

_min_days = min(_days)
_max_days = max(_days)
if _max_days - _min_days + 1 == len(_days):
    # continuous days
    _online_days = f"{_week_days[_min_days]} -- {_week_days[_max_days]}"
elif len(_days) == 0:
    _online_day = "Closed!"
    raise NotImplementedError
elif len(_days) == 1:
    _online_days = _week_days[_days[0]]
else:
    _online_days = ", ".join([_week_days[day] for day in _days[:-1]])
    _online_days = f"{_online_days} and {_week_days[_days[-1]]}"

print("ps: online days (Monday == 0) ", _days)

# Create jinja-replacements
html_context = {
    # Other useful data
    "github_user": "dtudk",
    "github_repo": "pythonsupport-page",
    "mail": f":mail:{_pythonsupport['mail']}",
    "discord": _discord_invite,
    "ps_repository": _pythonsupport["repository"],
    "github_version": "main",
    "path_to_docs": "docs/",
    "pref_symbol": _pref_symbol,
    "python_org_rec": _pythonsupport["python-org-recommended"],
    "python_version_min": _pythonsupport["python-version"]["min"],
    "python_version_max": _pythonsupport["python-version"]["max"],
    "python_version_recommended": _pythonsupport["python-version"]["recommended"],
    "python_version": _pythonsupport["python-version"]["recommended"],
    # Installation methods
    "pip": "pip",
    "conda": "conda",
    "poetry": "poetry",
    "pyenv": "pyenv",
    # Default naming conventions
    "video_install": "Video Guide --- description found below :fas:`down-long`",
    # dates
    "current_year": f"{year}",
    # Virtual environment methods
    "venv": f"venv {_pref_symbol}",
    "virtualenv": "virtualenv",
    "condaenv": "conda",
    # Operating systems
    "windows": "Windows",
    "macos": "MacOS",
    "linux": "Linux",
    "vscode": "VS Code",
    "spyder": "Spyder",
    # Operating shells
    "win_powershell": "Windows | PS",
    "win_batch": "Windows | Batch",
    "mac_bash": "MacOS",
    "linux_bash": "Linux",
    "unix_bash": "Bash",
    # Cheatsheet information
    "cheatsheet_icon": ":fas:`toolbox`",
    "cheatsheet_color": "muted",
    "windows_icon": ":fab:`windows`",
    "linux_icon": ":fab:`linux`",
    "apple_icon":  ":fab:`apple`",
    "apple_app_store":   ":fab:`app-store`",
    "arrow_icon": ":fas:`arrow-right`",
    # Timetable
    "timetable_widths": "15 17 17 17 17 17",
    # online days
    "online_days": _online_days,
}


print("^^^^^ DONE conf.py ^^^^^")


def rstjinja(app, source):
    """
    Render pages as a jinja template for fancy templating goodness.

    The reason for resorting to the jinja templating is simply because
    the directives might not always like combinations of replacement
    directives *and* other directives, e.g. the following would fail:

    .. |win| replace:: Hello :fas:`ranking-star`

    .. tab:: |win|

    When templating all gets replaced *in-place*.

    Thanks for https://www.ericholscher.com/blog/2016/jul/25/integrating-jinja-rst-sphinx/
    """
    # Make sure we're outputting HTML
    if app.builder.format != "html":
        return source

    return app.builder.templates.render_string(source, app.config.html_context)


def rstjinja_source(app, docname, content):
    """source-read event"""
    content[0] = rstjinja(app, content[0])


def rstjinja_include(app, relative_path, parent_docname, content):
    """include-read event"""
    content[0] = rstjinja(app, content[0])


def setup(app):

    app.connect("source-read", rstjinja_source)
    app.connect("include-read", rstjinja_include)

