.. _Deleting Visual Studio Code:

Deleting Visual Studio Code
===========================================
This is a guide on how to uninstall Visual Studio Code from your computer.  
This can come in handy in many different scenarios, but especially if Visual Studio Code is not working properly, and you want a fresh start on it. 

===========================================
Deleting Visual Studio Code on Windows
===========================================
1. Open the control panel.
2. Click on "Uninstall a program" under the "Programs" section.
3. Find Visual Studio Code in the list of programs, and click on it.
4. Click on "Uninstall" at the top of the list.
5. Follow the instructions to uninstall VSC.

.. note::

   This will leave behind some files, which you can delete manually if you want to. To do this follow the steps below.

1. Press the Windows key and R at the same time.
2. Type in %appdata% and press enter.
3. Find the folder named "Code" and delete it.
4. Press the Windows key and R at the same time.
5. Type in %userprofile% and press enter.
6. Find the folder named ".vscode" and delete it.


===========================================
Deleting VSC on MacOS
===========================================
1. Open Finder
2. Open the Apps folder
3. Find the Visual Studio Code App, right click and select move to Trash
4. Open Trash and press Empty in the top right hand corner

.. note::

   This will leave behind some files, which you can delete manually if you want to. To do this follow the steps below.

* Open up a terminal 
* run the following command:

.. tab:: {{ macos }}

   .. code-block:: bash

      rm -rf ~/.vscode

* Finally run the following command:

.. tab:: {{ macos }}

   .. code-block:: bash

      rm -rf "~/Library/Application Support/Code"

