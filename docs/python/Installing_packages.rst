.. _Installing packages:

Installing packages
=========================================

When using Python, you will most likely need to import several packages in your script. 
Python comes with a standard library that includes many of the most common packages. 
However, some packages you wil need to install manually. 

Depending on which distribution of Python you are using, you will need to use a different package manager.

=========================================
Using the official Python distribution
=========================================
If you are using the official Python distribution, you will need to use the pip package manager. Open up a terminal and run the following: 



.. tab:: {{ windows }}

   .. code-block:: bash

      python -m pip install numpy

.. tab:: {{ macos }}

   .. code-block:: bash

      python3 -m pip install numpy

.. tab:: {{ linux }}

   .. code-block:: bash

      python3 -m pip install numpy


.. note::

   The code above will install the library "numpy". For installation of other libraries, simply delete "numpy", and write the name of the library you want to download.



=========================================
Using a conda distribution
=========================================

If you are using a conda distribution, you will need to use the conda package manager.

On windows or on mac open a terminal and type:


.. tab:: {{ windows }}

   .. code-block:: bash

      conda install numpy

.. tab:: {{ macos }}

   .. code-block:: bash

      conda install numpy

.. tab:: {{ linux }}

   .. code-block:: bash

      conda install numpy



.. note::

   The code above will install the library "numpy". For installation of other libraries, simply delete "numpy", and write the name of the library you want to download.



