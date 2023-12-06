
# Hacking in the documentation

Thanks for looking into hacking our documentation.
Its structure can be explained like this:

Non documentation directories:
  - **ps_modules**
    Contains custom Python codes used for various
    things.
    - create_timetable.py
      This will automatically create the timetable for
      the current year+semester.
      It gets information from the `ps_configuration.toml`
      through `conf.py` and then parses the information
      based on the current year and semester configuration
      noted in the configuration.

      **NOTE**: Every year the semester information
      should be updated.
    - dictformatter.py
      A small dictionary formatter that holds course information.
      This can be used in the RST directives, e.g. :course-home:.

Documentation:
  - **courses/**
    Contains course specific guidelines.
    If a new course needs to be added, please follow the `template` folder.
  - **faqs/**
    Contains faq entries for the most common problems.
  - **ides/**
    Documenting the different IDE's, VS Code, Spyder.
  - **internal/**
    Our internal site information. Not exposed to students or other
    visitors.
  - **os/**
    Operating system specific documentation.
  - **python/**
    Generic python information, and pip/conda etc.
  - **quickstart/**
    Our quickstart page, this should be a trimmed down version
    of everything needed for a new student.
  - **timetable/**
    The specific timetables that will be updated as we run them through.

## Howto documentation using RST



