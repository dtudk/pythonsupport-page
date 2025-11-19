.. _pip:

pip
===

.. button-link:: https://www.google.com/search?q=cheatsheet+python+pip
   :color: {{ cheatsheet_color }}
   :align: right
   :tooltip: Search Google for cheatsheet

   Find a pip cheatsheet {{ cheatsheet_icon }}

.. include:: /_rst_includes/tip-copy.rst

Although we recommend using Conda for managing packages and environments due to 
its comprehensive features and dependency management, `pip <pypi-org_>`_ remains a valuable 
tool, especially when certain packages are not yet available or up-to-date in Conda.

`pip <pypi-org_>`_ is the *de-facto* standard tool for installing, upgrading, and maintaining
Python packages. It simplifies the management of package dependencies and supports installation 
in global or virtual environments. ``pip`` also handles package versioning 
to prevent compatibility issues. As a fundamental tool for any Python developer, ``pip`` is essentially 
a tool for managing your Python packages.
It also has extensive `documentation <pip-org_>`_. 

``pip`` comes with most Python installations, including Conda.
This means you can use ``pip`` in both Conda and standard Python installations and environments.
For installing Python first, see :ref:`here <install-python>`.

Below are some common tips and tricks about pip:

.. tip::

   It is recommended that you create virtual environments for your projects.
   Environments allow you to  manage installations without interfering with your main
   system.
   If you do not know what an environment is, please check the 
   description in the :ref:`environments <learn-more-environments>` section.

Using `pip <pypi-org_>`_ in a clean environment (meaning *no prior installed packages*) typically avoids installation issues. However, 
the risk of dependency conflicts increases with prolonged use of the same environment.
Testing updates in a separate environment before applying them broadly is a good idea.


.. _pip-installing:

Installing packages
-------------------

You can install packages with `pip`. List them during a single ``pip`` command
to install multiple packages at once.

.. note::

   Use ``pip list`` to view currently installed packages.

.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      .. code-block:: powershell

         python -m pip install "numpy==1.24.*" "scipy<1.10" "matplotlib"

   .. tab-item:: {{ macos }}
      :sync: mac

      .. code-block:: bash

         python3 -m pip install "numpy==1.24.*" "scipy<1.10" "matplotlib"

The command will install:

.. note::
   :class: margin

   Use ``pip3 show numpy`` to get more detailed information about the ``numpy``
   package, such as the directory where it is installed, etc.

- `numpy`_ at the latest version within the 1.24 release cycle
- `scipy`_ at the latest version, but older than the 1.10
- `matplotlib`_ at the latest version

When specifying more than one package on the line, dependencies will be checked during the installation to prevent conflicts.

.. note::
   
   You will often encounter some warnings or notices from ``pip``;
   they look like the following.
   It is perfectly normal, and
   unnecessary to do what it says.

   ``pip`` versions 21 and older:

   .. image:: /images/pip/pip21_upgrade.png
      :width: 800
      :align: left
      :alt: pip upgrade notice from versions 21 and older
   
   ``pip`` versions 22 and newer:

   .. image:: /images/pip/pip22_upgrade.png
      :width: 550
      :align: left
      :alt: pip upgrade notice from versions 22 and newer



.. _pip-requirements:

Requirements file
^^^^^^^^^^^^^^^^^

A ``requirements.txt`` file is often used to replicate an environment. Many Python tutorials will share a ``requirements.txt`` file containing
lines of packages. For instance, to replicate the example installation shown in :ref:`pip-installing`, one could create a file called ``requirements.txt``:

.. code-block::

   numpy==1.24.*
   scipy,1.10
   matplotlib

The file contains the equivalent versions of the packages in the :ref:`pip-installing` section. 
It is easier to do the installations with the help of a ``requirements.txt`` file when there are 
too many packages to install simultaneously, as it helps us to not do the installations with a 
single command on the same line or not to run the installation command multiple times.

To install using ``requirements.txt``, use the ``-r`` flag:

.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      .. code-block:: powershell

         python -m pip install -r requirements.txt

   .. tab-item:: {{ macos }}
      :sync: mac

      .. code-block:: bash

         python3 -m pip install -r requirements.txt


.. _pip-navigating:

Navigating and managing packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Listing and finding extra information on the installed packages is sometimes necessary.
Below is a set of commands that can be useful for interacting with the ``pip``
packages. To list, show, or freeze the state of installed packages, use the following commands:

.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

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

   .. tab-item:: {{ macos }}
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


.. _pip-dependencies:

Dependencies and conflicts
^^^^^^^^^^^^^^^^^^^^^^^^^^

Over time, installing packages can lead to dependency conflicts as new releases
and new dependency requirements of each package may arise. 

Below is a constructed example of a dependency conflict arising.

.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      .. code-block:: powershell

         $> python -m pip install dtumathtools==1.0.1
         ... lots of output
         $> python -m pip install --upgrade numpy
         ... lots of output ... then
         dtumathtools 1.0.1 requires numpy<1.24,>=1.21.1, but you have numpy 1.25.2 which is incompatible.

   .. tab-item:: {{ macos }}
      :sync: mac

      .. code-block:: bash

         $> python3 -m pip install dtumathtools==1.0.1
         ... lots of output
         $> python3 -m pip install --upgrade numpy
         ... lots of output ... then
         dtumathtools 1.0.1 requires numpy<1.24,>=1.21.1, but you have numpy 1.25.2 which is incompatible.

.. tip::

   Always prefer to use :ref:`environments <learn-more-environments>`
   to reduce package conflicts.

The first command completes installing the ``dtumathtools`` package 
while ensuring compliance with all the required dependencies, including 
other related packages that gets installed.

The second command successfully executes and upgrades ``numpy`` to version 
``1.25.2``. However, upon completion, a warning is issued indicating a potential 
issue. Although ``dtumathtools`` version ``1.0.1`` is installed and operational, it 
requires explicitly ``numpy`` to be within the version range of ``1.21.1<=numpy<1.24``. 
The newly installed ``numpy`` version ``1.25.2`` exceeds this required range, creating a 
version conflict. This conflict can lead to a malfunctioning or broken installation, 
as the requirements of some of the already installed packages (i.e., ``dtumathtools``) 
are not satisfied.

.. warning::

   ``pip`` only obeys package requirements for packages installed on the same installation command:

   .. code-block:: bash
   
      # this will install numpy and scipy in compatible versions
      ... pip install numpy scipy
      
      # this may install numpy and scipy in non-compatible versions
      ... pip install numpy
      ... pip install scipy

To check possible conflicts in the current environment, use ``pip check``:

.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      .. code-block:: powershell

         python -m pip check

   .. tab-item:: {{ macos }}
      :sync: mac

      .. code-block:: bash

         python3 -m pip check

.. tip::

   Further documentation on ``pip`` is available `here <pip-org_>`_.

