
Uninstalling Conda
===========================================

This guide will help you uninstall Conda from your computer. This can be useful if:

* You are trying to install packages with :ref:`pip`, but cannot import the package.

* You want to change to use :ref:`pip`.

* You have issues with packages.

* You already have the Anaconda distribution installed, but need to switch to Miniforge. 

* You already have the Miniconda distribution installed, but need to switch to Miniforge. 

* If you have installed Miniconda through Homebrew, run the following command line in the terminal:

  .. code-block:: bash
       
     brew remove miniconda

  .. tip::
      
     If you are unsure how you installed Miniconda, you can check by running the following command in your terminal. If the command returns ``miniconda``, it confirms that it was installed via Homebrew:
      
     .. code-block:: bash
      
        brew list | grep miniconda
      

* If you did not install Miniconda through Homebrew, you can remove it by running the following commands in your terminal:

  .. code-block:: bash
     
     conda activate
     conda init --reverse --all
     sudo rm -rf ~/miniconda3
     sudo rm -rf /opt/miniconda3
     rm -rf ${HOME}/.conda
     rm -f "${HOME}/.condarc"

* If you want to uninstall Anaconda, run the following commands in your terminal:

  .. code-block:: bash
      
     conda activate
     conda init --reverse --all
     sudo rm -rf ~/anaconda3
     sudo rm -rf /opt/anaconda3
     rm -rf ${HOME}/.conda
     rm -f "${HOME}/.condarc"

* If you want to uninstall Miniforge, run the following commands in your terminal:

  .. code-block:: bash
     
     conda activate
     conda init --reverse --all
     CONDA_BASE_ENVIRONMENT=$(conda info --base)
     rm -rf ${CONDA_BASE_ENVIRONMENT}
     rm -rf ${HOME}/.conda
     rm -f "${HOME}/.condarc"
