.. _Deleting Anaconda:

Deleting Anaconda
===========================================
This is a guide on how to uninstall Anaconda from your computer.  It can help if you for example:

1. Are trying to install packages with pip, but you cant import the package.

2. Want to change to use pip.

3. Generally have issues with packages.

===========================================
Windows
===========================================

1. Open your terminal and run the following line

.. code-block:: bash
    
    conda install anaconda-clean

2.  Open your controlpanel, and press uninstall application

3. Find all the applications regarding Anaconda, right click on the and press uninstall.

===========================================
MacOs and Linux
===========================================

1. Open your terminal and run the following line

.. code-block:: bash
    
    conda install anaconda-clean

2. Then run the following three lines, one at a time

.. code-block:: bash
    
    rm -rf anaconda3

.. code-block:: bash

    rm -rf ~/anaconda3
    
.. code-block:: bash

    rm -rf ~/opt/anaconda3

