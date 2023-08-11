
.. _install-pip:

pip
===

`pip <pypi-org_>`_ is the *de-facto* standard for installing and maintaining
packages/modules in a Python environment. Its `documentation <pip_>`_ is extensive.
Here some common tips and tricks will be listed.

.. note::

   It is recommended to create virtual :ref:`environments`, for basically everything.
   When testing software installations using :ref:`environments` allows you to do
   everything in an area of the computer that does not interfere with the rest of the
   system.

`pip <pypi-org_>`_ will generally install packages without problems if one is in a clean
environment (read, *no prior installed packages*).
The longer time one uses `pip <pypi-org_>`_ in the same environment (virtual or not) the
larger the risc is of causing problems via corrupted dependencies.
This should not deter one from using `pip` at all, this is just to mention that doing updates
*on the fly* may not always be a good idea without testing in a separate environment.

.. contents::
   :local:
   :backlinks: none


Installing packages
-------------------

Packages can be installed in a very simple manner, note how multiple packages and associated requirements
can be specified in a single invocation of the program.

.. tabs::

   .. group-tab:: Windows

      .. code-block:: powershell

         python -m pip install "numpy==1.24.*" "scipy<1.10" "matplotlib"

   .. group-tab:: MacOS

      .. code-block:: bash

         python3 -m pip install "numpy==1.24.*" "scipy<1.10" "matplotlib"

   .. group-tab:: Linux

      .. code-block:: bash

         python3 -m pip install "numpy==1.24.*" "scipy<1.10" "matplotlib"

The above will install:

- `numpy`_ at the latest version in the 1.24 release cycle
- `scipy`_ at the latest version, but older than the 1.10
- `matplotlib`_ at the latest version

when specifying more than one package on the line, all dependencies will be 

.. toctree::
   :maxdepth: 2

   venv.rst
   virtualenv.rst
