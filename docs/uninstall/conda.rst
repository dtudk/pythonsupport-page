.. _uninstall-conda:

Uninstalling Conda
===========================================

This guide will help you uninstall Conda from your computer. This can be useful if:

* You are trying to install packages with :ref:`pip`, but cannot import the package.

* You want to change to use :ref:`pip`.

* You have issues with packages.


{{ windows }}
-------------------------------------------

1. Open your terminal and run the following lines, one at a time

   .. code:: pwsh
       
       conda install anaconda-clean
       anaconda-clean --yes

   .. tip::
      To run the above command you need to be in the ``base`` environment.
      If it does not say ``(base)`` at the beginning of the line,
      run the following command:

      .. code:: pwsh
         
         conda activate base

2. Open your control panel, and press :guilabel:`Uninstall application`.

3. Please find all the applications regarding Anaconda (and Miniconda), right click on them and press :guilabel:`Uninstall`.


{{ macos }} and Linux
-------------------------------------------

* If you have installed Miniconda through Homebrew, run the following command line in the terminal:

  .. code:: bash
       
     brew remove miniconda

  .. tip::
      
     If you are unsure how you installed Miniconda, you can check by running the following command in your terminal. If the command returns ``miniconda``, it confirms that it was installed via Homebrew:
      
     .. code:: bash
      
        brew list | grep miniconda
      

* If you did not install Miniconda through Homebrew, you can remove it by running the following commands in your terminal:

  .. code:: bash
       
     rm -rf miniconda3
     rm -rf ~/miniconda3
     rm -rf ~/opt/miniconda3

* If you want to uninstall Anaconda, run the following commands in your terminal:

  .. code:: bash
       
     rm -rf anaconda3
     rm -rf ~/anaconda3
     rm -rf ~/opt/anaconda3

