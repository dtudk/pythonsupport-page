.. _uninstall-conda:

Uninstalling Anaconda/Conda
===========================================

This guide will help you uninstall Anaconda from your computer. This can be useful if:

* You are trying to install packages with :ref:`pip`, but you cannot import the package.

* You want to change to use :ref:`pip`.

* You Generally have issues with packages.


Windows
-------------------------------------------

1. Open your terminal and run the following lines, one at a time

   .. code:: bash
       
       conda install anaconda-clean
       anaconda-clean --yes

   .. tip::
      In order to run the above command you need to be in the ``base`` environment.
      If it does not say ``(base)`` in the beginning of the line,
      run the following command:

      .. code:: bash
         
         conda activate base

2. Open your control panel, and press *Uninstall application*

3. Find all the applications regarding Anaconda (and Miniconda), right click on them and press *Uninstall*.


MacOS and Linux
-------------------------------------------

1. Open your terminal and run the following lines, one at a time

   .. code:: bash
       
       conda install anaconda-clean
       anaconda-clean --yes

   .. tip::
      In order to run the above command you need to be in the 'base' environment.
      If it does not say (base) in the beginning of the line,
      run the following command: ``conda activate base``

2. Then run the following three lines, one at a time

   .. code:: bash
       
       rm -rf anaconda3
       rm -rf ~/anaconda3
       rm -rf ~/opt/anaconda3

