Python files (.py)
===================

A .py file is a text file that contains Python code. 
It's the standard file format used for writing and executing Python programs. 
When you write Python code in a .py file, you can run the file to execute the code it contains,
and it can be opened and edited in any text editor or integrated development environment (IDE) like VS Code or IDLE.

In this tutorial you will learn how to do all of these using Visual Studio Code:

- Open a Folder.
- Create a Python File.
- Save a Python File.
- Open File.
- Select right interpreter.
- Run a File.
- Difference between Terminal and Python Shell.


Opening a Folder
------------------

Opening a folder in VS Code allows you to manage all your project files in one place.

.. card::


    .. tab-set::

        .. tab-item:: Windows

            1. Press the "File" button in the top left corner of VS Code.
            2. Select "Open Folder..." from the dropdown menu.

            .. image:: ../images/NEEDS-TO-BE-CREATED.png
                :width: 450
                :align: center
                :alt: Open Folder in VS Code

            3. Browse to the folder you want to open and select it.


        .. tab-item:: MacOS

            1. Press the "File" button in the top left corner of your screen.
            2. Select "Open Folder..." from the dropdown menu.

            .. image:: ../images/openFolderMac.png
                :width: 450
                :align: center
                :alt: Open Folder in VS Code

            3. Browse to the folder you want to open and select it.    


Creating a Python-file
-----------------------

You can create a Python file in VS code. This is useful if you are writing code that you will need again. 

.. card::      
    

    .. tab-set::

                .. tab-item:: Windows 

                    Press the "File" button in the top left corner of VS Code. Select "New File". Select "Python File" from the menu that drops down. 

                    .. image:: ../images/VScode_windows1.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

                    Note that you can also use the Explorer to create a new File or Folder by using the top left side of VS Code:

                    .. image:: ../images/createFileUsingLeftBar.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell


                .. tab-item:: MacOS 

                    Press the "File" button in the top left corner of your screen. Select "New File". Select "Python File" from the menu that drops down. 
                    You may need to hover your mouse around the top of the screen for the menu bar to appear

                    .. image:: ../images/VScode_mac1.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

                    Note that you can also use the Explorer to create a new File or Folder by using the top left side of VS Code:

                    .. image:: ../images/createFileUsingLeftBar.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

                        

Saving a File
--------------

Saving a file in VS Code ensures that your work is not lost and can be accessed later.

.. card::
    
    .. tab-set::

        .. tab-item:: Windows

            1. Press the "File" button in the top left corner of VS Code.
            2. Select "Save" or "Save As..." from the dropdown menu.
            
            .. image:: ../images/VScode_windows_save_file.png
                :width: 450
                :align: center
                :alt: Save File in VS Code
            3. Choose a location and name for your file, then save it.

            Note that you can save a file by pressing "control" + "s".

        .. tab-item:: MacOS

            1. Press the "File" button in the top left corner of your screen.
            2. Select "Save" or "Save As..." from the dropdown menu.
            3. Choose a location and name for your file, then save it.

            .. image:: ../images/saveFileMac.png
                :width: 450
                :align: center
                :alt: Save File in VS Code

            Note that you can save a file by pressing "command" + "s".

    .. tip::

        You can also autosave by pressing the "File" button in the top left corner of VS Code and then selecting "Auto save".

Opening a File
---------------------------

Opening a file in VS Code allows you to edit and run your code directly within the editor.

.. card::


    .. tab-set::

        .. tab-item:: Windows

            1. Press the "File" button in the top left corner of VS Code.
            2. Select "Open..." from the dropdown menu.

            .. image:: ../images/NEEDS-TO-BE-CREATED.png
                :width: 450
                :align: center
                :alt: Open File in VS Code


            3. Browse to the file you want to open and select it.

            

        .. tab-item:: MacOS

            1. Press the "File" button in the top left corner of your screen.
            2. Select "Open..." from the dropdown menu.

            .. image:: ../images/openFileMac.png
                :width: 450
                :align: center
                :alt: Open File in VS Code

            3. Browse to the file you want to open and select it.    

    .. tip::

        You can also open a file by dragging and dropping it directly into the VS Code window.


Selecting the right interpreter
-------------------------------

Once you've created a Python file you need to select your interpreter. In short, the interpreter is the version of Python that you use to execute your code.

.. card::

    .. tab-set::
    
        .. tab-item:: Windows 

            1. Press "CTRL" + "Shift" +"p"
            2. Type "Python: Select Interpreter" and press once this shows up under the options 

            .. image:: ../images/VScode_windows2.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

            3. Choose the option similar to "Python 3.11.5 ('base')". You may have a different version of Python on your own PC.

            

            .. image:: ../images/VScode_windows3.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell


            .. tip::

                In VS Code, pressing "CTRL" + "Shift" +"p" brings down a search bar where you can search for anything you need help with.

        .. tab-item:: MacOS

            1. Press "CMD" + "Shift" +"p"
            2. type "Python: Select Interpreter" and press once this shows up under the options 

            .. image:: ../images/VScode_mac2.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell
                        
            3. Choose the option similar to "Python 3.11.5 ('base')". You may have a different version of Python on your own PC.

            .. image:: ../images/VScode_mac3.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

            .. tip::

                In VS Code, pressing "CMD" + "Shift" +"p" brings down a search bar where you can search for anything you need help with



.. tip::

    Once you've selected the right interpreter you can run all the code in your python file by clicking the icon shaped like a play button in the top right of VS Code.


Run a Python File - Needs to be redone according to video
----------------------------------------------------------------

Once you've written your Python code, you can easily run it in VS Code.

.. card::

   

    .. tab-set::

        .. tab-item:: Windows

            1. Open the Python file you want to run.
            2. Press "CTRL" + "Shift" +"p".
            3. Type "Run Python File in Terminal" and select it from the options.
            4. Alternatively, you can click the play button icon in the top right corner of the VS Code window.

            .. image:: ../images/VScode_windows_run_python.png
                :width: 450
                :align: center
                :alt: Run Python File in VS Code

        .. tab-item:: MacOS

            1. Open the Python file you want to run.
            2. Press "CMD" + "Shift" +"p".
            3. Type "Run Python File in Terminal" and select it from the options.
            4. Alternatively, you can click the play button icon in the top right corner of the VS Code window.

            .. image:: ../images/VScode_mac_run_python.png
                :width: 450
                :align: center
                :alt: Run Python File in VS Code

    .. tip::

        Running your Python file in VS Code allows you to see the output directly in the terminal, making it easier to debug and test your code.


Difference between Terminal and Python shell in VS Code - Needs to be redone according to video
------------------------------------------------------------------------------------------------------------------------

You can start a terminal from VS code, which works just like in the terminal app. 

.. card::      
    

    

    .. tab-set::

                .. tab-item:: Windows 

                    Press the three dots in the top menu bar. They are next to the "View" and "Go" options. Move your mouse to "Terminal" and click "New Terminal"

                    .. image:: ../images/VScode_windows4.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

                .. tab-item:: MacOS 

                    Move your mouse to the top of the screen. Select "Terminal" followed by "New Terminal"

                    .. image:: ../images/VScode_mac4.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

.. tip::
    You can have multiple terminals open at once. 
    You can delete a terminal by hovering your mouse over it's name (bottom right) and pressing the icon shaped like a trash can



