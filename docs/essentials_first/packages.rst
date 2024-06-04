Installing packages
===================

Packages can be installed in a very simple manner, note how multiple packages and associated requirements
can be specified in a single invocation of the program.

.. note::

   ``conda list`` will give you the current list of installed packages.

.. tab-set::

   .. tab-item:: {{ win_powershell }}
      :sync: powershell

      .. code-block:: powershell

         conda install "numpy==1.24.*" "scipy<1.10" "matplotlib"

   .. tab-item:: {{ win_batch }}
      :sync: batch

      .. code-block:: winbatch

         conda install "numpy==1.24.*" "scipy<1.10" "matplotlib"

   .. tab-item:: {{ mac_bash }}
      :sync: mac

      .. code-block:: bash

         conda install "numpy==1.24.*" "scipy<1.10" "matplotlib"

   .. tab-item:: {{ linux_bash }}
      :sync: bash

      .. code-block:: bash

         conda install "numpy==1.24.*" "scipy<1.10" "matplotlib"

The above will install:


.. note::
   
   You will quite often encounter some warnings or notices from ``pip``,
   they look something like the following. It is perfectly normal, and
   it is not necessary to do what it says.

   ``pip`` versions 21 and older:

   .. image:: /menu/images/pip21_upgrade.png
      :width: 800
      :align: left
      :alt: pip upgrade notice from versions 21 and older
   
   ``pip`` versions 22 and newer:

   .. image:: /menu/images/pip22_upgrade.png
      :width: 550
      :align: left
      :alt: pip upgrade notice from versions 22 and newer




.. _pip-navigating:

Navigating packages
^^^^^^^^^^^^^^^^^^^

Quite often it is necessary to list and find extra information about the packages
that is installed.

Here is a set of commands that can be useful for interacting with the ``pip``
packages:


.. tab-set::

   .. tab-item:: {{ win_powershell }}
      :sync: powershell

      .. code-block:: powershell

         # List the packages installed
         conda list


   .. tab-item:: {{ win_batch }}
      :sync: batch

      .. code-block:: winbatch

         # List the packages installed
         conda list


   .. tab-item:: {{ mac_bash }}
      :sync: mac

      .. code-block:: bash

         # List the packages installed
         conda list


   .. tab-item:: {{ linux_bash }}
      :sync: bash

      .. code-block:: bash

         # List the packages installed
         conda list








