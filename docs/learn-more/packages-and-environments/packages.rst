.. _installing-packages:

Packages
========

.. include:: /_rst_includes/tip-copy.rst


Python packages are an integral part of Python programming. A package is a bundle 
of modules. Modules are individual Python files that contain code pieces that 
can be used in your projects, which makes them easier to program.
For example, you will often use 
the package `sympy` in your studies.
The `sympy` package is a collection of modules containing 
code for different mathematical operations.
The module `sympy.matrices` contain tools for 
working with matrices, or `sympy.calculus` includes operations for derivatives and integrals.

.. tip:: 
   It is important to ensure that you have activated the correct environment before proceeding.
   Please check the :doc:`environments` section, if you need to know what this means.


Conda is an open-source package management system that can install, run, and 
update packages and their dependencies in your Python development environment. We recommend is 
using Conda to manage your packages. If you followed our :doc:`installation guides </install/python>`, you already have Conda 
installed.

.. button-link:: https://www.google.com/search?q=cheatsheet+python+conda
   :color: {{ cheatsheet_color }}
   :align: right
   :tooltip: Search Google for cheatsheet

   Find a Conda cheatsheet {{ cheatsheet_icon }}

Installing packages
^^^^^^^^^^^^^^^^^^^

Packages can be installed to your specific environment by using ``conda install``:

.. tab-set::

   .. tab-item:: {{ win_powershell }}
      :sync: powershell

      .. code:: powershell

         conda install "numpy==1.24.*" "scipy<1.10" "matplotlib"

   .. tab-item:: {{ mac_bash }}
      :sync: mac

      .. code:: bash

         conda install "numpy==1.24.*" "scipy<1.10" "matplotlib"


The above command will install specific versions of the listed packages, which can be important for 
maintaining compatibility and stability in your environment. The above will install version 1.24 of 
Numpy, a Scipy version lower than 1.10, and the latest version of matplotlib.


Navigating packages
^^^^^^^^^^^^^^^^^^^

Quite often, it is necessary to list and find out if you already have a certain package and what package version you have.
Using the command ``conda list``, you can see all the packages that you have 
installed and their specific versions.

.. tab-set::

   .. tab-item:: {{ win_powershell }}
      :sync: powershell

      .. code:: powershell

         conda list


   .. tab-item:: {{ mac_bash }}
      :sync: mac

      .. code:: bash

         conda list


Updating packages
^^^^^^^^^^^^^^^^^

Packages can be updated by using ``conda update`` and specifying the package you wish to update:

.. tab-set::

   .. tab-item:: {{ win_powershell }}
      :sync: powershell

      .. code:: powershell

         conda update numpy

   .. tab-item:: {{ mac_bash }}
      :sync: mac

      .. code:: bash

         conda update numpy


The above command will update the numpy package to the most recent version that is compatible with your environment.

Removing packages
^^^^^^^^^^^^^^^^^

The command ``conda remove`` allows you to remove a specific package from your environment. It is useful 
when you no longer need a package or want to replace it with a different version.

.. tab-set::

   .. tab-item:: {{ win_powershell }}
      :sync: powershell

      .. code:: powershell

         conda remove numpy

   .. tab-item:: {{ mac_bash }}
      :sync: mac

      .. code:: bash

         conda remove numpy


The above command will remove the numpy package from your environment.

.. tip::
    Further documentation on packages and installation is available on
    `Conda's webpage <https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/packages.html>`__.

