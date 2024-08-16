.. _manual-reference-macos:

{{ apple_icon }} --- Manual Installation 
-----------------------------------------


.. button-link:: ../windows/manual.html
   :align: right
   :color: primary
   

    Press here for Windows {{ windows_icon }}


.. _fully-manual-reference-mac:

Step 1: Install Miniconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. card:: 
    

    #. 
        Before starting, you need to know which processor you have. If you do not know which you have, you can find 
        out by pressing the {{ apple_icon }} logo on the top left of your
        screen. Go to :menuselection:`About This Mac --> Chip/Processor`. You need to know if it is an M1, M2, M3 or an Intel processor.

        .. image:: /images/install/macos-fully-manual-processor.png
            :width: 200
            :align: center

        
    #.  
        Go to `this website <https://docs.anaconda.com/miniconda/index.html#latest-miniconda-installer-links>`__.
    

    #. 
        Look for the title *Latest Miniconda installer links*. Here you you will see different installers where you will 
        have to download the correct one.
    
        * If you have an Intel processor you need to select Miniconda3 MacOS Intel x86 64-bit pkg.
        * If you have an **M** processor you need to select Miniconda3 MacOS Apple M1 64-bit pkg. *Even* if you have an **M2** or **M3**.

        .. image:: /images/install/macos-fully-manual-miniconda.png
            :width: 400
            :align: center


    #.
        Follow the instructions from the package.

        .. image:: /images/install/macos-fully-manual-miniconda-pkg.png
            :width: 400
            :align: center


Step 2: Install Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. card:: 


    #. 
        Open the Terminal by pressing the :kbd:`Command+Space` key at the same time, and searching for *Terminal*.  

        .. image:: /images/install/MacOS-spotlight-terminal.png
            :width: 300
            :align: center

    #.
        Run the following command in the Terminal by copying and pasting and pressing :kbd:`Enter`:

        .. code:: bash

            conda config --add channels conda-forge ; conda config --remove channels defaults

        .. include:: /_rst_includes/tip-copy.rst

    #.
        Copy and paste the following line of code into your terminal and press :kbd:`Enter`:


        .. code:: bash

            conda install python={{ python_version_recommended }} dtumathtools uncertainties -y



Step 3: Install Visual Studio Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |applications| image:: /images/install/macos-applications.png
    :height: 25px

.. card:: 

    After the installation is finished, you need to download Visual Studio Code. 
    
    #. 
        Go to `this website  <https://code.visualstudio.com>`__.
        
        
    #.  
        Click the download button and follow the instructions.

        .. image:: /images/install/macos-fully-manual-vsc-webpage.png
            :width: 500
            :align: center

    #.  
        Make sure that Visual Studio Code is under the |applications| folder in Finder.
        
        .. image:: /images/install/MacOS-finder-VSC.png
            :width: 400
            :align: center
    

   

Step 4: Install extensions for Visual Studio Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |extensions| image:: /images/install/extensions.png
    :height: 25px

.. card:: 

    #. 
        Open Visual Studio Code and select the Extensions |extensions| tab on the left.

        .. image:: /images/install/VSC-extensions.png
            :width: 400
            :align: center
    
    #.  
        Search for Python, and download the extension. Make sure that it is from Microsoft. 

        .. image:: /images/install/macos-package-managed-python.png
            :width: 200
            :align: center

    #. 
        Hereafter search for Jupyter, and download that extension as well. This also needs to be from Microsoft.
        
        .. image:: /images/install/macos-package-managed-jupyter.png
            :width: 200
            :align: center


.. include:: /_rst_includes/tip-finish.rst

.. include:: verify.rst
