.. _install-python-linux:

{{ linux_icon }} --- Manual Installation 
==========================================

.. button-ref:: ../macos/homebrew
   :ref-type: doc
   :align: right
   :color: primary
   
   Press here for {{ macos }} {{ apple_icon }}
   

.. _install-python-linux-conda:

Step 1: Install Miniconda
--------------------------

.. card:: 

    #. 
        Go to `this website  <https://docs.anaconda.com/miniconda/index.html#latest-miniconda-installer-links>`__.

    #. 
        Under the title *Latest Miniconda installer links*, you will see different installers where you must download the ``Miniconda3 Linux 64-bit`` that fits your hardware.

    #.
        It will be easier to use if ``conda`` is added to the ``PATH``
        in your shell startup scripts as the installer will suggest you to do.


.. _install-python-linux-python:

Step 2: Install Python
--------------------------

.. card:: 

    #. 
       Open a Terminal.

    #.
       Run the following command in the Terminal by copying and pasting and pressing :kbd:`Enter`:

       .. code:: bash

           conda config --add channels conda-forge ; conda config --remove channels defaults

       .. include:: /_rst_includes/tip-copy.rst

    #. 
       Copy the following line of code into your terminal and press :kbd:`Enter`:

       .. code:: bash

           conda install python={{ python_version_recommended }} dtumathtools pandas scipy statsmodels uncertainties -y


.. _install-python-linux-vscode:

Step 3: Install Visual Studio Code
-----------------------------------

.. card:: 

    #. 
        Go to `this website  <https://code.visualstudio.com>`__.
    
    #.
        Click the download button and follow the instructions.
      

.. _install-python-linux-vscode-exts:

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

