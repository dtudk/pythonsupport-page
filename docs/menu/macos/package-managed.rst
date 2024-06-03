MacOS - Package managed installation guide
================================


Step 1: Install Homebrew
-------------------------

Start by opening your terminal. This can be done by pressing ``cmd`` + ``space`` and then searching for terminal.

Paste the following line of code into your terminal and press ``enter``. 

.. code-block:: 
        
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"  && (echo; echo 'eval "$(/usr/local/bin/brew shellenv)"') >> ~/.zshrc && (echo; echo 'eval "$(/usr/local/bin/brew shellenv)"') >> ~/.bash_profile && eval "$(/usr/local/bin/brew shellenv)" && echo "Homebrew installed. Note: You do not need to run anything else in the terminal" && clear 


Step 2: Download Anaconda Navigator
--------------------------------------

This is done by running the following line in your terminal:

.. code-block:: 
        
    conda install anaconda-navigator


Now run the following commands in terminal one at a time: 

.. code-block:: 

    Command to downgrade conda base python version 

and 

.. code-block:: 

    pip3 install dtumathtools uncertainties 



Step 3: Install Visual Studio Code
--------------------------------------

This is done by pasting the following in you terminal and pressing enter:

.. code-block::    

    brew install --cask visual-studio-code

This is done by pressing the 'extensions button' on the left side or press command + shift + X. 
Here search for Python, and download the extension. Make sure that it's from Microsoft. 
Hereafter search for Jupyter, and download that extension as well. This also needs to be from Microsoft.

