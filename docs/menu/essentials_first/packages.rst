Package management
===================

.. tip::
    You can copy and paste all code in the grey code blocks below by hovering your mouse over the block and pressing the icon in the top right.

Navigating packages
^^^^^^^^^^^^^^^^^^^

Quite often it is necessary to list and find out if you already have a certain package and see what package version you have.

Using ``conda list`` you can see all the packages that you have installed and their specific versions.

.. tab-set::

   .. tab-item:: {{ win_powershell }}
      :sync: powershell

      .. code-block:: powershell

         conda list


   .. tab-item:: {{ win_batch }}
      :sync: batch

      .. code-block:: winbatch


         conda list


   .. tab-item:: {{ mac_bash }}
      :sync: mac

      .. code-block:: bash

    
         conda list


   .. tab-item:: {{ linux_bash }}
      :sync: bash

      .. code-block:: bash

  
         conda list


Installing packages
^^^^^^^^^^^^^^^^^^^


Packages can be installed in a very simple manner by using ``conda install``:


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

The above will install version 1.24 of Numpy, a Scipy version lower than 1.10 and the latest version of matplotlib.








