.. _install-python-ny:

Setting up python 
=================

.. tip:: 
   We suggest removing any pre-installed Python versions and VS Code before 
   proceeding with this guide to ensure a smooth installation process.
   For help with this process, take a look at the section on `Deleting multiple versions of python <Deleting multiple versions of python>`_.



**Download & Installation**

   .. note:: 
       For the time being, we recommend **not** downloading the newest python release (3.12).

   .. tab:: {{ windows }}

       - For a hassle-free Python download & installation experience, we recommend grabbing it straight from the `Microsoft Store <https://www.microsoft.com/store/productid/9NRWMJP3717K?ocid=pdpshare>`_.
     
       - However, if you find yourself on an adventurous detour and can't access it there, you can still opt for the `official Python release <https://www.python.org/downloads/release/python-3116/>`_ -- **Just remember to check the Add Python to PATH box (at the bottom of the installation GUI)**.

      .. warning::
          If you did not download python through Microsoft Store, then you need to make sure 
          that you check the "Add to path" box during the installation. 

      .. image:: images/python-win-step-1.png
          :width: 600px
          :align: center
          :alt: Add to path checkbox


   .. tab:: {{ macos }}

       - You can download the official python directly from `here <https://www.python.org/downloads/release/python-3116/>`_.
         After downloading the installer, the installation process should be relatively straightforward. 


Verifying installation
======================

To verify if python is installed correctly follow the steps below:  

.. tab:: {{ windows }}

    1. Give your keyboard's window key a friendly nudge.  
    2. Type ``powershell`` in the search bar, and hit enter to launch PowerShell.
    3. In the powershell window, type ``python --version``
    4. If you spot the ``Python x.xx.x`` smiling back at you, you're all set! You've got a python in your machine |:snake:|.  

.. tab:: {{ macos }} 

    1. Give your keyboard's ``Command`` key a friendly nudge.
    2. Type ``terminal`` in the search bar, and press Enter to open Terminal.
    3. In the Terminal window, type ``python3 --version``
    4. If you see the ``Python x.xx.x`` smiling back at you, you're all set! You've got a Python friend on your machine |:snake:|.

======================
Conda installation 
======================
If you wish to use a conda installation in order to run python, please go :ref:`here <install-conda>`.

.. note ::
    DTU recommends using the official python release (and pip). However, some courses might require you to use conda. Please check your course page for more information.