Jupyter Notebooks (.ipynb)
==========================

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



