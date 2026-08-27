.. _install-python-macos-manual:
.. _manual-reference-macos:

{{ apple_icon }} Manual Installation
==========================================

.. _fully-manual-reference-mac:

 .. dropdown:: {{ video_install }}
    :open:
    :color: info

    .. raw:: html

       <iframe src="https://panopto.dtu.dk/Panopto/Pages/Embed.aspx?id=1d9d7a10-d86b-4947-8486-b4b10113e8f7" height="405" width="100%" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

.. _install-python-macos-manual-conda:

Step 1: Install Miniforge
---------------------------------------------------

.. card:: 

   #.
      Search for :menuselection:`Terminal` using your Spotlight search (:kbd:`Command+Space`) and press :kbd:`Enter`.

      .. image:: /images/install/MacOS-SpotlightSearch-Terminal.png
         :width: 80%
         :align: center

   #.
      Copy and paste the following lines of code into your terminal and press :kbd:`Enter`
      (be sure to execute both lines of code before proceeding):

      .. code-block:: bash

         curl -fsSLo Miniforge3.sh "https://github.com/dtudk/pythonsupport-forge/releases/latest/download/Miniforge3-MacOSX-$(uname -m).sh"
         bash Miniforge3.sh -b -p "${HOME}/miniforge3-dtu" ; source "${HOME}/miniforge3-dtu/etc/profile.d/conda.sh" ; conda activate ; conda init $(basename "$SHELL")
       
      .. include:: /_rst_includes/tip-copy.rst
      
   #.
      Close and reopen your terminal for the changes to take effect.


.. _install-python-macos-manual-vscode:

Step 2: Install Visual Studio Code
---------------------------------------------------

.. |applications| image:: /images/install/macos-applications.png
    :height: 25px

.. card:: 

   After the installation is finished, you need to download Visual Studio Code. 
   
   #.
      Click `here  <https://code.visualstudio.com/Download#>`__ to download Visual Studio Code.

   #. 
      Make sure that Visual Studio Code is under the |applications| folder in Finder.
      
      .. image:: /images/install/MacOS-finder-VSC.png
         :width: 400
         :align: center


.. _install-python-macos-manual-vscode-exts:

Step 3: Install extensions for Visual Studio Code
---------------------------------------------------

.. |extensions| image:: /images/install/extensions.png
    :height: 25px

.. card:: 

    #.
       Open Visual Studio Code and select the Extensions |extensions| tab on the left.

       .. image:: /images/install/VSC-extensions.png
          :width: 400
          :align: center
    
    #. 
       Search for `Python`, and download the extension. Make sure that it is from Microsoft. 

       .. image:: /images/install/macos-package-managed-python.png
          :width: 200
          :align: center

    #.
       Hereafter search for `Jupyter`, and download that extension as well. This also needs to be from Microsoft.
       
       .. image:: /images/install/macos-package-managed-jupyter.png
          :width: 200
          :align: center


.. include:: /_rst_includes/vscode-ai.rst

.. include:: /_rst_includes/tip-finish.rst

.. include:: verify.rst
