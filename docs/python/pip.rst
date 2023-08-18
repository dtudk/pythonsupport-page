
.. _pip:

`pip <pypi-org_>`__
===================

.. note::

   ``pip`` is shipped with pretty much *all* Python installations (also :ref:`conda <conda>`).
   As such one can use ``pip`` in both ``conda`` and pure Python installations.

   See :ref:`here <install>` for installing Python.

.. todo::

   pip list | show | freeze

`pip <pypi-org_>`_ is the *de-facto* standard for installing and maintaining
packages/modules in a Python environment. Its `documentation <pip-org_>`_ is extensive.
Here some common tips and tricks will be listed.

.. tip::

   It is recommended to create virtual :ref:`python-environments`, for basically everything.
   Testing software installations using :ref:`python-environments` allows you to do
   everything in an area of the computer that does not interfere with the rest of the
   system.

`pip <pypi-org_>`_ will generally install packages without problems if one is in a clean
environment (read, *no prior installed packages*).
The longer time one uses `pip <pypi-org_>`_ in the same environment (virtual or not) the
larger the risk is of causing problems via corrupted dependencies.
This should not deter one from using `pip` at all, this is just to mention that doing updates
*on the fly* may not always be a good idea without testing in a separate environment.

.. contents::
   :local:
   :backlinks: none


Installing packages
-------------------

Packages can be installed in a very simple manner, note how multiple packages and associated requirements
can be specified in a single invocation of the program.

.. note::

   ``pip list`` will give you the current list of installed packages.

.. tab:: |win-powershell|

   .. code-block:: powershell

      python -m pip install "numpy==1.24.*" "scipy<1.10" "matplotlib"

.. tab:: |win-batch|

   .. code-block:: batch

      python -m pip install "numpy==1.24.*" "scipy<1.10" "matplotlib"

.. tab:: |macos-bash|

   .. code-block:: bash

      python3 -m pip install "numpy==1.24.*" "scipy<1.10" "matplotlib"

.. tab:: |linux-bash|

   .. code-block:: bash

      python3 -m pip install "numpy==1.24.*" "scipy<1.10" "matplotlib"

The above will install:

.. note::
   :class: margin

   Use ``pip show numpy`` to get more detailed information about the ``numpy``
   package, such as directory where it is installed etc.

- `numpy`_ at the latest version in the 1.24 release cycle
- `scipy`_ at the latest version, but older than the 1.10
- `matplotlib`_ at the latest version


when specifying more than one package on the line, all dependencies will be checked
against each other at install time.


Navigating packages
^^^^^^^^^^^^^^^^^^^

Quite often it is necessary to list and find extra information about the packages
that is installed.

Here is a set of commands that can be useful for interacting with the ``pip``
packages:


.. tab:: |win-powershell|

   .. code-block:: powershell

      # List the packages installed
      python -m pip list

      # Show additional information about a single package
      python -m pip show numpy

      # Create a *fixed* file with the exact numbers in a requirement.txt
      # compatible file format.
      # In this command we will create a file called 'requirements.txt'
      # as the command 'pipes' the output into that file
      python -m pip freeze > requirements.txt

.. tab:: |win-batch|

   .. code-block:: batch

      # List the packages installed
      python -m pip list

      # Show additional information about a single package
      python -m pip show numpy

      # Create a *fixed* file with the exact numbers in a requirement.txt
      # compatible file format.
      # In this command we will create a file called 'requirements.txt'
      # as the command 'pipes' the output into that file
      python -m pip freeze > requirements.txt

.. tab:: |macos-bash|

   .. code-block:: bash

      # List the packages installed
      python3 -m pip list

      # Show additional information about a single package
      python3 -m pip show numpy

      # Create a *fixed* file with the exact numbers in a requirement.txt
      # compatible file format.
      # In this command we will create a file called 'requirements.txt'
      # as the command 'pipes' the output into that file
      python3 -m pip freeze > requirements.txt

.. tab:: |linux-bash|

   .. code-block:: bash

      # List the packages installed
      python3 -m pip list

      # Show additional information about a single package
      python3 -m pip show numpy

      # Create a *fixed* file with the exact numbers in a requirement.txt
      # compatible file format.
      # In this command we will create a file called 'requirements.txt'
      # as the command 'pipes' the output into that file
      python3 -m pip freeze > requirements.txt



.. _pip-venv-env:

.. include:: environment-venv.rst.include

.. _pip-virtualenv-env:

.. include:: environment-virtualenv.rst.include
