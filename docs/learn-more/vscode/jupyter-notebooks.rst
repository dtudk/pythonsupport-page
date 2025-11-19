Jupyter Notebooks (.ipynb)
==========================


.. dropdown:: Video Tutorial
   :color: muted
   :open:

   .. raw:: html 
      
         <iframe src="https://panopto.dtu.dk/Panopto/Pages/Embed.aspx?id=e2325323-ea37-4216-bdf8-b1ce00b63fcf" height="405" width=100% style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>


A ``.ipynb`` file is a notebook file that contains Python code intermixed with
`Markdown text <https://en.wikipedia.org/wiki/Markdown>`__.

It works similar to other *cell-based* execution models. For example, individual segments
of the notebook can be executed in arbitrary order.

In this tutorial you will learn how to do all of these using Visual Studio Code:

.. contents::
   :local:
   :depth: 2


Creating a new Jupyter Notebook File
------------------------------------

.. card::
            
    #.
        Access the command palette by pressing :kbd:`Command+Shift+P` ({{ macos }}) or :kbd:`Ctrl+Shift+P` ({{ windows }})
        or by clicking :menuselection:`Help` in the menu bar at the top, and then all the commands are shown

    #. 
        Search for create new Jupyter Notebook and click that option.

        .. image:: /learn-more/images/VSC-create-new-notebook.png
            :width: 400
            :align: center

    #. 
        You can select a kernel by going to the upper right corner, clicking :menuselection:`Select Kernel`, and then choosing the version of Python you want to use.

        .. image:: /learn-more/images/VSC-select-kernel.png
            :width: 100%
            :align: center

        .. note::

            You may have different versions of Python installed on your computer, so it is very important to choose the version with the packages you want to use for this project.

    .. tip::
        If you accidentally choose the wrong kernel, don't worry, you can always go back by clicking the Python version you're currently using and then changing it.


Importing packages
-------------------

.. card::

    #. 
        Start by clicking on the first cell at the top of the notebook

    #.
        Copy and paste the following code:
        
        .. code-block:: python

            import numpy as np

    #. 
       Press :kbd:`Shift+Enter` to execute the code from the cell. A tick shows that the code from the specific cell is executed 
       and the time next to it shows how long it took. Alternatively, you can press the play button next to the cell to execute the code. 

       In the rest of the document you will have to write ``np.`` to use `numpy`_ functions. Your screen should look like the following image:

       .. image:: /learn-more/images/VSC-numpy-import.png
          :width: 100%
          :align: center



Creating a new code cell and running it
------------------------------------------


.. card::

    #. 
        Create a new code cell by hovering your mouse over an existing block (near the border) and pressing the :menuselection:`+ Code` option. 

        .. image:: /learn-more/images/VSC-codecell.png
             :width: 100%
             :align: center
        
        To delete a code cell, first ensure it is activated, then you can hover your mouse over the right corner of the cell 
        and click on the trash shaped icon.

        .. image:: /learn-more/images/VSC-deletecell.png
             :width: 100%
             :align: center

    #.
        Copy and paste the following code which will multiply the square root of 2 and pi:
        
        .. code-block:: python

            print(np.sqrt(2) * np.pi)

    #. 
       Press :kbd:`Shift+Enter` in order to execute the code from the cell (or press the play button). Below the code box you should see the following result.

       .. image:: /learn-more/images/VSC-numpyprint.png
                :width: 100%
                :align: center


       
Writing text using Markdown
----------------------------

.. card::

    #. 
        Create a new markdown cell by hovering your mouse over an existing block (near the border) and pressing the :menuselection:`+ Markdown` option. 
        
        .. image:: /learn-more/images/VSC-markdownadd.png
           :width: 100%
           :align: center
        
        You can use this option to write some text inside of your Jupyter Notebook using LaTeX. This is especially useful when you need
        to write complex mathematical equations.

    #. 
        Copy and paste the following code as an example in the Markdown cell:
        
        .. code-block:: markdown

            $$ 5/10 = \frac{5}{10} $$ 
            
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
      :sync-group: os

      .. tab-item:: {{ windows }}
         :sync: windows

         1. Press the :menuselection:`File` button in the top left corner of VS Code.
         2. Select :menuselection:`Save` or :menuselection:`Save As...` from the dropdown menu.
         
            .. image:: ../images/VScode_windows_save_file.png
               :width: 450
               :align: center
               :alt: Save File in VS Code

         3. Please choose a location and name for your file, then save it.

         .. tip::
            You can save a file by pressing :kbd:`Ctrl+S`.

      .. tab-item:: {{ macos }}
         :sync: mac

         1. Press the :menuselection:`File` button in the top left corner of your screen.
         2. Select :menuselection:`Save` or :menuselection:`Save As...` from the dropdown menu.
         3. Please choose a location and name for your file, then save it.

            .. image:: ../images/saveFileMac.png
                :width: 450
                :align: center
                :alt: Save File in VS Code

         .. tip::
            You can save a file by pressing :kbd:`Command+S`.

   .. tip::

      You can enable auto save by pressing the
      :menuselection:`File --> Auto Save` button in the top left corner of VS Code.

