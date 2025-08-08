
Uninstalling Visual Studio Code
===================================

This guide will help you uninstall Visual Studio Code from your computer. 
This can be useful if Visual Studio Code is not working correctly and you want a fresh start.

1. Open :guilabel:`Finder`
2. Open the :guilabel:`Apps` folder
3. Find the :guilabel:`Visual Studio Code` App, right click and select move to :menuselection:`Trash`
4. Open :guilabel:`Trash` and press :menuselection:`Empty` in the top right hand corner.

.. note::

   This will leave behind some files, which you can delete manually if you want to. To do this follow the steps below.

* Open up a :ref:`terminal <learn-more.terminal>` and run the following command:

.. code-block:: bash

   rm -rf ~/.vscode
   rm -rf "~/Library/Application Support/Code"
