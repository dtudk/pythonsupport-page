Visual Studio Code
========

.. note::
    If you are in your first year, you probably will not need to use VS Code until **week 7 or 8 of your studies**. Just remember that this page is here to get you started with some basic tips whenever you need. 

Similarly to the Idle, VS Code is a place to write your Python code. VS Code is great for larger projects. It is useful for things like debugging, organizing files and collaborating with other people for coding.
It also comes with extensions that can improve visual clarity, help you collaborate with 
others and a particularly useful type of file called Jupyter notebooks (These will be explained below). 





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

                .. tab-item:: MacOS 

                    Press the "File" button in the top left corner of your screen. Select "New File". Select "Python File" from the menu that drops down. 
                    You may need to hover your mouse around the top of the screen for the menu bar to appear

                    .. image:: images/VScode_mac1.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell



Selecting the right interpreter
------------------------------

.. card::

    

    Once you've created a python file you need to selecet your interpreter. In short, the interpreter is the version of Python that you use to execute your code.

    .. tab-set::
    
        .. tab-item:: Windows 

            1. Press "CTRL" + "Shift" +"p"
            2. type "Python: Select Interpreter" and press once this shows up under the options 

            .. image:: images/VScode_windows2.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

            3. Choose the option similar to "Python 3.11.5 ('base')" (You may have a different version of Python on your own PC)

            

            .. image:: images/VScode_windows3.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell


            .. tip::

                In VS Code, pressing "CTRL" + "Shift" +"p" brings down a search bar where you can search for anything you need help with

        .. tab-item:: MacOS

            1. Press "CMD" + "Shift" +"p"
            2. type "Python: Select Interpreter" and press once this shows up under the options 

            .. image:: images/VScode_mac2.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell
            3. Choose the option similar to "Python 3.11.5 ('base')" (You may have a different version of Python on your own PC)

            .. image:: images/VScode_mac3.png
                        :width: 450
                        :align: center
                        :alt: IDLE Shell

            .. tip::

                In VS Code, pressing "CMD" + "Shift" +"p" brings down a search bar where you can search for anything you need help with



.. tip::

    Once you've selected the right interpreter you can run all the code in your python file by clicking the icon shaped like a play button in the top right of VS Code.



Terminal in VS Code 
-------------------


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

                    Move your mouse to the top of the screen. Selcet "Terminal" followed by "New Terminal"

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
    *"Running cells with 'base (python 3.11.5)' requires the ipykernel package"*. 
    Simply click "install" and wait for the code to run  














