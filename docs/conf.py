# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os

project = 'DTU Python support'
copyright = '2023, DTU Python support developers'
author = 'DTU Python support developers'

url = "https://pythonsupport.dtu.dk"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    # allow shorthands for links
    'sphinx.ext.extlinks',
    # allows to view code directly in the homepage
    'sphinx.ext.viewcode',
    # create tabs and grouped tabs
    'sphinx_tabs.tabs',
    # allow emoji's in the documentation
    'sphinxemoji.sphinxemoji',
    # allow copybutton on code-blocks
    'sphinx_copybutton',
    # spell checking
    'sphinxcontrib.spelling',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None)
}

sphinxemoji_style = 'twemoji'

templates_path = ['_templates']
exclude_patterns = []


extlinks = {
    "mail": ("mailto:%s", "%s"),
    "course": (":doc:`/courses/%s/index`", "%s"),
}

_discord_general = "https://discord.com/channels/1138793943526539266/1138793944247980124"
_discord_invite = "https://discord.gg/h8EVaV9ShP"

# Add common links to all
rst_epilog = f"""

.. _01001: https://01001.compute.dtu.dk
.. _01003: https://01001.compute.dtu.dk
.. _02002: https://www.unknown-course-site.org
.. _02003: https://www.unknown-course-site.org

.. _ps-discord-general: {_discord_general}
.. _ps-discord-invite: {_discord_invite}

.. _python-org: https://www.python.org
.. _python-org-down: https://www.python.org/downloads/
.. _pypi-org: https://pypi.org
.. _pip: https://pip.pypa.io/en/stable

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

.. _dtu-courses: https://kurser.dtu.dk/

.. |conda| replace:: conda
.. |pip| replace:: pip

.. |win-powershell| replace:: Windows | PowerShell
.. |win-batch| replace:: Windows | Batch
.. |linux-bash| replace:: Linux | Bash
.. |macos-bash| replace:: MacOS | Bash
"""


# do not allow to collapse the tabs (always show one tab)
sphinx_tabs_disable_tab_closing = True

_navbar_start = [
    "link_courses.html",
]
_navbar_end = [
    "link_email.html",
    "link_discord.html",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "DTU Python support"
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

# this move will work regardless of hover...
_fa_move = ""

_icon_links = [
    {
        "name": "Python support - Discord channel invitation",
        "url": _discord_invite,
        "icon": f"fa-brands fa-discord {_fa_move}",
    },
    {
        "name": "Python support development page",
        "url": "https://github.com/dtudk/pythonsupport-page",
        "icon": f"fa-brands fa-github {_fa_move}",
    },
    {
        "name": "Python homepage",
        "url": "https://www.python.org",
        "icon": f"fa-brands fa-python {_fa_move}",
    },
    {
        "name": "PyPi package installation repository",
        "url": "https://pypi.org/",
        "icon": f"_static/logo-small.2a411bc6.svg",
        "type": "local",
    },
    {
        "name": "Conda documentation",
        "url": "https://docs.conda.io/en/latest/index.html",
        "icon": "_static/anaconda_logo.svg",
        "type": "local",
    },
]


html_theme_options = {
    "use_repository_button": True,
    "repository_provider": "github",
    "repository_url": "https://github.com/dtudk/pythonsupport-page",
    "use_edit_page_button": True,
    "use_fullscreen_button": True,
    "header_links_before_dropdown": 3,
    "navbar_align": "content",
    "navbar_center": ["navbar-nav"],
    "icon_links": _icon_links,
}

_course_json_url = "_static/course_switcher.json"
if False:
    html_theme_options["switcher"] = {
        "json_url": _course_json_url,
        "version_match": "courses",
    }
    html_theme_options["navbar_center"].append("version-switcher")

html_css_files = [
    "css/custom_styles.css",
]

html_context = {
    "github_user": "dtudk",
    "github_repo": "pythonsupport-page",
    "github_version": "main",
    "doc_path": "docs",
}


# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

# TODO add custom codes to make this false when releasing
# Some kind of env-variable
todo_include_todos = {
    "true": True, "T": True, "TRUE": True, "True": True, True: True,
    "false": False, "F": False, "FALSE": False, "False": False, False: False,
}.get(os.environ.get("PS_INCLUDE_TODOS", True))


# Spell checking
spelling_lang = 'en_US'
tokenizer_lang = 'en_US'


# Automatically call the switcher creator
def course_switcher(out=_course_json_url):
    """ Create a course switcher based on the available courses

    This small snippet will automatically search the directories in:
    `courses/` and add any course to the file
    """
    from pathlib import Path
    import json

    # current path
    cwd = Path(__file__).parent

    # Now search directories in the /courses folder

    courses = cwd / "courses"

    data = [{
        "name": "courses",
        "version": "courses",
        "url": f"pathto(courses/index.html, 1)",
        "preferred": True,
    }]

    for course in courses.glob("*"):
        if not course.is_dir():
            continue # only search directories

        if not (course / "index.rst").exists():
            continue # not a valid course

        data.append({
            "name": course.name,
            "version": course.name,
            "url": f"pathto(courses/{course.name}/index.rst, 1)",
        })

    json.dump(data, open(out, 'w'), indent=4)

course_switcher()
