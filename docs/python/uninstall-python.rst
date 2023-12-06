.. _uninstall-python:


Python
=========================================

If for some reason you wish to delete Python from your computer, here is how you do it. 
This might be useful to do in a couple of scenarios:

1. Your current Python installation is not working properly. 
2. You have several versions of Python that conflict with each other. 
3. You have tried to install Python, but something went wrong, and you want to start from scratch. 


Deleting Python on Windows
-----------------------------------------

1. Open the control panel.
2. Click on *Uninstall a program* under the *Programs* section.
3. Find *Python* in the list of programs, and click on it.
4. Click on *Uninstall* at the top of the list.
5. Follow the instructions to uninstall Python.
6. Repeat steps 3-5 for all versions of Python that you have installed on your computer.


Deleting Python on Mac
-----------------------------------------

A version of Python comes pre-installed with {{macs}}. This version of Python is used by the operating system, and should not be deleted.
Other versions of Python may be deleted using a script supplied here.
This may include versions installed from the official Python website, anaconda or miniconda.

The deletion script can be :download:`downloaded here </_downloads/deletePythonMac.sh>`.
Be sure to place the downloaded script on your *Desktop*.

Once you have downloaded and placed on the *Desktop* open a terminal (:kbd:`Command + Space` then type ``terminal`` :kbd:`Enter`).

Then run the following command:

.. code-block:: bash

   cd ~/Desktop
   bash deletePythonMac.sh

The script will ask you for your system password. Enter it and press enter.
The script will then delete all versions of python that you have installed on your computer.

If this does not work check out :ref:`this page <os-terminal>`.

.. warning::
   This will delete all versions of Python that you have installed on your computer - including packages that you have installed using ``pip`` or ``conda install``.

