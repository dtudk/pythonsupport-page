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
First you need to download the package manager Homebrew. This is done by going to `this website <https://brew.sh>`_ and follow the instructions. The Homebrew website will ask you to open a terminal. This is done by pressing the "command" and "space" buttons at the same time and searching for terminal.

.. todo::
   Insert image of spotlight search for terminal. 

.. image:: /images/install/macos-package-managed-homebrew.png
    :width: 400
    :align: center

Be aware that Homebrew will need to be added to **PATH**. When the installation is done, it will ask
you to copy, paste and run some code in the terminal. Simply press enter once you have pasted the code.
It should look similar to the following image, but might differ a little for different masOS versions.

.. image:: /images/install/macos-package-managed-homebrew-terminal-instructions.png
    :width: 400
    :align: center


It is VERY important that you close or restart your terminal after installing HomeBrew. 

Step 2: Install Miniconda and Python
-------------------------------------
Once Homebrew has been installed and you have RESTARTED your terminal, paste the following code in your terminal and press enter. 

.. tip::
    You can copy and paste all code in the grey code blocks below by hovering your mouse over the block and pressing the icon in the top right.

.. code-block:: bash

    brew install --cask miniconda

Now run the following commands in terminal one at a time by pasting and pressing enter:

.. code-block:: bash

    conda install python=3.11 -y
    
.. code-block:: bash

    conda install -c conda-forge dtumathtools uncertainties -y
    


Step 3: Install VS Code 
--------------------------
After this you need to install Visual Studio Code. This is done by pasting the following in your
terminal and pressing enter:

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


Verification and Quick Troubleshooting
--------------------------------------
Open up a terminal again. if you see ``(base)`` next to your username, you can proceed. Otherwise
try to install miniconda again. Miniconda can be found on `this website  <https://docs.anaconda.com/miniconda/index.html#latest-miniconda-installer-links>`_. 
For further information, see step 1 :ref:`here <fully-manual-reference-mac>`.

.. todo::
    Insert image of the terminal with ``(base)`` next to the username

Make sure that it says ``(base)`` next to your user name when opening the terminal.

Finally type ``idle3`` in the terminal and press enter. This should open up a new window in which you will able to run Python code.

Now ensure the following:

• It says Python 3.11.xx in the top left.
• You get no errors when typing ``import dtumathtools, uncertainties`` and press enter. This should open a new line without any text, as shown bellow.

.. todo::
    Insert image of ``idle3`` after import dtumathtools and uncertainties so they can see what it should look like.


If it is not the case for one of the above, try to paste the following line of code in the terminal and press enter:

.. code-block:: bash

     conda install -c conda-forge python=3.11 dtumathtools uncertainties -y


If you are still having trouble or have any questions please do not hesitate to visit us at our office hours, or contact us via email or Discord. More information can be found at our :ref:`homepage <reach-us-reference>`.
