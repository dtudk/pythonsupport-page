.. _uninstall-conda:

Uninstalling Conda
===========================================

This guide will help you uninstall Conda from your computer. This can be useful if:

* You are trying to install packages with :ref:`pip`, but cannot import the package.

* You want to change to use :ref:`pip`.

* You have issues with packages.

* You already have the Anaconda distribution installed, but need to switch to Miniconda. 


{{ windows }}
-------------------------------------------

1. Ensure all shells, command prompts are closed i.e. make sure no files related to Anaconda/Miniconda are open anywhere.  

2. In the ``Search`` tab, search for **add or remove programs**.

3. Search for **conda**, click the three dots on the right hand side and click ``uninstall``

      .. image:: /images/install/conda_uninstall.png
         :width: 500
         :align: center

4. If you want to completely get rid of everything related to conda, make sure to tick off all the boxes in the last step of the uninstaller as shown below:

      .. image:: /images/install/conda_uninstall_last_step.png
         :width: 500
         :align: center


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
     
     conda activate
     conda init --reverse --all
     cd
     sudo rm -rf ~/miniconda3
     sudo rm -rf /opt/miniconda3


      

* If you want to uninstall Anaconda, run the following commands in your terminal:

  .. code:: bash
      
     
     conda activate
     conda init --reverse --all
     cd
     sudo rm -rf ~/anaconda3
     sudo rm -rf /opt/anaconda3


