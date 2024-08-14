Jupyter Notebooks (.ipynb)
==========================


Creating a new Jupyter Notebook File
------------------------------------

.. card::
            
    #.
        Access the command palette by either pressing command+shift+P on Mac or control+shift+P in Windows or by clicking help in the menu bar at the top and then show all the commands from there on.

    #. 
        Search for create new Jupyter Notebook and click that option.


    #. 
        Select a kernel by going to the upper right corner, clicking select kernel and then choosing the version of Python you want to use.

            PICTURE!!! 

        Note: You may have different versions of Python installed on your computer, and it's therefore very important to choose the version with the packages that you want to use for this project.

    .. tip::
        If you accidentally chose the wrong kernel, don't worry,you can always go back by clicking the Python version you're currently using and then changing it.


Importing packages
-------------------

.. card::

    #. 
    
        Click on the first box.

        PICTURE!!!

    #.

        Copy and paste the following code:
        
        .. code-block:: bash

            important numpy as np

    #. 

       Press shift+Enter in order to execute the code from the box. A tick shows that the code from the specific box is executed 
       and the time next to it shows how long it took.

       In the rest of the document you will just have to write ``np.`` to use the functions from NumPy.


Creating a new code box and running it
---------------------------------------


.. card::

    #. 
    
        Create a new code box by hovering your mouse over an existing box and pressing the plus code. 
        

        PICTURE!!!
        
        If you to delete one, you can just hover your mouse over the right corner of the box 
        and click on the trash.

        PICTURE!!!


    #.

        Copy and paste the following code which will multiplicate the square root of 2 and pi:
        
        .. code-block:: bash

            np.sqrt(2)*np.pi

    #. 

       Press shift+Enter in order to execute the code from the box. Below the code box you should see the result.

       PICTURE!!!!

       




Writing text using Markdown
----------------------------


.. card::

    #. 
        
        Add a Markdown box.

        PICTURE!!!

        You can use this option to write some text inside of your Jupyter Notebook using LaTeX. This is specially useful when you need
        to write complex mathematical equations.

    #. 

        Copy and paste the following code as an example in the Markdown box:
        
        .. code-block:: bash

            $$ 5/10 = \frac{1}{2} $$ 
            
            This is my solution!

        
    #. 

        Press shift+Enter. This should give you the following output:

            PICTURE!!!    

        .. tip::

            To run your code inside a Jupyter Notebook, you can also use the ``Execute Cell``, ``Execute Above Cells``, 
            or ``Execute Cell and Below`` buttons.



Saving a File
--------------


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

