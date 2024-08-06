.. _package-managed-reference-macOS:


MacOS - Package managed installation guide
================================

.. note::
    Not using **MacOS**? A similar installation guide for **Windows** can be found :ref:`here <manual-reference-windows>`.

.. tip::
    You can copy and paste all code in the grey code blocks below by hovering your mouse over the block and pressing the icon in the top right.

Step 1: Install Homebrew 
--------------------------
First you need to download the package manager Homebrew. This is done by going to `this <https://brew.sh>`_ website
and follow the instructions. The Homebrew website will ask you to open a terminal. This is
done by pressing the "command" and "space" buttons at the same time and searching for terminal

.. image:: /menu/images/macos-package-managed-homebrew.png
    :width: 400
    :align: center

Be aware that Homebrew will need to be added to path. When the installation is done, it will ask
you to copy, paste and run some code in the terminal. Simply press enter once you have pasted the code.
It should look similar to the following image

.. image:: /menu/images/macos-package-managed-homebrew-terminal-instructions.png
    :width: 400
    :align: center


Step 2: Install Miniconda and Python
-------------------------------------

Once Homebrew has been installed, open your terminal and paste the following code and press
enter:

.. code-block::

    brew install --cask miniconda

Now run the following commands in terminal one at a time by inserting and pressing enter:

.. code-block::

    conda install python=3.11 -y
    
.. code-block::

    conda install -c conda-forge dtumathtools uncertainties -y
    


Step 3: Install VS Code 
--------------------------
After this you need to install Visual Studio Code. This is done by pasting the following in you
terminal and executing it:

.. code-block::

    brew install --cask visual-studio-code


Step 4: Install extensions for Visual Studio Code
-------------------------------------------------

.. |extensions| image:: /menu/images/extensions.png
    :height: 25px


Finally you need to install some extensions in Visual Studio Code. This is done by pressing the
Extensions |extensions| button on the left side. Here search for ``Python``, and download the extension. Make
sure that it is from Microsoft. Hereafter search for ``Jupyter``, and download that extension as
well. This also needs to be from Microsoft.

.. image:: /menu/images/macos-package-managed-python.png
      :width: 200
      :align: center

.. image:: /menu/images/macos-package-managed-jupyter.png
      :width: 200
      :align: center

.. tip::
    When you have finished the guide, we **strongly recommend** checking out the :ref:`Python Essentials <essentials-reference>` to prepare you for coding.

Verification and Quick Troubleshooting
---------------------------------------

* 
    Open up a terminal again. if you see (base) next to your username, you can proceed. Otherwise
    try to install miniconda again. Miniconda can be found on `this website  <https://docs.anaconda.com/miniconda/index.html#latest-miniconda-installer-links>`_. 
    For further information, see step 1 :ref:`here <fully-manual-reference-mac>`

* 

    Open up a terminal again and verify that you now see (base)

* 

    Finally type idle3 in a terminal and press Enter. This should open up a new window in which
    you will able to run python code

* 
    | now ensure the following:
    | It says Python 3.11.xx in the top left 
    | You get no errors when typing ``import dtumathtools, uncertainties`` and pressing enter. (nothing should happen)

* 
    If you do get an error for the above, try to paste the following line of code in a temrinal and pressing enter 

    .. code-block::

        conda install -c conda-forge python=3.11 dtumathtools uncertainties -y

* 
    open up idle3 again to verify. 



Supporter's Notes
-----------------
When writing your password in the terminal, it will not show that you are writing. Don't worry, you are writing, you just need to type your password and press enter, and it is all good. If you are in doubt, you can check out the video guide.

You are always welcome to visit us at our office hours, or contact us via email or Discord. More information can be found at our :ref:`homepage <reach-us-reference>`.