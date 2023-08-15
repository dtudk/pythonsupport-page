
.. _install-pip:

`pip <pypi-org_>`_
==================

.. todo::

   pip list | show | freeze

`pip <pypi-org_>`_ is the *de-facto* standard for installing and maintaining
packages/modules in a Python environment. Its `documentation <pip_>`_ is extensive.
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
   :class: margin

   ``pip list`` will give you the current list of installed packages.

.. tabs::

   .. group-tab:: |win-powershell|

      .. code-block:: powershell

         python -m pip install "numpy==1.24.*" "scipy<1.10" "matplotlib"
   
   .. group-tab:: |win-batch|

      .. code-block:: batch

         python -m pip install "numpy==1.24.*" "scipy<1.10" "matplotlib"

   .. group-tab:: |macos-bash|

      .. code-block:: bash

         python3 -m pip install "numpy==1.24.*" "scipy<1.10" "matplotlib"

   .. group-tab:: |linux-bash|

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


.. _install-venv-env:

.. include:: environment-venv.rst.include

.. _install-virtualenv-env:

.. include:: environment-virtualenv.rst.include
