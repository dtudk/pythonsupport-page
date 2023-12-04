.. _install-packages:

Installing packages
=========================================

When using Python, you will most likely need to import several packages in your script. 
Python comes with a standard library that includes many of the most common packages. 
However, some packages you will need to install manually. 

Depending on which distribution of Python you are using, you will need to use a different package manager.

.. note::
   
   If you at some point have trouble with installing a package, and you already have Anaconda installed, consider deleting it, since this can miscommunicate with pip.
   You can find a guide for the uninstalling process :ref:`by clicking here <uninstall-conda>`.


Using the official Python distribution
=========================================

.. note::

   If you are unsure about using the terminal, we advice that you read :ref:`this <os-terminal>` before proceeding.

If you are using the official Python distribution, you will need to use the :ref:`pip` package manager. Open up a terminal and run the following: 



.. tab:: {{ win_powershell }}

   .. code-block:: powershell

      python -m pip install numpy

.. tab:: {{ mac_bash }}

   .. code-block:: bash

      python3 -m pip install numpy

.. tab:: {{ linux_bash }}

   .. code-block:: bash

      python3 -m pip install numpy


.. tip::

   The code above will install the library ``numpy``. For installation of other libraries, simply delete ``numpy``, and write the name of the library you want to download.

.. note::

   If you get the error message ending in ``(mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64'))``, run the following instead:


   .. tab:: {{ win_powershell }}

      .. code-block:: powershell

         pip install --upgrade --force-reinstall numpy

   .. tab:: {{ mac_bash }}

      .. code-block:: bash

         pip3 install --upgrade --force-reinstall numpy

   .. tab:: {{ linux_bash }}

      .. code-block:: bash

         pip3 install --upgrade --force-reinstall numpy



Using a conda distribution
=========================================

If you are using a conda distribution, you will need to use the conda package manager.

On windows or on mac open a terminal and type:


.. tab:: {{ win_powershell }}

   .. code-block:: powershell

      conda install numpy

.. tab:: {{ mac_bash }}

   .. code-block:: bash

      conda install numpy

.. tab:: {{ linux_bash }}

   .. code-block:: bash

      conda install numpy


.. tip::

   The code above will install the library ``numpy``. For installation of other libraries, simply replace ``numpy`` with the name of the library you want to install.
