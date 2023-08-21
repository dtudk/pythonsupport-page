.. pythonsupport documentation master file, created by
   sphinx-quickstart on Mon Aug  7 12:41:08 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. meta::
   :description: Technical University of Denmark (DTU) Python Installation Support
   :keywords: dtudk, dtu, support, python, pip, conda, venv, virtualenv

.. todolist::


DTU Python support
==================

-- Polytechnical Foundation courses
-----------------------------------

.. grid:: 1 1 2 2
    :gutter: 2

    .. grid-item-card:: :fas:`person-running` -- Quick-start guide
        :link: quickstart/index
        :link-type: doc

        New to Python @ DTU? Quickly get started.

    .. grid-item-card::  :fas:`book-open` -- Courses
        :link: courses/index
        :link-type: doc

        Course specific installation guides

    .. grid-item-card:: :fas:`envelope` -- pythonsupport@dtu.dk 
        :link: mailto:pythonsupport@dtu.dk
        :link-type: url

        | Contact us outside working hours.
        | Monday -- Thursday in the evening
   
    .. grid-item-card:: :fab:`discord` -- Discord
        :link: https://discord.gg/h8EVaV9ShP
        :link-type: url

        | Contact us outside working hours.
        | Monday -- Thursday in the evening


Welcome to the DTU student support unit!  
We are here to help with Python installation problems related
to courses at DTU.

When encountering the icon {{ pref_symbol }} you are using the
recommended DTU Python installation procedure.

Our goal is to ensure that students can get a Python
environment up and running according to the needs of DTU courses.  
Help can be requested through various channels:

.. todo::

   Should these (below) be here? Or is the above enough?

Office hours
   we will have physical presence at DTU Lyngby campus on differing locations
   depending on the used lecture rooms in the Polytechnical Foundation courses.
   See further down for our locations during specific weeks of the semester.
   This page will be updated continuously.
Mail -- :mail:`pythonsupport@dtu.dk`
   Outside of office hours we can be contacted through emails. We strive to return
   answers as soon as possible, and will have someone ready to answer Monday through
   Thursday in the evening
Discord -- `channel <ps-discord-general_>`_ and `invite link <ps-discord-invite_>`_
   Our support team will also be present on the Discord chatting service.

   Using the Discord channel requires signing up to Discord's terms, DTU
   have no control over Discord and how they use your data. If you feel uncomfortable
   about signing up, please use the email or the physical meet-ups. Otherwise contact
   us for details if needed.

.. include:: /timetable/index.rst


.. note::

   Currently we only support installation problems related
   to Python (it self) and packages required in specific courses.
   These are the Polytechnical Foundation courses:
   
   - :course-base:`01001`, :course-base:`01002`, :course-base:`01003` and :course-base:`01004`
     Mathematics 1
   - :course-base:`02002` and :course-base:`02003`
     Computer Programming
   - :course-base:`02402`
     Statistics
   - :course-base:`10060`, :course-base:`10063` and :course-base:`10065`
     Physics
   - :course-base:`26020`, :course-base:`26021` and :course-base:`26022`
     Chemistry
   - :course-base:`27022`
     Bioengineering

   Many more will come! Our support unit is new, and we wish to figure
   out what the need is among our students, please do not hesitate
   to contact us regarding other courses, we will use it to understand the
   need for Python support at DTU.


.. toctree::
   :maxdepth: 2
   :hidden:

   quickstart/index.rst
   courses/index.rst

   python/install.rst


.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Everyday use
   
   python/environments.rst

   python/pip.rst
   python/conda.rst

   os/index.rst
   ides/index.rst

   src/about.rst
