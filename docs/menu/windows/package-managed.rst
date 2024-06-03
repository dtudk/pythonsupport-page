Windows - Package managed installation guide
================================

Step 1: Download Chocolatey
--------------------------------------

This is done by opening your Command Prompt as an administrator. This can be done by searching for ``cmd``. Once you see ``Command Prompt``, on the right hand side you can select ``Run as administrator``.

Next thing you need to do is to paste the following line of code (the whole one), into your command prompt, and press enter:

.. code-block::

    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))




Step 2: Install miniconda3
--------------------------------

Open your terminal and paste the following and click enter:

.. code-block::

    choco install miniconda3

After this you need to install the Anaconda Navigator. This is done by running the following line in your command prompt:

.. code-block::

    conda install anaconda-navigator


Now run the following commands in terminal one at a time: 

.. code-block::

    CODIGO

and 

.. code-block::

    pip install dtumathtools uncertainties 




Step 3: Install Visual Studio Code
--------------------------------

This is done by pasting the following in you terminal and executing it: 
    
.. code-block::

    choco install vscode

Finally you need to install some extensions in visual studio code. This is done by pressing the 'extensions button' on the left side or press command + shift + X. Here search for Python, and download the extension. Make sure that it's from Microsoft. Hereafter search for Jupyter, and download that extension as well. This also needs to be from Microsoft.
