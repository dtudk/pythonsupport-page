.. _manual-reference-macos:

{{ apple_icon }} --- Manual Installation 
==========================================

.. button-ref:: ../windows/manual
   :ref-type: doc
   :align: right
   :color: primary
   

    Press here for Windows {{ windows_icon }}


.. _fully-manual-reference-mac:

.. dropdown:: {{ video_install }}
    :open:
    :color: info

    .. raw:: html

       <iframe src="https://panopto.dtu.dk/Panopto/Pages/Embed.aspx?id=6e4b5e83-a182-4f4d-936c-b1dc00bb2e1d" height="405" width=100% style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>



Step 1: Install Miniconda
---------------------------------------------------


.. card:: 
    
   #.
      Before starting, you need to know which processor you have. If you do not know, you can find 
      out by pressing the {{ apple_icon }} logo at the top left of your
      screen. Go to :menuselection:`About This Mac --> Chip/Processor`. You need to know if it is an **M** or **Intel** processor.

      .. image:: /images/install/macos-fully-manual-processor.png
         :width: 200
         :align: center
   
   #. 

      * If you have an **M** processor, click `here <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.pkg>`__.

      * If you have an **Intel** processor, click `here <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg>`__.
   #.
      When the installer has been downloaded, open it and follow the instructions.

      .. image:: /images/install/macos-fully-manual-miniconda-pkg.png
         :width: 400
         :align: center


Step 2: Install Python
---------------------------------------------------

.. card:: 

   #.
      Search for :menuselection:`Terminal` using your Spotlight search (:kbd:`Command+Space`) and press :kbd:`Enter`.

      .. image:: /images/install/MacOS-SpotlightSearch-Terminal.png
         :width: 80%
         :align: center

   #.
      Run the following command in the Terminal by copying and pasting and pressing :kbd:`Enter`:

      .. code:: bash

         conda config --add channels conda-forge ; conda config --remove channels defaults ; conda config --set channel_priority strict

      .. include:: /_rst_includes/tip-copy.rst

   #.
      Copy and paste the following line of code into your terminal and press :kbd:`Enter`:

      .. code:: bash

         conda install python={{ python_version_recommended }} dtumathtools pandas scipy statsmodels uncertainties -y



Step 3: Install Visual Studio Code
---------------------------------------------------

.. |applications| image:: /images/install/macos-applications.png
    :height: 25px

.. card:: 

   After the installation is finished, you need to download Visual Studio Code. 
   
   #.
   
      Go to `this website  <https://code.visualstudio.com/Download#>`__.
      
   #. 
      Click the **Mac** button and follow the instructions.

      .. image:: /images/install/macos-fully-manual-vsc-webpage.png
         :width: 500
         :align: center

   #. 
      Make sure that Visual Studio Code is under the |applications| folder in Finder.
      
      .. image:: /images/install/MacOS-finder-VSC.png
         :width: 400
         :align: center


Step 4: Install extensions for Visual Studio Code
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


.. include:: /_rst_includes/tip-finish.rst

.. include:: verify.rst
