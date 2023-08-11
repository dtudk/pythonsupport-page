# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DTU Python support'
copyright = '2023, DTU Python support developers'
author = 'DTU Python support developers'

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

.. todo::
    check links

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

.. _dtu-courses: https://kurser.dtu.dk/
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

_icon_links = [
    {
        "name": "Discord",
        "url": _discord_invite,
        "icon": "_static/discord_blurple_CMYK.png",
        "type": "local",
    },
]

html_theme_options = {
    "use_repository_button": True,
    "repository_provider": "github",
    "repository_url": "https://github.com/dtudk/pythonsupport-webpage",
    "use_edit_page_button": True,
    "use_fullscreen_button": True,
    "header_links_before_dropdown": 4,
    "navbar_align": "left",
    "navbar_center": ["navbar-nav"],
    "icon_links": _icon_links,
}

html_css_files = [
    "css/custom_styles.css",
]

html_context = {
    "github_user": "dtudk",
    "github_repo": "python-support-page",
    "github_version": "main",
    "doc_path": "docs",
}

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True
