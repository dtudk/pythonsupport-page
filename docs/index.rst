.. pythonsupport documentation master file, created by
   sphinx-quickstart on Mon Aug  7 12:41:08 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. meta::
   :description: Technical University of Denmark (DTU) Python Installation Support
   :keywords: dtu, dtudk, python, support, pip, conda, venv, virtualenv

.. todolist::


Python support
==============

-- Polytechnical Foundation courses
-----------------------------------

.. :img-top: _static/index_getting_started.svg
.. :img-top: _static/index_user_guide.svg

.. grid:: 1 1 2 2
    :gutter: 2

    .. grid-item-card:: Quick-start guide :fas:`person-running`
        :link: quickstart/index
        :link-type: doc

        New to Python @ DTU? Quickly get started with minimal guides.

    .. grid-item-card::  Courses :fas:`book-open`
        :link: courses/index
        :link-type: doc

        Find installation guides for specific courses.

    .. grid-item-card:: :fas:`envelope` -- :mail:`pythonsupport@dtu.dk` 
        :link: mailto:pythonsupport@dtu.dk
        :link-type: url

        | Contact us outside working hours.
        | Monday -- Thursday @ 18:00-22:00
   
    .. grid-item-card:: Discord :fab:`discord`
        :link: https://discord.gg/h8EVaV9ShP
        :link-type: url

        | Contact us outside working hours.
        | Monday -- Thursday @ 18:00-22:00


Welcome to the DTU student support unit!  
We are here to help students with Python installation problems related
to courses at DTU.
Our goal is to ensure that students can get a Python
environment up and running according to the needs of DTU courses.  
Help can be requested through various channels:

Office hours
   we will have physical presence at DTU Lyngby campus on differing locations
   depending on the used lecture rooms in the Polytechnical Foundation courses.
   Once these locations has been fixed, we will list the locations and opening hours
   for the semester. These opening hours will change *during* the semester. Please
   stay up to date on this page!
Discord - `channel <ps-discord-general_>`_ and `invite link <ps-discord-invite_>`_
   Our support team will also be present on the Discord chatting service.

   Using the Discord channel requires signing up to Discord's terms, DTU
   have no control over Discord and how they use your data. If you feel uncomfortable
   about signing up, please use the email or the physical meet-ups. Otherwise contact
   us for details if needed.


.. note::

   Currently we only support students with installation problems related
   to Python (it self) and packages required in specific courses.
   These course are the Polytechnical Foundation courses:
   
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
   need for supporting in a broader sense.


.. note::

   If you are a teacher, please visit :ref:`here <teacher-contact>` if you
   wish to post your course installation guidelines here.

.. todo::

   check that the drop down actually works, also look into css settings for
   making it look prettier

.. todo::

   what is a terminal, how to open, how to download, very basic things
   navigate a terminal.

.. todo::

   Create a Quickstart guide

   There is too much information for each of the steps
   It would be ideal with some kind of simple quickstart guide
   which references the sub-pages if there are problems.

   Add sphinx-panels


.. toctree::
   :maxdepth: 2
   :hidden:
   
   courses/index.rst

   python/install.rst

   python/environments.rst

   python/pip.rst
   python/conda.rst

   os/index.rst
   ides/index.rst

   src/about.rst
