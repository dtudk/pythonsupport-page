MacOS - Package managed installation guide
================================


Step 1: Install Homebrew
-------------------------

Start by opening your ``terminal``. This can be done by pressing ``command`` + ``space`` and then searching for ``terminal``.

Paste the following line of code into your terminal and press ``enter``. 

.. hint::

    You can copy the lines by clicking the icon in the top right corner of the code block. 


.. code-block::

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"  && (echo; echo 'eval "$(/usr/local/bin/brew shellenv)"') >> ~/.zshrc && (echo; echo 'eval "$(/usr/local/bin/brew shellenv)"') >> ~/.bash_profile && eval "$(/usr/local/bin/brew shellenv)" && echo "Homebrew installed. Note: You do not need to run anything else in the terminal" && clear && echo 'Homebrew installed'

Step 2: Install Miniconda 
--------------------------------------
Again open a terminal (if you closed it) and paste the following line of code into your terminal and press ``enter``.

.. code-block:: 

    brew install --cask Miniconda

Step 3: Install the anaconda Navigator GUI
--------------------------------------

This is done by running the following line in your terminal:

.. code-block:: 
        
    conda install anaconda-navigator --yes


Now run the following commands in terminal one at a time: 

.. code-block:: 

     conda install python=3.11 --yes
and 

.. code-block:: 

    conda install -c conda-forge dtumathtools uncertainties 



Step 3: Install Visual Studio Code
--------------------------------------

This is done by pasting the following in you terminal and pressing enter:

.. code-block::    

    brew install --cask visual-studio-code

This is done by pressing the 'extensions button' on the left side or press ``command`` + ``shift`` + ``X``. 
Here search for ``Python``, and download the extension. Make sure that it's from Microsoft. 
Hereafter search for ``Jupyter``, and download that extension as well. This also needs to be from Microsoft.

