.. _Deleting Visual Studio Code:


Uninstalling Visual Studio Code
===================================

This guide will help you uninstall Visual Studio Code from your computer. 
This can be useful if Visual Studio Code is not working properly and you want a fresh start.

Windows
---------------------------------------

1. Open the control panel.
2. Click on ``Uninstall a program`` under the ``Programs`` section.
3. Find Visual Studio Code in the list of programs, and click on it.
4. Click on ``Uninstall`` at the top of the list.
5. Follow the instructions to uninstall VS Code.

.. note::

   This will leave behind some files, which you can delete manually if you want to. To do this follow the steps below.

1. Press the :kbd:`Win+R` buttons at the same time.
2. Type in ``%appdata%`` and press :kbd:`Enter`.
3. Find the folder named ``Code`` and delete it.
4. Press the :kbd:`Win+R` buttons at the same time.
5. Type in ``%userprofile%`` and press :kbd:`Enter`.
6. Find the folder named ``.vscode`` and delete it.


MacOS
----------------------

1. Open Finder
2. Open the Apps folder
3. Find the Visual Studio Code App, right click and select move to :menuselection:`Trash`
4. Open Trash and press :menuselection:`Empty` in the top right hand corner

.. note::

   This will leave behind some files, which you can delete manually if you want to. To do this follow the steps below.

* Open up a terminal and run the following command:


.. code:: bash

   rm -rf ~/.vscode
   rm -rf "~/Library/Application Support/Code"

