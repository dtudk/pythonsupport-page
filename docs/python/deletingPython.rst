.. _Deleting multiple versions of python:

Deleting multiple versions of python
=========================================

If for some reason you wish to delete python from your computer, here is how you do it. 
This might be useful to do in a couple of scenarios:

1. Your current python installation is not working properly. 
2. You have several versions of python that conflict with each other. 
3. You have tried to install python, but something went wrong, and you want to start from scratch. 

=========================================
Deleting python on Windows
=========================================

1. Open the control panel.
2. Click on "Uninstall a program" under the "Programs" section.
3. Find python in the list of programs, and click on it.
4. Click on "Uninstall" at the top of the list.
5. Follow the instructions to uninstall python.
6. Repeat steps 3-5 for all versions of python that you have installed on your computer.

=========================================
Deleting python on Mac
=========================================

A version of Python comes pre-installed with macOs. This version of python is used by the operating system, and should not be deleted.
Other verions of Python may be deleted using the script below. This may include versions installed from the official python website, anaconda or miniconda. 

In order to run the script below you will need to download it. Afterwards open a terminal window and navigate to the folder where you downloaded the script. 
Then run the following command:

.. code-block:: bash

    bash deletePythonMac.sh

.. tip:: Place the script on your desktop. Then open a terminal window and type the following command: 'cd ~/Desktop'. Then run the script as described above. If this does not work check out: LINK TO HELP WITH TERMINAL

This will promt you for your system password. Enter it and press enter. The script will then delete all versions of python that you have installed on your computer.

:download:`Download script for deleting python: deletePythonMac.sh </_downloads/deletePythonMac.sh>`

.. note:: This will delete all versions of python that you have installed on your computer - including packages that you have installed using pip or conda install.

