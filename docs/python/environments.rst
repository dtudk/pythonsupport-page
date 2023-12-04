
.. _python-environments:

Environments
============

It is often necessary to retain two different but fully functional
package specifications. Imagine having two courses ``A`` and ``B``.
One has the requirement of ``numpy==1.23`` while the other has ``numpy==1.25``.
In cases where these are incompatible, for instance an `API <https://en.wikipedia.org/wiki/API>`_
change, one would be required to change the installed packages when participating in
each course.

Instead, one can use *environments* which allows one to retain a fully functional
package list and easily swap between them.

.. note::

   Using environments can be used for a variety of things:

   1. quickly test whether certain packages conflicts
   2. check whether a developed Python script is compatible with
      different package versions.
   3. ensures a minimal package list (no unused packages)
   4. have multiple functional package environments

   It is our clear recommendation to create an environment for
   each course. In this way you will ensure that anything you do
   in that course environment will not interfere with your other
   course environments.

.. contents::
   :depth: 2
   :backlinks: none
   :local:

.. include:: /python/environment-venv.rst.include 
.. include:: /python/environment-conda.rst.include 
.. include:: /python/environment-virtualenv.rst.include 


.. _python-environments-jupyter:

Jupyter Notebooks / IPython
---------------------------


Virtual environments and Jupyter can cause issues when Jupyter is installed in the
system (not in the virtual environment). This is because the kernel is fixed to launch
the Python interpreter it got installed with.

.. warning::

   This issue will arise in *any* virtual environment, including ``conda``.


The simplest way to check whether your Jupyter Notebook is using your virtual environment
is to execute the following code in a notebook cell:

.. code-block:: python

   import sys
   print(sys.exec_prefix)

if it shows a directory where you have your virtual environment, you are all set!
If not, then the simplest solution would be to install the kernel runner
in the virtual environment:


.. tab-set::

   .. tab-item:: {{ win_powershell }}
      :sync: powershell

      .. code-block:: powershell

         python -m ipykernel install --prefix <path to venv|conda-env>

   .. tab-item:: {{ win_batch }}
      :sync: batch

      .. code-block:: winbatch
         
         python -m ipykernel install --prefix <path to venv|conda-env>

   .. tab-item:: {{ mac_bash }}
      :sync: mac

      .. code-block:: bash

         python3 -m ipykernel install --prefix <path to venv|conda-env>

   .. tab-item:: {{ linux_bash }}
      :sync: bash

      .. code-block:: bash

         python3 -m ipykernel install --prefix <path to venv|conda-env>

Only insert the folder name in the ``< ... >`` block.
The problem, and fix, is described in greater detail
`here <https://ipython.readthedocs.io/en/stable/install/kernel_install.html>`__.
