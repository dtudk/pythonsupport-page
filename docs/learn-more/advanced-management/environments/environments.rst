
.. _python-environments:

Environments
============

Python environments are isolated spaces where you can manage separate sets of packages for different projects. 
This helps avoid conflicts that arise when different projects require different versions of the 
same package. For example, one project might need require ``numpy==1.23``, while another may require ``numpy==1.25``. If these versions 
are not compatible, switching back and forth between them for different 
projects can become quite annoying. Instead of reinstalling the correct version each time you switch projects, 
it is possible to use environments which allows you to keep fully functional and separate
package lists and easily swap between them.

Python environments allow you to maintain separate sets of packages, making it easy to switch between 
completely different configurations without conflict. Using environments can be used for a variety of things:

1. Quickly testing whether certain packages conflicts
2. Checking whether a developed Python script is compatible with different package versions
3. Ensuring a minimal package list (no unused packages)
4. Maintaining multiple functional package environments

It is recommended to create a separate environment for each course or project to ensure 
that their requirements do not interfere with each other.

.. _python-environments-venv-env:

.. include:: /menu/documentation/environments/environment-venv.rst.include

.. _python-environments-virtualenv-env:

.. include:: /menu/documentation/environments/environment-virtualenv.rst.include

.. _python-environments-conda-env:

.. include:: /menu/documentation/environments/environment-conda.rst.include


.. _python-environments-jupyter:

Jupyter Notebooks / IPython
---------------------------

Jupyter Notebooks and IPython are interactive computing environments that 
enable users to write and execute code in a notebook format. These notebooks 
can combine code, text, and visualizations. The usage of Jupyter notebooks are 
common in many computing-related tasks of the courses at DTU.

Using Virtual Environments with Jupyter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Virtual environments and Jupyter can cause issues when Jupyter is installed in the
system (not in the virtual environment). The kernel is fixed to launch
the Python interpreter it got installed with. Kernel is a process that allows you to 
execute the code in your Jupyter notebook by providing the necessary Python languge support.

.. warning::

   This issue will arise in *any* virtual environment, including ``conda``.


The simplest way to check whether your Jupyter Notebook is using your virtual environment
is to execute the following code in a notebook cell:

.. code-block:: python

   import sys
   print(sys.exec_prefix)

If it shows the directory of your virtual environment, you are all 
set. If not, install the kernel runner in the virtual environment:


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

Replace <path to venv|conda-env> with the path to your virtual environment. 
The problem and the fix is described in greater detail
`here <https://ipython.readthedocs.io/en/stable/install/kernel_install.html>`__.
