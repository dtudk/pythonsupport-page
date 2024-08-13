.. _package-managed-reference-macos:


MacOS - Package managed installation guide
==========================================

.. button-ref:: manual-reference-windows
    :ref-type: ref
    :color: info

    Not using **MacOS**? Press here for **Windows** guides.

.. todo::
    Change color?

Step 1: Install Homebrew 
--------------------------

First you need to download the package manager Homebrew.
This is done by going to `this website <https://brew.sh>`_ and follow the instructions.
The Homebrew website will ask you to open a terminal.
This can be done by pressing :kbd:`Command-Space` at the same time.
Then search for :menuselection:`Terminal` and press :kbd:`Enter`.

.. todo::
   Insert image of spotlight search for terminal. 

.. image:: /images/install/macos-package-managed-homebrew.png
    :width: 400
    :align: center

Please do *not* close the terminal once the installation script has finished.
A final step is missing which ensures that Homebrew gets added to the **PATH**.
At the last lines of the script it will ask you to copy, paste and run some code in the terminal. Please do this.
Press :kbd:`Enter` once you have pasted the code.
It should look similar to the following image, but might differ a little for different {{ macos }} versions.

.. image:: /images/install/macos-package-managed-homebrew-terminal-instructions.png
    :width: 400
    :align: center



Step 2: Install Miniconda and Python
-------------------------------------

Before starting on this step, please close the previously used terminal, and open up a new terminal (:kbd:`Command-Space`).

Then paste the following code in the terminal and press :kbd:`Enter`.

.. tip::
    You can copy and paste all code in the gray code blocks below by hovering your mouse over the block and pressing the icon in the top right.

.. code-block:: bash

    brew install --cask miniconda

Now run the following commands in terminal one at a time by pasting and pressing enter:

.. code-block:: bash

    conda install python=3.11 -y
    
.. code-block:: bash

    conda install -c conda-forge dtumathtools uncertainties -y
    


Step 3: Install Visual Studio Code 
-----------------------------------

Install Visual Studio Code by pasting the following in your terminal and pressing :kbd:`Enter`.

.. code-block:: bash

    brew install --cask visual-studio-code


Step 4: Install extensions for Visual Studio Code
-------------------------------------------------

.. |extensions| image:: /images/install/extensions.png
    :height: 25px


Finally you need to install some extensions in Visual Studio Code. This is done by pressing the
Extensions |extensions| button on the left side. Here search for ``Python``, and download the extensions. Make
sure that it is from Microsoft. Hereafter search for ``Jupyter``, and download that extension as
well. This also needs to be from Microsoft.

.. image:: /images/install/macos-package-managed-python.png
      :width: 200
      :align: center

.. image:: /images/install/macos-package-managed-jupyter.png
      :width: 200
      :align: center

.. tip::
    When you have finished the guide, we **strongly recommend** checking out the :ref:`Python Essentials <essentials-reference>` to prepare you for coding.


.. include:: verify.rst
