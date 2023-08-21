:nosearch:

.. Ensure no search in this file

.. _internal-exercises:

Exercises
---------

These exercises are meant to prepare the DTU Python supporters for a variety
of things that they may encounter from students.

It also covers a bit more of what the courses expects, we need to be prepared
for a variety a things. 


.. note::

   These exercises are intended with low guidance, we strive
   to let our supporters be explorative, and that they ensure they
   know where to find information.

   As such, supporters should be able to find the information on-line
   if they encounter problems they have not experienced before. Or use
   their peers to get the same information.
   So please use search engines for solving the problems.


Interacting with students
^^^^^^^^^^^^^^^^^^^^^^^^^

Students will arrive with a variety of backgrounds. Some are very interested
in programming, while others are not interested, *at all*, in the inner workings
of Python and simply want to be able to attend courses.

Our goal is to support both ends of the student spectrum.
Information overload can be a problem for new students as there is already
enough on the plate. It is imperative that information is given at the level
of the student and at the pace that might be interesting for the student.
Always ask if they want more information, before recommending best practices for
something they do not really care for.


Discord
^^^^^^^

Our Discord channels can be found `here <ps-discord-general_>`.
Once you have joined, ping ``@nicpa`` and ask for supporter role.

We have a separate category where the students (and others) cannot see
anything. Here you can share experiences, or consult your colleagues.

If we need additional channels, we discuss it there!


Best practices
^^^^^^^^^^^^^^

After all steps of an installation/upgrade of packages it is important
to understand and ensure that the environment is behaving as expected.

There can be numerous paths to confirm this, here are some check-points
that can be useful:

- check the ``conda``/``pip`` list of packages and ensure that the package
  version and package is installed as requested.
- open up a Python shell and ensure it can be imported
- ensure the module's version *after* import is as requested.
  Most likely the module has a variable: ``<modulename>.__version__``
  which can be checked for current imported version.
- do the above points also in their editor to ensure that their editor
  does not launch in a virtual environment.

For instance, after having installed ``numpy==1.22`` one can check:

.. tab:: {{ pip }}

   .. code-block:: bash

      pip list
      # or "grep"'ing for a specific package
      pip list | grep numpy

.. tab:: {{ conda }}

   .. code-block:: bash

      conda list
      # or "grep"'ing for a specific package
      conda list | grep numpy

Once the package is listed in the package list, check version and
import:

.. code-block:: bash

   python3 -c "import numpy ; print(numpy.__version__)

this will fail with errors if it can not import it, and if it succeeds, it will
print the version, if the variable (``__version__``) is part of the package.

.. warning::

   Please always use a virtual environment (``pip``/``conda``) when performing these
   exercises. It ensures that you do not mess up your own installation.


.. contents::
   :depth: 1
   :backlinks: none
   :local:


.. _internal-exercise-1:

Exercise 1a
^^^^^^^^^^^

Install :ref:`conda <install-conda>` in its minimal installation (MiniConda).

Create a `new environment <https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment>`_ in a local folder.

Understand that:

1. Environments created in local folders are not automatically listed when listing available environments
2. How to activate a local environment.
3. How to install packages into a local environment

   a. Packages can be installed from an *external* command, such as ``conda install -n <path to environment> <packages>``,
   b. Packages will be installed directly if the environment is already the activated one: ``conda activate <path to environment>``

In the semester 2023; the student primary usage will be ``pip``.
Undoubtedly there will be some students with a prior ``conda`` installation.
It is thus important that you know how to have a ``conda`` installation *and* navigate a regular Python installation.


Exercise 1b
^^^^^^^^^^^

Install the :ref:`official Python <install-python>` distribution.

Ensure you can navigate both the ``conda`` and the official Python installation.


.. _internal-exercise-2:

Exercise 2
^^^^^^^^^^

Create two virtual environments, using `venv <https://docs.python.org/3/library/venv.html>`_ and ``conda``.

.. code-block:: bash

   # first environment
   numpy=1.24
   matplotlib=3.6

   # second environment
   numpy=1.23
   matplotlib=3.6


Check that you can easily swap between these two environments.


.. note::

   One cannot copy paste the above in ``pip``, ensure you change the package specification
   to match the package installers terminology.


.. _internal-exercise-3:

Exercise 3
^^^^^^^^^^

Install the package `pyparsing <https://github.com/pyparsing/pyparsing>`_ at a specific Git commit ``c8b7664`` using ``pip``.


.. _internal-exercise-4:

Exercise 4
^^^^^^^^^^

Install any package, and figure out its location in the file-system. It is important you check against an *importable*
package.

Hints:

- ``__file__``
- ``pip``


.. _internal-exercise-5:

Exercise 5
^^^^^^^^^^

Complete :ref:`exercise 2 <internal-exercise-2>` using `virtualenv <env-virtualenv_>`_
which works slightly different from ``venv``.


.. _internal-exercise-6:

Exercise 6
^^^^^^^^^^

For all the currently known recommend IDE's:

- :ref:`VSCode <ide-vscode>`
- :ref:`PyCharm <ide-pycharm>`
- :ref:`Spyder <ide-spyder>`

Figure out the following:

1. How to swap environment (interpreter) in the IDE instead of the default Python executable
2. How to check the packages that are installed (some IDE's allows calling Pip directly
   in the ``IPython`` shell)


.. _internal-exercise-7:

Exercise 7
^^^^^^^^^^

Run through the :course-home:`02002` installation instructions.
