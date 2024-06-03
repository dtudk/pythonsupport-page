Windows - Fully manual installation guide
================================


Step 1: Download miniconda
--------------------------------------

Go to `Anaconda Website <https://docs.anaconda.com/free/miniconda/index.html>`_, where you scroll down to ``Latest Miniconda installer links``. Here you need to click and download ``Miniconda3 Windows 64-bit``. Then you need to follow the instructions from the package. 


Step 2: Install Anaconda navigator
--------------------------------------

This is done by running the following line in your command prompt:

.. code-block:: RST

    conda install anaconda-navigator

If you are unsure on how to open the command prompt, it can be done by searching for ``cmd``. Once you see ``Command Prompt``. Then on the right hand side you can select ``Run as administrator``. 

Now run the following commands in your command prompt one at a time: 

.. code-block::

    "Command to downgrade conda base python version" 


and 

.. code-block::

    pip install dtumathtools uncertainties


Step 3: Install Visual Studio Code
--------------------------------------

This is done by going to `Visual Studio Code <https://code.visualstudio.com>`_. Click the download button and follow the instructions. 

Open VSC and select the Extensions tab on the left, or press command + shift + X. Here search for Python, and download the extension. **Make sure that it's from Microsoft**. Hereafter search for Jupyter, and download that extension as well. This also needs to be from Microsoft.
