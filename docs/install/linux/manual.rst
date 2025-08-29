.. _install-python-linux-manual:

{{ linux_icon }} --- Manual Installation 
==========================================


.. _install-python-linux-manual-conda:

Step 1: Install Miniforge
--------------------------

.. card:: 

   #.
      Click `here <https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh>`__ to download the installer.
      Change the ``x86_64`` to your hardware architechture, if it is not ``x86-64``.

   #.
      Run the installer in a terminal:

      .. code-block:: bash

         bash Miniforge3-Linux-x86_64.sh -b -p "${HOME}/miniforge3"
         source "${HOME}/miniforge3/etc/profile.d/conda.sh"
         conda activate
         conda init $(basename $SHELL)

      .. include:: /_rst_includes/tip-copy.rst

.. _install-python-linux-manual-python:

Step 2: Install Python
--------------------------

.. card:: 

   #. 
      Open a Terminal.

   #. 
      Copy the following line of code into your terminal and press :kbd:`Enter`:

      .. code-block:: bash

         conda install python={{ python_version_recommended }} dtumathtools pandas scipy statsmodels uncertainties -y
      


.. _install-python-linux-manual-vscode:

Step 3: Install Visual Studio Code
-----------------------------------

.. card:: 

   #.
      Go to `this website  <https://code.visualstudio.com>`__.
   
   #.
      Click the download button and follow the instructions.
      

.. _install-python-linux-manual-vscode-exts:

Step 4: Install extensions for Visual Studio Code
---------------------------------------------------

.. |extensions| image:: /images/install/extensions.png
    :height: 25px


.. card:: 

   #.
      Open Visual Studio Code and select the Extensions |extensions| tab on the left. 
      
   #.
      Here search for `Python`, and download the extension. Make sure that it's from Microsoft. 

      .. image:: /images/install/macos-package-managed-python.png
         :width: 200
         :align: center
      
   #.
      Search for `Jupyter`, and download 
      that extension as well. This also needs to be from Microsoft.

      .. image:: /images/install/macos-package-managed-jupyter.png
         :width: 200
         :align: center


.. include:: /_rst_includes/tip-finish.rst

.. include:: verify.rst

