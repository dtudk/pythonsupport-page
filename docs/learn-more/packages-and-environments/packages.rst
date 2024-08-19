Packages
========

.. include:: /_rst_includes/tip-copy.rst


Python packages are an integral part of programming in Python. A package is a bundle 
of modules. Modules are individual Python files that contain prewritten code pieces that 
can be used in your projects which makes it easier to program. As an example, you will use 
the package `sympy` quite often in your studies. `sympy` package is a collection of different modules which contain 
code for different mathematical operations. The module `sympy.matrices` contains tools for 
working with matrices, or `sympy.calculus` includes operations for derivatives and integrals.

.. tip:: 
    It is important to make sure that you have activated the correct environment before proceeding.
    If you do not know what this means, please check the Environments section.


Conda is an open-source package management system that can install, run, and 
update packages and their dependencies in your Python development environment. Our recommendation is 
using Conda to manage your packages. If you followed our installation guides, you already have Conda 
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

Quite often it is necessary to list and find out if you already have a certain package and see 
what package version you have. Using ``conda list`` you can see all the packages that you have 
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
    Further documentation is available on Conda's webpage on `packages <https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/packages.html>`__ and 
    `installation <https://docs.anaconda.com/working-with-conda/packages/install-packages/>`__.
