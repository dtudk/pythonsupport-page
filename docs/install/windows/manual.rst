.. _install-python-windows:

{{ windows_icon }} --- Manual Installation 
==========================================

.. .. button-ref:: ../macos/homebrew
   :ref-type: doc
   :align: right
   :color: primary

    Press here for {{ macos }} {{ apple_icon }}


.. dropdown:: {{ video_install }}
    :open:
    :color: info

    .. raw:: html

       <iframe src="https://panopto.dtu.dk/Panopto/Pages/Embed.aspx?id=f5831f1f-6ea3-435b-8677-b1dc00da49e7" height="405" width=100% style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>


.. _install-python-windows-conda:

Step 1: Install Miniconda
--------------------------

.. card:: 

   #.
      Click `here  <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe>`__ to download the installer.

   #. Open the installer, once it has been downloaded. 

   #.
      Follow the instructions from the installer.
      Make sure to cross off all the options regarding ``PATH``, as shown below.

      .. image:: /images/install/Miniconda-install-path.png
         :width: 400
         :align: center


.. _install-python-windows-python:

Step 2: Install Python
--------------------------

.. card:: 

   #.
      Open :menuselection:`Anaconda PowerShell` as an `Administrator` by opening the menu bar, then search for :menuselection:`Anaconda PowerShell`.

      Once you see Anaconda PowerShell on the right-hand side, you can select :menuselection:`Run as Administrator`.
      If not, right-click the icon and choose :menuselection:`Run as Administrator`. 

      .. image:: /images/install/windows-anaconda-ps-run-admin.png
         :width: 400
         :align: center

   #.
      Run the following command in the PowerShell window by copying, pasting and pressing :kbd:`Enter`:

      .. code-block:: pwsh

         Set-ExecutionPolicy -Force RemoteSigned

      .. include:: /_rst_includes/tip-copy.rst

   #.
      Run the following commands in the PowerShell window by copying, pasting and pressing :kbd:`Enter`:

      .. code-block:: pwsh

         conda init

      .. code-block:: pwsh

         conda config --add channels conda-forge ; conda config --remove channels defaults ; conda config --set channel_priority strict

   #.
      Run the following commands in the PowerShell window by copying, pasting and pressing :kbd:`Enter`:

      .. code-block:: pwsh

         conda install python={{ python_version_recommended }} dtumathtools pandas scipy statsmodels uncertainties -y



.. _install-python-windows-vscode:

Step 3: Install Visual Studio Code
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


.. _install-python-windows-vscode-exts:

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

