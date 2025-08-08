Export Environment Tutorial
===========================

This guide will explain how to create an `.yml` to share with students.
By creating these environments with the correct metadata students will
be able to automatically install all course requirements from this website.


1. Create Environment
---------------------

In your favorite text editor create the file environment file `{course_number}_{year}_{os}.yml`.
If there are no requirements that depend on the operating system then `_{os}` can be dropped.

For `conda` to install the correct dependencies use the following template:

.. code-block:: yaml

    metadata:
      course_full_name: "xxxxx Course name"
      course_number: "xxxxx"
      course_year: "2026"
      course_semester: "Spring"

    name: "xxxxx_S26" or "xxxxx_E26"
    channels:
      - conda-forge
    dependencies:
      - ipykernel
      - numpy=2.2.0
      - python=3.13.4
      - pip
      - pip:
        - matplotlib

Here ``conda-forge`` requirements go into ``dependencies:``, while ``pip`` requirements should be listed
as a subentry ``pip:``.

.. tip::

   Consider adding ``ipykernel`` or ``jupyter`` to the dependencies if you expect the students to work in Jupyter notebooks.

.. important::
    There may be licensing issues with packages installed from the default Anaconda channels.
    It is encouraged to use *free software* such as those supplied through ``conda-forge``.

    See details `here <rec-conda>`.

.. note::
    If you already have a conda environment that satisfies the licensing requirements, then a `.yml` file can be exported with the following command:

    .. code-block:: bash

        conda env export --from-history --no-builds --name {course_number}_{year} | grep -v "^prefix:" > {course_number}_{year}_{os}.yml

    Then add course metadata to the top of the file using the template above.


2. Verification
---------------

It is important to verify that that the newly created ``environment.yml`` file creates the correct environment.
In order to create a testing environment, use the following command:

.. code-block:: bash

   conda create -f {course_number}_{year}.yml -n testing_{course_number}_{year}_{os}

Activate the testing environment with:

.. code-block:: bash

   conda activate testing_{course_number}_{year}_{os}

Create a testing script that imports all of the packages required by the course.
This script could also be shared with students to allow them to verify that their
installation fulfills the course requirements.


3. Upload To Python Support
---------------------------

In order for DTU Pythonsupport to provide guides and support for the course please
send the environment file and verification script to :mailto:`pythonsupport@dtu.dk`.

When we have verified the installation process, the course will be listed on the :ref:`environments list <environments-list>`.


