.. _package-managed-reference-macos:


{{ apple_icon }} --- Homebrew Installation
============================================

.. button-link:: ../windows/manual.html
   :align: right
   :color: primary
   

    Press here for Windows {{ windows_icon }}


Step 1: Install Homebrew 
--------------------------

.. card:: 

    #.
        Go to `this website <https://brew.sh>`__ and follow the instructions.
        
    #.  
        The Homebrew website will ask you to open a terminal.
        This can be done by pressing :kbd:`Command+Space` at the same time.
        Then search for :menuselection:`Terminal` and press :kbd:`Enter`.
        Do *not* close the terminal once the installation script has finished.

        .. image:: /images/install/MacOS-spotlight-terminal.png
            :width: 100%
            :align: center

        .. image:: /images/install/macos-package-managed-homebrew.png
            :width: 400
            :align: center

    #.
        
        Add Homebrew to the **PATH** by copying, pasting and running the code that Homebrew displays in the Terminal (look at the picture for guidance). 
        Press :kbd:`Enter` once you have pasted the code. The code should look similar to the following image, 
        but might differ a little for different {{ macos }} versions.

        .. image:: /images/install/macos-package-managed-homebrew-terminal-instructions.png
            :width: 400
            :align: center



.. _step2-homebrew-reference:

Step 2: Install Miniconda and Python
-------------------------------------

.. card::

    #. 
        Close the previously used Terminal, and open up a new Terminal (:kbd:`Command+Space`).

    #.
        Paste the following code in the Terminal and press :kbd:`Enter`.

        .. code-block:: bash

            brew install --cask miniconda

    #.
        Run the following command in the Terminal by copying and pasting and pressing enter:

        .. code-block:: bash

            conda config --add channels conda-forge ; conda config --remove channels defaults

        .. include:: /_rst_includes/tip-copy.rst


    #.
        Run the following command in the Terminal by copying and pasting and pressing enter:

        .. code-block:: bash

            conda install python={{ python_version_recommened }} -y ; conda install dtumathtools uncertainties -y
            
    

Step 3: Install Visual Studio Code 
-----------------------------------

.. card::
    
    Install Visual Studio Code by pasting the following in your terminal and pressing :kbd:`Enter`.

    .. code-block:: bash

        brew install --cask visual-studio-code


Step 4: Install extensions for Visual Studio Code
-------------------------------------------------

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


.. include:: /_rst_include/tip-finish.rst

.. include:: verify.rst
