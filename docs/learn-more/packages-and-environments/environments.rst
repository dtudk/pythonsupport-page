.. _learn-more-environments:

Environments
============

.. include:: /_rst_includes/tip-copy.rst

Python environments are isolated spaces where you can manage separate sets of packages for different projects. 
This helps avoid conflicts  when different projects require different versions of the 
same package. For example, one project might require ``numpy==1.23``, while another may require ``numpy==1.25``. If these versions 
are incompatible, switching back and forth between them for different 
projects can become quite annoying. Instead of reinstalling the correct version each time you switch projects, 
you can use environments that allow you to keep fully functional and separate
package lists and swap between them.

.. tip:: 
    If you need to know what packages are, please check :doc:`here <packages>`.

Python environments allow you to maintain separate sets of packages, making switching
between configurations without conflicts.
Using environments can be used for a variety of things:

1. Quickly testing whether certain packages conflicts
2. Checking whether a developed Python script is compatible with different package versions
3. Ensuring a minimal package list (no unused packages)
4. Maintaining multiple functional package environments

It is recommended that each course or project be given a separate environment
to ensure that their requirements do not interfere.


Environment management with Conda
---------------------------------

.. button-link:: https://www.google.com/search?q=cheatsheet+python+conda
   :color: {{ cheatsheet_color }}
   :align: right
   :tooltip: Search Google for cheatsheet

   Find a Conda cheatsheet {{ cheatsheet_icon }}


Conda lets users create separate sets of packages for different projects called **environments**. 
When users switch between projects, they can switch to the environment of that project, which would prevent the need to 
manage packages each time a different project is used. The Conda manager allows you to create and manage 
environments with specific packages and Python versions. This can be useful if a specific
package requires a specific Python version.

One can list all *global* environments by:

.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      .. code-block:: powershell

         conda env list

   .. tab-item:: {{ macos }}
      :sync: mac

      .. code-block:: bash

         conda env list

.. note::

    A *global* environment, created using ``conda create --name`` is stored in Conda's default directory.
    Creating your environment in the global environment list will make it
    to activate just the environment name and centrally manage all your environments.

    Alternatively, one can create *subdirectory* environments.
    These are created using ``conda create --prefix``. It will be stored in the specified
    folder, which would keep the environment self-contained within your project.


Creating an environment with commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For example, let us create an environment with Conda for Course A. An environment can be created by using:

.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      .. code-block:: powershell

         # create an environment named 'course-A' (in the global environment list)
         conda create --name course-A
         # alternatively, the environment can be placed in a subdirectory
         conda create --prefix course-A

   .. tab-item:: {{ macos }}
      :sync: mac

      .. code-block:: bash

         # create an environment named 'course-A' (in the global environment list)
         conda create --name course-A
         # alternatively, the environment can be placed in a subdirectory
         conda create --prefix course-A


.. _learn-more-environments-yaml:

Creating an environment from an ``environment.yml`` file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In some cases an installation guide will share an `environment.yml <https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually>`__ file.
This file contains the full details to reproduce an environment.
When having an ``environment.yml`` file, it can be installed with (note, the file
can have *any* name):

.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      .. code-block:: powershell

         conda env create -f environment.yml

   .. tab-item:: {{ macos }}
      :sync: mac

      .. code-block:: bash

         conda env create -f environment.yml

Here is an example ``environment.yml`` file that creates an environment
named ``course-A``, with Python and ``numpy``:

.. code-block:: yaml

   name: course-A
   channels:
     - conda-forge
     - nodefaults
   dependencies:
     - python
     - numpy


Activating an environment
^^^^^^^^^^^^^^^^^^^^^^^^^

Once the environment is created, one can use the environment by *activating* it.

.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      .. code-block:: powershell
        
         # if the enviroment was created with --name:
         conda activate course-A
         # if the environment was created in a sub directory (--prefix):
         conda activate .\course-A

   .. tab-item:: {{ macos }}
      :sync: mac

      .. code-block:: bash

         # if the enviroment was created with --name:
         conda activate course-A
         # if the environment was created in a sub directory (--prefix):
         conda activate ./course-A

Once an environment has been created and sourced (activated), all ``python`` commands only act in *that environment*.

Every executed Python script will only use the packages installed
in the environment. To exit the environment, run the command ``conda deactivate``.


Example environment management with Conda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below is a complete example of creating an environment using a specific Python
version, installing a specific package, running code in the environment, and exiting it.

.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      .. code-block:: powershell

         conda create --name numpy-env python={{python_version_recommended}}
         conda activate numpy-env
         conda install "numpy=1.23"
         python -c "import numpy as np ; print(np.__version__)"
         conda deactivate

   .. tab-item:: {{ macos }}
      :sync: mac

      .. code-block:: bash

         conda create --name numpy-env python={{python_version_recommended}}
         conda activate numpy-env
         conda install "numpy=1.23"
         python3 -c "import numpy as np ; print(np.__version__)"
         conda deactivate

This code creates a new Conda environment named numpy-env with Python {{python_version_recommended}} installed. It then
activates the environment and installs version 1.23 of the Numpy library. After installation, 
it runs a Python command to import NumPy and print the installed version of Numpy to verify the installation. 
Finally, the environment is deactivated, returning the user to their previous environment.

.. tip::

    Further documentation on environments can be found
    `here <https://docs.anaconda.com/working-with-conda/environments/>`__ while
    management of the environments can be found `here <https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment>`__.


The equivalent ``environment.yml`` file would look like this:

.. code-block:: yaml

   name: numpy-env
   dependencies:
     - python={{python_version_recommended}}
     - numpy=1.23


Environments with venv
----------------------

While Conda offers powerful tools for managing complex environments and dependencies, there are 
situations where ``venv`` might be more suitable. ``venv`` is ideal for simpler projects that only require 
Python packages, as it is lightweight and easy to use.
It is built into Python, so it does not require 
additional installation, making it convenient for managing environments directly tied to the system's Python.


Using venv in VS Code
^^^^^^^^^^^^^^^^^^^^^^^^^^

VS Code helps manage virtual environments through some built-in commands. 
Here is a brief explanation of how to set up a virtual environment in VS Code:

First, check that you are already in a virtual environment (see point 5 below). If not, proceed to the next step.

1. Create a folder/directory according to the course you wish to work on.
   
   *This is optional but helps keep your projects organized.*.

2. Press :guilabel:`Open Folder` to start working in the designated course
   folder. If you already have several opened folders, this will not be
   visible. Just select the workspace.

   .. image:: /learn-more/images/environments-vscode-open-folder.png
      :width: 700
      :align: center
      :alt: Open the folder in VS Code

3. We will create a virtual environment once you are in a folder/workspace.
   Press :kbd:`Ctrl+Shift+P` and search for
   ``Python: Create Environment...``, and select that.

   .. image:: /learn-more/images/environments-vscode-python-env.png
      :width: 600
      :align: center
      :alt: VS Code command prompt

4. Next, select the option below:

   .. image:: /learn-more/images/environments-vscode-python-env-venv.png
      :width: 600
      :align: center
      :alt: VS Code venv creation

5. Check that the virtual environment is functional. Sometimes you must
   run a small Python script to enable the virtual environment,
   either press :fas:`arrow-right`, or :kbd:`Shift+Enter`.

   .. image:: /learn-more/images/environments-vscode-python-env-venv-check.png
      :width: 700
      :align: center
      :alt: Check if virtual environment is enabled through VS Code


Using venv in the Terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^

The package ``venv`` creates environments using the ``pip`` method.
Once an environment has been created and
sourced (activated), all ``pip`` commands only act within that environment.

.. tip:: 
    If you need to learn what ``pip`` is, please check the description in :doc:`pip`.

.. note::

    The ``venv`` package can only create environments with different packages.
    It cannot switch between different Python versions.

    An environment will be a directory on your computer. Deleting
    it will be the same as deleting the environment.

.. warning::
   Environments in :doc:`/learn-more/vscode/index` requires special handling when
   working in workspaces. Please see :ref:`here <faq-vscode-venv-workspace>`.


An environment can be created using:

.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      .. code-block:: powershell

         python -m venv <path to venv>
         # create an environment named 'course-A' in the current directory
         python -m venv course-A

   .. tab-item:: {{ macos }}
      :sync: mac

      .. code-block:: bash

         python3 -m venv <path to venv>
         # create an environment named 'course-A' in the current directory
         python3 -m venv course-A

Once created, one can *activate*/use the environment by *sourcing* a file.
Change ``course-A`` with the name of the environment.

.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      .. warning::
         Please see :ref:`this FAQ entry <faq-win-ps-execution-policy>`!

      .. code-block:: powershell

         course-A\Scripts\Activate.ps1

   .. tab-item:: {{ macos }}
      :sync: mac

      .. code-block:: bash

         source course-A/bin/activate


Every executed Python script will only use the packages installed
in the environment, and every ``pip`` command will only install/remove packages
in the environment. To exit the environment, run the command ``deactivate``.

Below is an example workflow of creating an environment, installing a specific
package, running a code using the environment, and exiting the environment.

.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      .. code-block:: powershell

         python -m venv numpy-env
         numpy-env\Scripts\Activate.ps1
         pip install "numpy==1.23.*"
         python -c "import numpy as np ; print(np.__version__)"
         deactivate

   .. tab-item:: {{ macos }}
      :sync: mac

      .. code-block:: bash

         python3 -m venv numpy-env
         source numpy-env/bin/activate
         pip install "numpy==1.23.*"
         python3 -c "import numpy as np ; print(np.__version__)"
         deactivate

This code creates a Python virtual environment called numpy-env using venv, then activates 
it to install version 1.23 of Numpy using ``pip``. After installing, it verifies
the installation by printing the installed Numpy version. Finally, the environment is deactivated, 
returning the user to their previous environment.

.. tip::
    Further documentation on environments are available on `VS Code's webpage <https://code.visualstudio.com/docs/python/environments>`__.


Using Virtual Environments with Jupyter/IPython
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Jupyter Notebooks and IPython are interactive computing environments that 
enable users to write and execute code in a notebook format. These notebooks 
can combine code, text, and visualizations. Jupyter Notebooks are 
commonly used in many DTU courses.

Virtual environments and Jupyter can cause issues when Jupyter is installed in the
system (not in the virtual environment). The kernel is fixed to launch
the Python interpreter it was installed with. The kernel is a process that allows you to 
execute the code in your Jupyter Notebook by providing the necessary Python language support.

The simplest way to check whether your Jupyter Notebook is using your virtual environment
is to execute the following code in a notebook cell:

.. code-block:: python

   import sys
   print(sys.exec_prefix)

You are all set if it shows your virtual environment's directory.
If not, install the kernel runner in the virtual environment:


.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      .. code-block:: powershell

         python -m ipykernel install --prefix <path to venv|conda-env>

   .. tab-item:: {{ macos }}
      :sync: mac

      .. code-block:: bash

         python3 -m ipykernel install --prefix <path to venv|conda-env>

Replace ``<path to venv|conda-env>`` with the path to your virtual environment. 
The problem and the fix are described in greater detail
`here <https://ipython.readthedocs.io/en/stable/install/kernel_install.html>`__.

