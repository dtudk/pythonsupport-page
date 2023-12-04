.. _uninstall-conda:

Anaconda/Conda
===========================================

This is a guide on how to uninstall Anaconda from your computer.  It can help if you for example:

1. Are trying to install packages with :ref:`pip`, but you cant import the package.

2. Want to change to use :ref:`pip`.

3. Generally have issues with packages.


Windows
-------------------------------------------

1. Open your terminal and run the following lines, one at a time

   .. code-block:: bash
       
       conda install anaconda-clean
       anaconda-clean --yes

   .. tip::
      In order to run the above command you need to be in the ``base`` environment.
      If it does not say ``(base)`` in the beginning of the line,
      run the following command:

      .. code-block:: bash
         
         conda activate base

2. Open your control panel, and press uninstall application

3. Find all the applications regarding Anaconda, right click on the and press uninstall.


MacOS and Linux
-------------------------------------------

1. Open your terminal and run the following lines, one at a time

   .. code-block:: bash
       
       conda install anaconda-clean
       anaconda-clean --yes

   .. tip::
      In order to run the above command you need to be in the 'base' environment.
      If it does not say (base) in the beginning of the line,
      run the following command: ``conda activate base``

2. Then run the following three lines, one at a time

   .. code-block:: bash
       
       rm -rf anaconda3
       rm -rf ~/anaconda3
       rm -rf ~/opt/anaconda3

