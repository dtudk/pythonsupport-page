.. _manual-reference-macos:

MacOS - Manual installation
=======================================

.. button-ref:: manual-reference-windows
    :ref-type: ref
    :color: info

    Not using **MacOS**? Press here for **Windows** guides.

.. todo::
    Change color?

.. _fully-manual-reference-mac:

Step 1: Install Miniconda
---------------------------


The first thing to do is to download Miniconda.
This is done by going to `this website <https://docs.anaconda.com/miniconda/index.html#latest-miniconda-installer-links>`__, and downloading the appropriate installer for your system.
Under the title ``Latest Miniconda installer links``, you will see different installers where you will have to download the correct one.

* If you have an Intel processor you need to select Miniconda3 MacOS Intel x86 64-bit pkg.
* If you have an **M** processor you need to select Miniconda3 MacOS Apple M1 64-bit pkg. *Even* if you have an **M2** or **M3**.

.. image:: /images/install/macos-fully-manual-miniconda.png
    :width: 400
    :align: center


You can find out which processor you have by pressing the Apple logo an the top left of your
screen. Go to :menuselection:`About This Mac --> Chip/Processor`.

.. image:: /images/install/macos-fully-manual-processor.png
    :width: 200
    :align: center


Then you need to follow the instructions from the package.

.. image:: /images/install/macos-fully-manual-miniconda-pkg.png
    :width: 400
    :align: center


Step 2: Install Python
---------------------------

Now you need to open your terminal. This is done by pressing the "command" and "space" key at the same time, and searching for "terminal".

.. todo::
    Insert image of spotlight search for terminal.

Copy and paste the following lines of code into your terminal and press enter one line at a time:

.. tip::
    You can copy and paste all code in the gray code blocks below by hovering your mouse over the block and pressing the icon in the top right.

.. code-block:: bash
        
    conda install python=3.11 -y
    
.. code-block:: bash

    conda install -c conda-forge dtumathtools uncertainties -y


Step 3: Install Visual Studio Code
-----------------------------------

.. |applications| image:: /images/install/macos-applications.png
    :height: 25px

After the installation is finished, you need to download Visual Studio Code. This is done by going
to `this website  <https://code.visualstudio.com>`_. Click the download button and follow the instructions. 
Once downloaded make sure that Visual Studio Code is under the |applications| folder in Finder.


.. image:: /images/install/macos-fully-manual-vsc-webpage.png
      :width: 500
      :align: center


Step 4: Install extensions for Visual Studio Code
-------------------------------------------------

.. |extensions| image:: /images/install/extensions.png
    :height: 25px


Open Visual Studio Code and select the Extensions |extensions| tab on the left. Here search for Python, and
download the extension. Make sure that it is from Microsoft. Hereafter search for Jupyter, and
download that extension as well. This also needs to be from Microsoft.


.. image:: /images/install/macos-package-managed-python.png
      :width: 200
      :align: center

.. image:: /images/install/macos-package-managed-jupyter.png
      :width: 200
      :align: center

.. tip::
    When you have finished the guide, we **strongly recommend** checking out the :ref:`Python Essentials <essentials-reference>` to prepare you for coding.


.. include:: verify.rst
