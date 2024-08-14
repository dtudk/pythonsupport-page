.. _manual-reference-windows:

{{ windows_icon }} --- Manual Installation 
=============================================


.. button-link:: ../macos/manual.html
   :align: right
   :color: primary
   

    Press here for {{ macos }} {{ apple_icon }}
   

.. dropdown:: Video guide
    :color: info

    .. raw:: html
    
        <iframe src="https://panopto.dtu.dk/Panopto/Pages/Embed.aspx?id=e5e4bea0-13f2-4b1e-85cd-b1c800e7391c&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&captions=false&interactivity=all" height=100%  style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>




Step 1: Install Miniconda
--------------------------

.. card:: 

    #. 

        Go to to `this website  <https://docs.anaconda.com/miniconda/index.html#latest-miniconda-installer-links>`__.


    #. 
        
        Under the title *Latest Miniconda installer links*, you will see different installers where you will have to download the ``Miniconda3 Windows 64-bit``, as shown below.



        .. image:: /images/install/windows-fully-manual-miniconda.png
            :width: 400
            :align: center


    #. 

        Follow the instructions during the installation.
        Make sure to cross off all the options regarding **PATH** as shows below.

        .. image:: /images/install/Miniconda-install-path.png
            :width: 400
            :align: center


Step 2: Install Python
-------------------------


.. card:: 

    #. 
        Open PowerShell as an administrator by opening the menu bar, then search for :menuselection:`Windows PowerShell`.
        

    #.

        Once you see Windows PowerShell, on the right hand side you can select *Run as administrator*. If not, right-click the
        icon and select :menuselection:`Run as administrator`. 

        .. image:: /images/install/windows-ps-run-admin.png
            :width: 400
            :align: center

    #. 
        Copy the following line of code into your terminal and press enter:        


    .. code-block:: bash

        conda install python={{ python_version_recommended }} -y ; conda install -c conda-forge dtumathtools uncertainties -y

    .. tip::
        You can copy and paste all code in the gray code blocks above by hovering your mouse over the block and pressing the icon in the top right.

        



Step 3: Install Visual Studio Code
------------------------------------

.. card:: 

    #. 
    
        Go to `this website  <https://code.visualstudio.com>`__.
    
    #.
    
        Click the download button and follow the instructions.

        .. image:: /images/install/windows-fully-manual-vsc-webpage.png
            :width: 500
            :align: center
      

Step 4: Install extensions for Visual Studio Code
-------------------------------------------------

.. |extensions| image:: /images/install/extensions.png
    :height: 25px


.. card:: 

    #. 

        Open Visual Studio Code and select the Extensions |extensions| tab on the left. 
        
    #.
        Here search for Python, and download the extension. Make sure that it's from Microsoft. 

        .. image:: /images/install/macos-package-managed-python.png
            :width: 200
            :align: center
        
    #. 
        Search for Jupyter, and download 
        that extension as well. This also needs to be from Microsoft.

        .. image:: /images/install/macos-package-managed-jupyter.png
            :width: 200
            :align: center




.. tip::
    When you have finished the guide, we **strongly recommend** checking out the :ref:`Python Essentials <essentials-reference>` to prepare you for coding.


.. include:: verify.rst

