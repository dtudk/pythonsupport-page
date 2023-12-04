:nosearch:

.. Ensure no search in this file

.. _internal-exercises:

Exercises
---------

These exercises are meant to prepare the DTU Python supporters for a variety
of things that they may encounter.

It also covers a bit more than what the courses expects, we need to be prepared
for a variety a things. 


.. note::

   These exercises are intended with low guidance, we strive
   to let our supporters be explorative, and that they ensure they
   know where to find information.

   As such, supporters should be able to find the information on-line
   if they encounter problems they have not experienced before. Or, use
   their peers to get a solution.
   So please use search engines for solving the problems.


Best practices
^^^^^^^^^^^^^^

After all steps of an installation/upgrade of packages it is important
to understand and ensure that the environment is behaving as expected.

There can be numerous paths to confirm this, here are some check-points
that can be useful:

- check the ``pip``/``conda`` list of packages and ensure that the package
  version and package is installed as requested.
- open up a Python shell and ensure it can be imported
- ensure the module's version *after* import is as requested.
  Most likely the module has a variable: ``<modulename>.__version__``
  which can be checked for current imported version.
- do the above points also in their editor to ensure that their editor
  does not launch in a virtual environment.

For instance, after having installed ``numpy==1.22`` one can check:

.. tab-set::

   .. tab-item:: {{ pip }}
      :sync: pip

      .. code-block:: bash

         pip list
         # or "grep"'ing for a specific package
         pip list | grep numpy

   .. tab-item:: {{ conda }}
      :sync: conda

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

As will be clear in :ref:`internal-exercise-4`, the above test is also important in the
IDE that the questioner is working with.

.. warning::

   Please always use a virtual environment (``pip``/``conda``) when performing these
   exercises. It ensures that you do not mess up your own installation.


.. contents::
   :depth: 1
   :backlinks: none
   :local:


.. _internal-exercise-1:

Exercise 1
^^^^^^^^^^

1. Install the :ref:`official Python <install-python>` distribution.

   **Windows only**: If your terminal will not recognize the ``python``
   executable, most likely your forgot to check the ``Add ... to PATH``.
   It might be a good idea if you also try and install Python like this (forcefully)
   to know how the error message looks.

2. Install :ref:`conda <install-conda>` in its minimal installation (MiniConda).

   In the semester 2023; the recommended usage will be ``pip``.
   Likely there will be some students with a prior ``conda`` installation.
   It is thus important that you know how to have a ``conda`` installation
   *and* navigate a regular Python installation.
   
   Create a `new environment <https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment>`_ in a local folder.

   Understand that:

   1. Environments created in local folders are not automatically listed when listing available environments
   2. How to activate a local environment.
   3. How to install packages into a local environment

      a. Packages can be installed from an *external* command, such as ``conda install -n <path to environment> <packages>``,
      b. Packages will be installed directly if the environment is already the activated one: ``conda activate <path to environment>``

  
   4. How can you see if you are in a ``conda`` environment? 
   
   5. Ensure you can navigate between both the ``conda`` and the official Python installation.


.. hint::

   The command ``python -c "import sys ; print(sys.exec_prefix)"`` can give a hint at
   which Python interpreter is being used.


.. _internal-exercise-2:

Exercise 2
^^^^^^^^^^

Create two virtual environments, using `venv <https://docs.python.org/3/library/venv.html>`__.

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

.. note::

   If you have gone through all exercises, then do this again with ``conda``!


.. _internal-exercise-3:

Exercise 3
^^^^^^^^^^

Install any package, and figure out its location in the file-system. It is important you check against an *importable*
package.


.. hint::

   - ``__file__``
   - ``pip``


.. _internal-exercise-4:

Exercise 4
^^^^^^^^^^

For the currently known recommend IDE's:

*In order of priority, if time is limited, only do the first*.

- :ref:`VS Code <ide-vscode>` (please also read the page linked for some additional information)
- :ref:`Spyder <ide-spyder>`
- :ref:`PyCharm <ide-pycharm>`

Figure out the following:

1. How to swap environment (interpreter) in the IDE instead of the default Python executable
2. How to check the packages that are installed (some IDE's allows calling Pip directly
   in the ``IPython`` console)


.. _internal-exercise-5:

Exercise 5
^^^^^^^^^^

Run through the :course-home:`02002` installation instructions.
Then run through these extra steps: :full-link:`https://lab.compute.dtu.dk/cp/02002students/-/wikis/testing`

It would also be great to test some of these things in a Jupyter Notebook, to see how well they fare in
a more constrained environment.


.. _internal-exercise-6:

Exercise 6
^^^^^^^^^^

Go to :ref:`pip dependencies <pip-dependencies>` and provoke the output
shown, in a virtual environment. Understand all output of the commands, especially the warnings and errors.
Use ``pip check`` as well.

Also resolve the ``pip check`` errors.


.. _internal-exercise-7:

Exercise 7 (not necessary)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Complete :ref:`exercise 2 <internal-exercise-2>` using `virtualenv <env-virtualenv_>`_
which works slightly different from ``venv``.


.. _internal-exercise-8:

Exercise 8 (not necessary)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Install the package `pyparsing <https://github.com/pyparsing/pyparsing>`_ at a specific Git commit ``c8b7664`` using ``pip``.

