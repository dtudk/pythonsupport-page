Visual Studio Code
===================

.. note::
    If you are in your first year, you probably will not need to use VS Code until **week 7 or 8 of your studies**. Just remember that this page is here to get you started with some basic tips whenever you need. 

Similarly to IDLE, VS Code is a place to write your Python code. VS Code is great for larger projects. It is useful for things like debugging, organizing files and collaborating with other people for coding.
It also comes with extensions that can improve visual clarity, help you collaborate with 
others and a particularly useful type of file called Jupyter notebooks. 


Opening a Folder in VS Code
------------------------

.. card::

    Opening a folder in VS Code allows you to manage all your project files in one place.

    .. tab-set::

        .. tab-item:: Windows

            1. Press the "File" button in the top left corner of VS Code.
            2. Select "Open Folder..." from the dropdown menu.

            .. image:: images/NEEDS-TO-BE-CREATED.png
                :width: 450
                :align: center
                :alt: Open Folder in VS Code

            3. Browse to the folder you want to open and select it.


        .. tab-item:: MacOS

            1. Press the "File" button in the top left corner of your screen.
            2. Select "Open Folder..." from the dropdown menu.

            .. image:: images/openFolderMac.png
                :width: 450
                :align: center
                :alt: Open Folder in VS Code

            3. Browse to the folder you want to open and select it.    


Creating a Python-file
-----------------------

.. card::      
    

    You can create a Python file in VS code. This is useful if you are writing code that you will need again. 

    .. tab-set::

                .. tab-item:: Windows 

                    Press the "File" button in the top left corner of VS Code. Select "New File". Select "Python File" from the menu that drops down. 

                    .. image:: images/VScode_windows1.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

                    Note that you can also use the Explorer to create a new File or Folder by using the top left side of VS Code:

                    .. image:: images/createFileUsingLeftBar.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell


                .. tab-item:: MacOS 

                    Press the "File" button in the top left corner of your screen. Select "New File". Select "Python File" from the menu that drops down. 
                    You may need to hover your mouse around the top of the screen for the menu bar to appear

                    .. image:: images/VScode_mac1.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

                    Note that you can also use the Explorer to create a new File or Folder by using the top left side of VS Code:

                    .. image:: images/createFileUsingLeftBar.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

                        

Saving a File
-----------

.. card::

    Saving a file in VS Code ensures that your work is not lost and can be accessed later.

    .. tab-set::

        .. tab-item:: Windows

            1. Press the "File" button in the top left corner of VS Code.
            2. Select "Save" or "Save As..." from the dropdown menu.
            
            .. image:: images/VScode_windows_save_file.png
                :width: 450
                :align: center
                :alt: Save File in VS Code
            3. Choose a location and name for your file, then save it.

            Note that you can save a file by pressing "control" + "s".

        .. tab-item:: MacOS

            1. Press the "File" button in the top left corner of your screen.
            2. Select "Save" or "Save As..." from the dropdown menu.
            3. Choose a location and name for your file, then save it.

            .. image:: images/saveFileMac.png
                :width: 450
                :align: center
                :alt: Save File in VS Code

            Note that you can save a file by pressing "command" + "s".

    .. tip::

        You can also autosave by pressing the "File" button in the top left corner of VS Code and then selecting "Auto save".

Opening a File in VS Code
----------------------

.. card::

    Opening a file in VS Code allows you to edit and run your code directly within the editor.

    .. tab-set::

        .. tab-item:: Windows

            1. Press the "File" button in the top left corner of VS Code.
            2. Select "Open..." from the dropdown menu.

            .. image:: images/NEEDS-TO-BE-CREATED.png
                :width: 450
                :align: center
                :alt: Open File in VS Code


            3. Browse to the file you want to open and select it.

            

        .. tab-item:: MacOS

            1. Press the "File" button in the top left corner of your screen.
            2. Select "Open..." from the dropdown menu.

            .. image:: images/openFileMac.png
                :width: 450
                :align: center
                :alt: Open File in VS Code

            3. Browse to the file you want to open and select it.    

    .. tip::

        You can also open a file by dragging and dropping it directly into the VS Code window.


Selecting the right interpreter
-------------------------------

.. card::

    Once you've created a Python file you need to select your interpreter. In short, the interpreter is the version of Python that you use to execute your code.

    .. tab-set::
    
        .. tab-item:: Windows 

            1. Press "CTRL" + "Shift" +"p"
            2. Type "Python: Select Interpreter" and press once this shows up under the options 

            .. image:: images/VScode_windows2.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

            3. Choose the option similar to "Python 3.11.5 ('base')". You may have a different version of Python on your own PC.

            

            .. image:: images/VScode_windows3.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell


            .. tip::

                In VS Code, pressing "CTRL" + "Shift" +"p" brings down a search bar where you can search for anything you need help with.

        .. tab-item:: MacOS

            1. Press "CMD" + "Shift" +"p"
            2. type "Python: Select Interpreter" and press once this shows up under the options 

            .. image:: images/VScode_mac2.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell
                        
            3. Choose the option similar to "Python 3.11.5 ('base')". You may have a different version of Python on your own PC.

            .. image:: images/VScode_mac3.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

            .. tip::

                In VS Code, pressing "CMD" + "Shift" +"p" brings down a search bar where you can search for anything you need help with



.. tip::

    Once you've selected the right interpreter you can run all the code in your python file by clicking the icon shaped like a play button in the top right of VS Code.


Run a Python File - Needs to be redone according to video
----------------------------------------------------------------

.. card::

    Once you've written your Python code, you can easily run it in VS Code.

    .. tab-set::

        .. tab-item:: Windows

            1. Open the Python file you want to run.
            2. Press "CTRL" + "Shift" +"p".
            3. Type "Run Python File in Terminal" and select it from the options.
            4. Alternatively, you can click the play button icon in the top right corner of the VS Code window.

            .. image:: images/VScode_windows_run_python.png
                :width: 450
                :align: center
                :alt: Run Python File in VS Code

        .. tab-item:: MacOS

            1. Open the Python file you want to run.
            2. Press "CMD" + "Shift" +"p".
            3. Type "Run Python File in Terminal" and select it from the options.
            4. Alternatively, you can click the play button icon in the top right corner of the VS Code window.

            .. image:: images/VScode_mac_run_python.png
                :width: 450
                :align: center
                :alt: Run Python File in VS Code

    .. tip::

        Running your Python file in VS Code allows you to see the output directly in the terminal, making it easier to debug and test your code.


Difference between Terminal and Python shell in VS Code - Needs to be redone according to video
------------------------------------------------------------------------------------------------------------------------


.. card::      
    

    You can start a terminal from VS code, which works just like in the terminal app. 

    .. tab-set::

                .. tab-item:: Windows 

                    Press the three dots in the top menu bar. They are next to the "View" and "Go" options. Move your mouse to "Terminal" and click "New Terminal"

                    .. image:: images/VScode_windows4.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

                .. tab-item:: MacOS 

                    Move your mouse to the top of the screen. Select "Terminal" followed by "New Terminal"

                    .. image:: images/VScode_mac4.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

.. tip::
    You can have multiple terminals open at once. 
    You can delete a terminal by hovering your mouse over it's name (bottom right) and pressing the icon shaped like a trash can



Jupyter Notebooks
-----------------

Jupyter notebooks give you a way to combine Python code, and plain text similar to a word document. 

.. card:: Creating a Jupyter notebook

    .. tab-set::

                .. tab-item:: Windows 

                    1. Press "CTRL" + "Shift" + "p"
                    2. Search for "Create: New Jupyter Notebook" and press

                    .. image:: images/VScode_windows5.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

                    3. Press the "Select Kernel" button in the top right of the notebook
                    4. Click "Python Environments" and "3.11.5 ('base') (You may have a different version of Python on your own PC)"

                    .. image:: images/VScode_windows6.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell
                    
                    .. warning::
                        If the "Create: New Jupyter notebook" option does not pop up, you need to install the Jupyter extension for VS Code. This is easily done by
                        pressing "CTRL" + "Shift" + "X", searching for "Jupyter" and pressing install
                        when Jupyter pops up. If it is still not working, open a terminal, type "pip install jupyter", 
                        press "Enter" and wait for jupyter to be installed. You may need to restart VS Code

                .. tab-item:: MacOS 

                    1. Press "CMD" + "Shift" + "p"
                    2. Search for "Create: New Jupyter Notebook" and press

                    .. image:: images/VScode_mac5.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

                    3. Press the "Select Kernel" button in the top right of the notebook
                    4. Click "Python Environments" and "3.11.5 ('base') (You may have a different version of Python on your own PC)"

                    .. image:: images/VScode_mac6.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

                    .. warning::
                        If the "Create: New Jupyter notebook" option does not pop up, you need to install the Jupyter extension for VS Code. This is easily done by
                        pressing "CMD" + "Shift" + "X", searching for "Jupyter" and pressing install
                        when Jupyter pops up. If it is still not working, open a terminal, type "pip3 install jupyter", 
                        press "Enter" and wait for jupyter to be installed. You may need to restart VS Code




.. card:: Code blocks and Text Blocks

    If you hover your mouse around the top of the notebook two icons will appear. "+ Code" and "+ Markdown".
    Press "+ Code" to create a code block.

    .. image:: images/VScode_windows7.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

    You can execute the code in a block by pressing the play-button next to the code block or pressing "Shift"+"Enter".

    .. image:: images/VScode_windows8.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

    Markdown cells allow you to type plain text. Running these cells will just print the plain text. 
    You can finish the markdown cell by pressing "Shift" + "Enter"

    .. image:: images/VScode_windows9.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell



    You can create more blocks of either code or markdown by hovering your mouth below any code or markdown cell. 



.. warning:: 
    If it is your first time creating a notebook, running a code block may give you the following error:
    *"Running cells with 'base (Python 3.11.5)' requires the ipykernel package"*. 
    Simply click "install" and wait for the code to run  














