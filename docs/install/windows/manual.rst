.. _install-python-windows-manual:

{{ windows_icon }} Manual Installation
==========================================

 .. dropdown:: {{ video_install }}
    :open:
    :color: info

    .. raw:: html

        <iframe src="https://panopto.dtu.dk/Panopto/Pages/Embed.aspx?id=0626cb3a-1188-42b4-9618-b4b100d5ed62" height="405" width=100% style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>


.. _install-python-windows-manual-conda:

Step 1: Install Miniforge
--------------------------
      
.. card:: 

   #.
      Click `here <https://github.com/dtudk/pythonsupport-forge/releases/latest/download/Miniforge3-Windows-x86_64.exe>`__ to download the installer.

   #. Open the installer, once it has been downloaded. 

   #. Once the installer is open you might encounter a security warning. Click on the :guilabel:`More info` button and then :guilabel:`Run anyway`.
      
      .. container:: images-side-by-side

         .. image:: /images/install/windows-miniforge-security-warning.png
            :width: 45%

         .. image:: /images/install/windows-miniforge-run-anyway.png
            :width: 45%


   #.
      Follow the instructions from the installer.

      .. dropdown:: Error: 'Destination Folder' contains 1 space
         :animate: fade-in-slide-down
         :color: warning
         :icon: alert

         If your Windows username contains spaces, you will get an error (e.g. ``Error: 'Destination Folder' contains 1 space.``) asking you to remove spaces from the installation path.

         In that case, change the :guilabel:`Destination Folder` to ``C:\miniforge3-dtu`` instead.

         .. note::

            In case the destination folder is not writeable, run the installer as administrator (right-click on the installer ``.exe`` and choose :guilabel:`Run as administrator`).


.. _install-python-windows-manual-vscode:

Step 2: Install Visual Studio Code
-----------------------------------

.. card:: 

   #.
      Go to `this website  <https://code.visualstudio.com/Download>`__.
   
   #.
      Click the **Windows** button

      .. image:: /images/install/windows-fully-manual-vsc-webpage.png
         :width: 500
         :align: center
   
   #. 
      Open the installer and follow the instructions. 


.. _install-python-windows-manual-vscode-exts:

Step 3: Install extensions for Visual Studio Code
---------------------------------------------------

.. |extensions| image:: /images/install/extensions.png
   :height: 25px


.. card:: 

   #.
      Open Visual Studio Code and select the Extensions |extensions| tab on the left. 
      
   #.
      Here search for `Python`, and download the extension. Make sure that it is from Microsoft. 

      .. image:: /images/install/macos-package-managed-python.png
         :width: 200
         :align: center
      
   #.
      Search for `Jupyter`, and download 
      that extension as well. This also needs to be from Microsoft.

      .. image:: /images/install/macos-package-managed-jupyter.png
         :width: 200
         :align: center


.. include:: /_rst_includes/vscode-ai.rst

.. include:: /_rst_includes/tip-finish.rst

.. include:: verify.rst

