Export Environment Tutorial
===========================

This guide will explain how to create an .yml to share with students.
By creating these environments with the correct metadata students will
be able to automatically install all course requirements from this website.

1. Create Environment
---------------------
In your favorite text editor create the file environment file "{course_number}_{year}_{os}.yml". If there are no requirements that depend on the operating system then "_{os}" can be dropped.
For conda to install the correct dependencies use the following template:

.. code:: yml

    metadata:
      course_full_name: "0xxxx Course name"
      course_number: "0xxxx"
      course_identifier: "Spring 2026"
      course_env_name: "0xxxx_S26" or "0xxxx_E26"
    name: "0xxxx_S26" or "0xxxx_E26"
    channels:
      - conda-forge
    dependencies:
      - numpy=2.2.0
      - python=3.13.4
      - pip
      - pip:
        - matplotlib

Here conda-forge requirements go into "dependencies:", while pip requirements go into "pip:".

.. important::
    Due to licensing problems we are not allowed to use packages from the default anaconda channel. 
    Instead use packages from `conda forge <https://conda-forge.org>`_.

.. note::
    If you already have a conda environment that satisfies the licensing requirements, then a .yml file can be exported with the following command:

    .. code:: bash

        conda env export --from-history --no-builds --name {course_number}_{year} | grep -v "^prefix:" > {course_number}_{year}_{os}.yml
    
    Then add course metadata to the top of the file using the template above.

2. Verification
---------------

It is very important to verify that that this environment.yml file creates the correct environment.
In order to create a testing environment, use the following command:

.. code:: bash

  conda create -f "{course_number}_{year}.yml" -n "testing_{course_number}_{year}_{os}"

Activate the testing environment with:

.. code:: bash

  conda activate "testing_{course_number}_{year}_{os}"

Create a testing script that imports all of the packages required by the course.
This script could also be shared with students to allow them to verify that their
installation fulfills the course requirements.

3. Upload To Python Support
---------------------------

In order for DTU pythonsupport to provide guides and support for the course please
send the environment file and verification script to :mail:`pythonsupport@dtu.dk`.

When we have verified the installation process, the course will be listed on the :ref:`environments list <environments-list>`.


