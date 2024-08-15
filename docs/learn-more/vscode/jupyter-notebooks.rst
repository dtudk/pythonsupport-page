Jupyter Notebooks (.ipynb)
==========================


Creating a new Jupyter Notebook File
------------------------------------

.. card::
            
    #.
        Access the command palette by either pressing :kbd:`Command+Shift+P` on {{ macos }} or :kbd:`Ctrl+Shift+P`` in Windows or by clicking help in the menu bar at the top and then show all the commands from there on.

    #. 
        Search for create new Jupyter Notebook and click that option.

        .. image:: /learn-more/images/VSC-create-new-notebook.png
            :width: 400
            :align: center


    #. 
        Select a kernel by going to the upper right corner, clicking select kernel and then choosing the version of Python you want to use.

        .. image:: /learn-more/images/VSC-select-kernel.png
            :width: 100%
            :align: center

        .. note::

            You may have different versions of Python installed on your computer, and it is therefore very important to choose the version with the packages that you want to use for this project.

    .. tip::
        If you accidentally chose the wrong kernel, don't worry,you can always go back by clicking the Python version you're currently using and then changing it.


Importing packages
-------------------

.. card::

    #. 
        Start by clicking on the box in the top of the notebook


    #.
        Copy and paste the following code:
        
        .. code:: python

            import numpy as np

    #. 
       Press :kbd:`Shift+Enter` in order to execute the code from the box. A tick shows that the code from the specific box is executed 
       and the time next to it shows how long it took. You can also press the play button next to the box to execute the code. 

       In the rest of the document you will just have to write ``np.`` to use the functions from `numpy`_. Your screen should now look like the following image:

       .. image:: /learn-more/images/VSC-numpy-import.png
          :width: 100%
          :align: center




Creating a new code cell and running it
------------------------------------------


.. card::

    #. 
        Create a new code cell by hovering your mouse over an existing block and pressing the ``+ code`` option. 

        .. image:: /learn-more/images/VSC-codecell.png
             :width: 100%
             :align: center
        
        To delete a code cell one, you can just hover your mouse over the right corner of the box 
        and click on the trash shaped icon.

        .. image:: /learn-more/images/VSC-deletecell.png
             :width: 100%
             :align: center

    #.

        Copy and paste the following code which will multiplicate the square root of 2 and pi:
        
        .. code:: python

            print(np.sqrt(2) * np.pi)

    #. 

       Press shift+Enter in order to execute the code from the box (or press the play button). Below the code box you should see the following result.

       .. image:: /learn-more/images/VSC-numpyprint.png
                :width: 100%
                :align: center


       

Writing text using Markdown
----------------------------


.. card::

    #. 
        Add a Markdown box.
        
        .. image:: /learn-more/images/VSC-markdownadd.png
           :width: 100%
           :align: center
        
        You can use this option to write some text inside of your Jupyter Notebook using LaTeX. This is specially useful when you need
        to write complex mathematical equations.

    #. 
        Copy and paste the following code as an example in the Markdown box:
        
        .. code:: markdown

            $$ 5/10 = \frac{1}{2} $$ 
            
            This is my solution!

        .. image:: /learn-more/images/VSC-markdowntyping.png
            :width: 100%
            :align: center
        
    #. 
        Press :kbd:`Shift+Enter`. This should give you the following output:

        .. image:: /learn-more/images/VSC-markdownfinish.png
            :width: 100%
            :align: center    

        .. tip::

            To run your code inside a Jupyter Notebook, you can also use the ``Execute Cell``, ``Execute Above Cells``, 
            or ``Execute Cell and Below`` buttons.



Saving a File
--------------


.. card::
    
    .. tab-set::

        .. tab-item:: {{ windows }}

            1. Press the :menuselection:`File` button in the top left corner of VS Code.
            2. Select :menuselection:`Save` or :menuselection:`Save As...` from the dropdown menu.
            
            .. image:: ../images/VScode_windows_save_file.png
                :width: 450
                :align: center
                :alt: Save File in VS Code

            3. Choose a location and name for your file, then save it.

            Note that you can save a file by pressing :kbd:`Ctrl+S`.

        .. tab-item:: {{ macos }}

            1. Press the :menuselection:`File` button in the top left corner of your screen.
            2. Select :menuselection:`Save` or :menuselection:`Save As...` from the dropdown menu.
            3. Choose a location and name for your file, then save it.

            .. image:: ../images/saveFileMac.png
                :width: 450
                :align: center
                :alt: Save File in VS Code

            Note that you can save a file by pressing :kbd:`Command+S`.

    .. tip::

        You can also enable autosave by pressing the :menuselection:`File --> Auto save` button in the top left corner of VS Code.

