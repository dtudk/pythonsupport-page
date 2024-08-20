.. _install-python-windows:

{{ windows_icon }} --- Manual Installation 
==========================================

.. button-ref:: ../macos/homebrew
   :ref-type: doc
   :align: right
   :color: primary
   

    Press here for {{ macos }} {{ apple_icon }}
   

.. dropdown:: Video Guide
    :open:
    :color: info

    .. raw:: html 
    
        <iframe src="https://panopto.dtu.dk/Panopto/Pages/Embed.aspx?id=045bfd79-bb8a-49af-b1d7-b1ce00a9662e&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&captions=false&interactivity=all" height="405" width=100% style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

.. _install-python-windows-conda:

Step 1: Install Miniconda
--------------------------

.. card:: 

    #. 
        Go to `this website  <https://docs.anaconda.com/miniconda/index.html#latest-miniconda-installer-links>`__.

    #. 
        Under the title *Latest Miniconda installer links*, you will see different installers where you must download the ``Miniconda3 Windows 64-bit``, as shown below.

        .. image:: /images/install/windows-fully-manual-miniconda.png
            :width: 400
            :align: center

    #. 
        Follow the instructions during the installation.
        Make sure to cross off all the options regarding ``PATH``, as shown below.

        .. image:: /images/install/Miniconda-install-path.png
            :width: 400
            :align: center


.. _install-python-windows-python:

Step 2: Install Python
--------------------------

.. card:: 

    #. 
       Open PowerShell as an Administrator by opening the menu bar, then search for :menuselection:`Windows PowerShell`.
        

    #.
       Once you see Windows PowerShell on the right-hand side, you can select *Run as Administrator*. If not, right-click the
       icon and choose :menuselection:`Run as Administrator`. 

       .. image:: /images/install/windows-ps-run-admin.png
           :width: 400
           :align: center

    #.
       Run the following command in the Terminal by copying and pasting and pressing :kbd:`Enter`:

       .. code:: bash

           conda config --add channels conda-forge ; conda config --remove channels defaults

       .. include:: /_rst_includes/tip-copy.rst

    #. 
       Copy the following line of code into your PowerShell and press :kbd:`Enter`:

       .. code:: bash

           conda install python={{ python_version_recommended }} dtumathtools pandas scipy statsmodels uncertainties -y


.. _install-python-windows-vscode:

Step 3: Install Visual Studio Code
-----------------------------------

.. card:: 

    #. 
        Go to `this website  <https://code.visualstudio.com>`__.
    
    #.
        Click the download button and follow the instructions.

        .. image:: /images/install/windows-fully-manual-vsc-webpage.png
            :width: 500
            :align: center
      

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

