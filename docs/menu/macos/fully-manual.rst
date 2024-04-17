.. _manual-reference-macOS:

MacOS - Manual installation guide
=======================================

.. note::
    Not using **MacOS**? The manual installation guide for **Windows** can be found :ref:`here <manual-reference-windows>`.
.. tip::
    You can copy and paste all code in the grey code blocks below by hovering your mouse over the block and pressing the icon in the top right.


.. _fully-manual-reference-mac:

Step 1: Install Miniconda
---------------------------

First thing you need to do is download Miniconda. This is done by going to `this website  <https://docs.anaconda.com/miniconda/index.html#latest-miniconda-installer-links>`_, and downloading the appropriate installer for your system.
Under the title "Latest Miniconda installer links", you will see different installers where you will have to download the correct one.
If you have an Intel processor you need to select Miniconda3 macOS Intel x86 64-bit pkg.
If you have an M processor you need to select Miniconda3 macOS Apple M1 64-bit pkg. Even if
you have an M2 or M3.

.. image:: /menu/images/macos-fully-manual-miniconda.png
    :width: 400
    :align: center


You can find out which processor you have by pressing the Apple logo an the top left of your
screen. Go to "About This Mac", and then under "Chip/Processor".

.. image:: /menu/images/macos-fully-manual-processor.png
    :width: 200
    :align: center


Then you need to follow the instructions from the package.

.. image:: /menu/images/macos-fully-manual-miniconda-pkg.png
    :width: 400
    :align: center


Step 2: Install Python
---------------------------

Now you need to open your terminal. This is done by pressing the "command" and "space" key at the same time and searching for "terminal".
Copy and paste the following lines of cod einto your terminal and press enter one line at a time:

.. code-block::
        
    conda install python=3.11 -y
    
.. code-block::

    conda install -c conda-forge dtumathtools uncertainties -y


Step 3: Install VS Code
----------------------------

.. |applications| image:: /menu/images/macos-applications.png
    :height: 25px

After the installation is finished, you need to download Visual Studio Code. This is done by going
to `this website  <https://code.visualstudio.com>`_. Click the download button and follow the instructions. 
Once downloaded make sure that the VSC app is under the |applications| folder in Finder.


.. image:: /menu/images/macos-fully-manual-vsc-webpage.png
      :width: 500
      :align: center


Step 4: Install extensions for Visual Studio Code
-------------------------------------------------

.. |extensions| image:: /menu/images/extensions.png
    :height: 25px


Open Visual Studio Code and select the Extensions |extensions| tab on the left. Here search for Python, and
download the extension. Make sure that it is from Microsoft. Hereafter search for Jupyter, and
download that extension as well. This also needs to be from Microsoft.


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

You are always welcome to visit us at our office hours, or contact us via email or Discord. More information can be found at our :ref:`homepage <reach-us-reference>`.