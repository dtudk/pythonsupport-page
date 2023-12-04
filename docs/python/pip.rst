
.. _pip:

`pip <pypi-org_>`__ {{ pref_symbol }}
=========================================

.. button-link:: https://www.google.com/search?q=cheatsheet+python+pip
   :color: {{ cheatsheet_color }}
   :align: right
   :tooltip: Search google for cheatsheet

   Find a pip cheatsheet {{ cheatsheet_icon }}

.. note::

   ``pip`` is shipped with pretty much *all* Python installations (also :ref:`conda <conda>`).
   As such one can use ``pip`` in both ``conda`` and pure Python installations.

   See :ref:`here <install-python>` for installing Python.


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


.. _pip-installing:

Installing packages
-------------------

Packages can be installed in a very simple manner, note how multiple packages and associated requirements
can be specified in a single invocation of the program.

.. note::

   ``pip list`` will give you the current list of installed packages.

.. tab-set::

   .. tab-item:: {{ win_powershell }}
      :sync: powershell

      .. code-block:: powershell

         python -m pip install "numpy==1.24.*" "scipy<1.10" "matplotlib"

   .. tab-item:: {{ win_batch }}
      :sync: batch

      .. code-block:: winbatch

         python -m pip install "numpy==1.24.*" "scipy<1.10" "matplotlib"

   .. tab-item:: {{ mac_bash }}
      :sync: mac

      .. code-block:: bash

         python3 -m pip install "numpy==1.24.*" "scipy<1.10" "matplotlib"

   .. tab-item:: {{ linux_bash }}
      :sync: bash

      .. code-block:: bash

         python3 -m pip install "numpy==1.24.*" "scipy<1.10" "matplotlib"

The above will install:

.. note::
   :class: margin

   Use ``pip3 show numpy`` to get more detailed information about the ``numpy``
   package, such as directory where it is installed etc.

- `numpy`_ at the latest version in the 1.24 release cycle
- `scipy`_ at the latest version, but older than the 1.10
- `matplotlib`_ at the latest version

when specifying more than one package on the line, all dependencies will be checked
against each other at install time.

.. note::
   
   You will quite often encounter some warnings or notices from ``pip``,
   they look something like the following. It is perfectly normal, and
   it is not necessary to do what it says.

   ``pip`` versions 21 and older:

   .. image:: images/pip21_upgrade.png
      :width: 800
      :align: left
      :alt: pip upgrade notice from versions 21 and older
   
   ``pip`` versions 22 and newer:

   .. image:: images/pip22_upgrade.png
      :width: 550
      :align: left
      :alt: pip upgrade notice from versions 22 and newer



.. _pip-requirements:

Requirements file
^^^^^^^^^^^^^^^^^

Many Python tutorials will share a *so called* ``requirements.txt`` file which contains
lines packages. For instance to replicate the installation shown in :ref`pip-installing`, one could create a file (called ``requirements.txt``):

.. code-block::

   numpy==1.24.*
   scipy,1.10
   matplotlib

Basically it contains the equivalent of many packages on the same line, see :ref:`pip-installing`.

Installation using a ``requirements.txt`` file is simply specifying the file with ``-r`` flag:

.. tab-set::

   .. tab-item:: {{ win_powershell }}
      :sync: powershell

      .. code-block:: powershell

         python -m pip install -r requirements.txt

   .. tab-item:: {{ win_batch }}
      :sync: batch

      .. code-block:: winbatch

         python -m pip install -r requirements.txt

   .. tab-item:: {{ mac_bash }}
      :sync: mac

      .. code-block:: bash

         python3 -m pip install -r requirements.txt

   .. tab-item:: {{ linux_bash }}
      :sync: bash

      .. code-block:: bash

         python3 -m pip install -r requirements.txt


.. _pip-navigating:

Navigating packages
^^^^^^^^^^^^^^^^^^^

Quite often it is necessary to list and find extra information about the packages
that is installed.

Here is a set of commands that can be useful for interacting with the ``pip``
packages:


.. tab-set::

   .. tab-item:: {{ win_powershell }}
      :sync: powershell

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

   .. tab-item:: {{ win_batch }}
      :sync: batch

      .. code-block:: winbatch

         # List the packages installed
         python -m pip list

         # Show additional information about a single package
         python -m pip show numpy

         # Create a *fixed* file with the exact numbers in a requirement.txt
         # compatible file format.
         # In this command we will create a file called 'requirements.txt'
         # as the command 'pipes' the output into that file
         python -m pip freeze > requirements.txt

   .. tab-item:: {{ mac_bash }}
      :sync: mac

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

   .. tab-item:: {{ linux_bash }}
      :sync: bash

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


.. _pip-dependencies:

Dependencies and conflicts
^^^^^^^^^^^^^^^^^^^^^^^^^^

Installing packages over the course of several months. During this time, new releases
and new dependency requirements of each package arise.

.. tip::

   Always prefer to use :ref:`virtual environments <python-environments>`
   to reduce package conflicts.

Below is a constructed example of a dependency conflict arising.

.. tab-set::

   .. tab-item:: {{ win_powershell }}
      :sync: powershell

      .. code-block:: powershell

         $> python -m pip install dtumathtools==1.0.1
         ... lots of output
         $> python -m pip install --upgrade numpy
         ... lots of output ... then
         dtumathtools 1.0.1 requires numpy<1.24,>=1.21.1, but you have numpy 1.25.2 which is incompatible.

   .. tab-item:: {{ win_batch }}
      :sync: batch

      .. code-block:: winbatch

         $> python -m pip install dtumathtools==1.0.1
         ... lots of output
         $> python -m pip install --upgrade numpy
         ... lots of output ... then
         dtumathtools 1.0.1 requires numpy<1.24,>=1.21.1, but you have numpy 1.25.2 which is incompatible.

   .. tab-item:: {{ mac_bash }}
      :sync: mac

      .. code-block:: bash

         $> python3 -m pip install dtumathtools==1.0.1
         ... lots of output
         $> python3 -m pip install --upgrade numpy
         ... lots of output ... then
         dtumathtools 1.0.1 requires numpy<1.24,>=1.21.1, but you have numpy 1.25.2 which is incompatible.

   .. tab-item:: {{ linux_bash }}
      :sync: bash

      .. code-block:: bash

         $> python3 -m pip install dtumathtools==1.0.1
         ... lots of output
         $> python3 -m pip install --upgrade numpy
         ... lots of output ... then
         dtumathtools 1.0.1 requires numpy<1.24,>=1.21.1, but you have numpy 1.25.2 which is incompatible.

The first command finalized package installation obeying all requirements between the installed
packages (``dtumathtools`` depends on many other packages which will also be installed).

The second command will also succeed, however, at the end a warning will be printed.
This tells us that the package ``dtumathtools`` installed is version ``1.0.1`` and that it requires
a ``numpy`` version in the range ``1.21.1<=numpy<1.24``. However, the upgrade installed ``numpy`` version
``1.25.2`` which is not in the requirement range. It still got installed regardless of the already installed
packages requirements! Sometimes this results in a broken installation and nothing works.

.. warning::

   ``pip`` only obeys package requirements for packages installed on the same installation command:

   .. code-block:: bash
   
      # this will install numpy and scipy in compatible versions
      ... pip install numpy scipy
      
      # this MAY install numpy and scipy in non-compatible versions
      ... pip install numpy
      ... pip install scipy

To check possible conflicts in the current environment do

.. tab-set::

   .. tab-item:: {{ win_powershell }}
      :sync: powershell

      .. code-block:: powershell

         python -m pip check

   .. tab-item:: {{ win_batch }}
      :sync: batch

      .. code-block:: winbatch

         python -m pip check

   .. tab-item:: {{ mac_bash }}
      :sync: mac

      .. code-block:: bash

         python3 -m pip check

   .. tab-item:: {{ linux_bash }}
      :sync: bash

      .. code-block:: bash
         
         python3 -m pip check


.. _pip-venv-env:

.. include:: environment-venv.rst.include

.. _pip-virtualenv-env:

.. include:: environment-virtualenv.rst.include
