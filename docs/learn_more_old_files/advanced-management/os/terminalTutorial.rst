.. _os-terminal-tutorial:

Terminal tutorial
==================

Welcome to the world of the Terminal! In this tutorial, you will learn the fundamentals of using the Terminal, 
a powerful tool for interacting with your computer through text commands. 
We will cover essential commands and tips to help you navigate and perform tasks efficiently.

You can learn more about what a Terminal is and the most useful commands :ref:`here <os-terminal>`.


.. _os-terminal-open:

Opening a terminal
^^^^^^^^^^^^^^^^^^

Each operating system opens terminals in a different way. 

.. tab-set::

   .. tab-item:: {{ win_powershell }}
      :sync: powershell

      Search for ``powershell`` in the Windows taskbar search or 
      press :kbd:`Win-R` buttons (simultaneously), then type
      ``powershell`` in the small run window appearing, press :kbd:`Enter`.

      This should open a **Terminal** looking *something* like this:

      .. image:: ../../../os/gifs/PS/terminal.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ win_batch }}
      :sync: batch

      Search for ``cmd`` in the Windows taskbar search
      or press :kbd:`Win-R` buttons (simultaneously), then type
      ``cmd`` in the small run window appearing, press :kbd:`Enter`.
     
      This should open a **Terminal** looking *something* like this:

      .. image:: ../../../os/gifs/CMD/terminal.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ mac_bash }}
      :sync: bash

      Open the Launchpad icon in the Dock, or press :kbd:`Command-Space`; type ``Terminal`` and click on it.

      See more detailed explanation `here <https://support.apple.com/en-gb/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac>`__.
      
      This should open a **Terminal** looking *something* like this:

      .. image:: ../../../os/gifs/Unix/terminal.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ linux_bash }}
      :sync: bash

      **Note**: This depends on the distribution you are using. Nearly all Linux distributions
      has the Terminal icon near the Desktop.

      Try one of the following options:

      1. Press :kbd:`Ctrl-Alt-T` simultaneously.
      2. Press the :kbd:`Win` key which should open up a search box, type
         ``terminal`` and press :kbd:`Enter`
      3. Open a file explorer and right-click a folder,
         there should be an option name ``Open in Terminal`` which will open that
         folder in the terminal.

      This should open a **Terminal** looking *something* like this:   

      .. image:: ../../../os/gifs/Unix/terminal.gif
         :width: 100%
         :align: center


.. _os-terminal-pwd:

1. Where am I?
^^^^^^^^^^^^^^

.. tab-set::

   .. tab-item:: {{ win_powershell }} 
      :sync: powershell
         
      To find out your current directory (location), you can use the 
      ``pwd`` command on Windows. 

      1. Type and enter ``pwd`` in your Terminal.

      This should look *something* like this in your **Terminal**:
      
      .. image:: ../../../os/gifs/PS/pwd.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ win_batch }} 
      :sync: batch
      
      To find out your current directory (location), you can use the  
      ``cd`` command on Windows. 

      1. Type and enter ``cd`` in your Terminal.

      This should look *something* like this in your **Terminal**:
      
      .. image:: ../../../os/gifs/CMD/currentDir.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ unix_bash }}
      :sync: bash

      To find out your current directory (location), you can use the 
      ``pwd`` command on Unix-based systems (Linux or macOS).

      1. Type and enter ``pwd`` in your Terminal.

      This should look *something* like this in your **Terminal**:
         
      .. image:: ../../../os/gifs/Unix/pwd.gif
         :width: 100%
         :align: center


.. _os-terminal-ls:

2. What's in here?
^^^^^^^^^^^^^^^^^^^


.. tab-set::

   .. tab-item:: {{ win_powershell }} 
      :sync: powershell

      To list the contents of your current directory in PowerShell, you can use the ``ls`` cmdlet. 
      If you want to see only files and not directories, use ``ls -Force``. 
      

      1. Type and enter in your Terminal:
      ``ls``

      2. Type and enter in your Terminal:
      ``ls -Force``

      This should look *something* like this in your **Terminal**:

      .. image:: ../../../os/gifs/PS/ls.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ win_batch }}
      :sync: batch

      To list the contents of your current directory in Windows Command Prompt, you can use the ``dir`` command. If you want to see hidden files and directories as well, use ``dir /a``. 
      

      1. Type and enter in your Terminal:
      ``dir``

      2. Type and enter in your Terminal:
      ``dir /a``

      This should look *something* like this in your **Terminal**:

      
      .. image:: ../../../os/gifs/CMD/dir.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ unix_bash }}
      :sync: bash

      To list the contents of your current directory, you can use the ``ls`` command. 
      If you want to see hidden files as well, use ``ls -a``.  
      

      1. Type and enter in your Terminal:
      ``ls``

      2. Type and enter in your Terminal:
      ``ls -a``

      This should look *something* like this in your **Terminal**:

      
      .. image:: ../../../os/gifs/Unix/ls.gif
         :width: 100%
         :align: center


.. _os-terminal-cd:

3. Changing directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tab-set::

   .. tab-item:: {{ win_powershell }} 
      :sync: powershell
      
      **Warning 1**:
      Note that instead of ``MyFolder`` you should use one of the folders listed in the previous exercise.

      **Warning 2 (for Windows)**:
      Note when typing the directory name of subfolders, that Windows uses backslashes ``\`` and **not** forward slashes ``/``

      To navigate to a different directory, you can use the ``cd`` command followed by the path to the desired 
      directory, and to navigate one step backwards, you can use the ``cd ..`` command.

      1. Type and enter in your Terminal: ``cd MyFolder``
      
      2. Type and enter in your Terminal: ``cd ..``
      
      This should look *something* like this in your **Terminal**:
      
      .. image:: ../../../os/gifs/PS/cd.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ win_batch }}
      :sync: batch

      **Warning 1**:
      Note that instead of ``MyFolder`` you should use one of the folders listed in the previous exercise.

      **Warning 2 (for Windows)**:
      Note when typing the directory name of subfolders, that windows uses backslashes ``\`` and NOT forward slashes ``/``

      To navigate to a different directory, you can use the ``cd`` command followed by the path to the desired 
      directory, and to navigate one step backwards, you can use the ``cd ..`` command.

      1. Type and enter in your Terminal: ``cd MyFolder``
      
      2. Type and enter in your Terminal: ``cd ..``
      
      This should look *something* like this in your **Terminal**:
      
      .. image:: ../../../os/gifs/CMD/cd.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ unix_bash }}
      :sync: bash

      **Warning**:
      Note that instead of ``MyFolder`` you should use one of the folders listed in the previous exercise.

      To navigate to a different directory, you can use the ``cd`` command followed by the path to the desired 
      directory, and to navigate one step backwards, you can use the ``cd ..`` command.

      1. Type and enter in your Terminal: ``cd MyFolder``
      
      2. Type and enter in your Terminal: ``cd ..``

      This should look *something* like this in your **Terminal**:
      
      .. image:: ../../../os/gifs/Unix/cd.gif
         :width: 100%
         :align: center
      


A good trick to use in Visual Studio Code is to open a folder in your sidebar, and copy the names of folders/directories that you would like to work in. This is done by completing the steps below:

#. Press the icon in the top left of the screen that looks like 2 pieces of paper on top of each other
#. Press "open folder"
#. Visual studio code will now open your files. Select the folder that you would like to work with by clicking on it
#. Now you should see all the files and subfolders contained in the folder taht you selected on the left side of the screen
#. You can now right click a folder and press "copy path"
#. type cd in your terminal and paste the path that you just copied 

In general it is a good idea to change your directory, to the place of whatever you are working with. For example, if a large dataset is in a specific folder, you can change your directory to that folder. 


.. _os-terminal-mkdir:

4. How can I create a new folder?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tab-set::

   .. tab-item::  {{ win_powershell }} 
      :sync: powershell

      To create a new folder you can use ``mkdir`` on your Terminal. Then, you can use ``ls`` to see 
      if the folder was successfully created.

      1. Type and enter in your Terminal: ``mkdir NewPythonFolder``

      2. Type and enter in your Terminal: ``ls``

      This should look *something* like this in your **Terminal**:

      
      .. image:: ../../../os/gifs/PS/mkdir.gif
         :width: 100%
         :align: center  


   .. tab-item:: {{ win_batch }}
      :sync: batch

      To create a new folder you can use ``mkdir`` on your Terminal. Then, you can use ``dir`` to see 
      if the folder was successfully created.
      
      1. Type and enter in your Terminal: ``mkdir NewPythonFolder``

      2. Type and enter in your Terminal: ``dir``

      This should look *something* like this in your **Terminal**:
      
      .. image:: ../../../os/gifs/CMD/mkdir.gif
         :width: 100%
         :align: center    


   .. tab-item:: {{ unix_bash }}
      :sync: bash

      To create a new folder you can use ``mkdir`` on your Terminal. Then, you can use ``ls`` to see 
      if the folder was successfully created.
      
      1. Type and enter in your Terminal: ``mkdir NewPythonFolder``

      2. Type and enter in your Terminal: ``ls``

      This should look *something* like this in your **Terminal**:

      
      .. image:: ../../../os/gifs/Unix/mkdir.gif
         :width: 100%
         :align: center


.. _os-terminal-rm:

5. How can I delete a folder or a file using a Terminal?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. tab-set::

   .. tab-item::  {{ win_powershell }} 
      :sync: powershell

      You can use ``rm`` to delete a file or ``rm -r`` to delete a folder using the Terminal. 

      1. Type and enter in your Terminal: ``rm -r NewPythonFolder``

      2. Type and enter in your Terminal: ``ls``

      This should look *something* like this in your **Terminal**:

      
      .. image:: ../../../os/gifs/PS/rm.gif
         :width: 100%
         :align: center

   .. tab-item:: {{ win_batch }}
      :sync: batch
      
      You can use ``del`` to delete a file or ``rmdir /s`` to delete a folder using the Terminal. 

      1. Type and enter in your Terminal: ``rmdir /s NewPythonFolder``

      2. Type and enter in your Terminal: ``dir``

      This should look *something* like this in your **Terminal**:

      
      .. image:: ../../../os/gifs/CMD/rmdir.gif
         :width: 100%
         :align: center



   .. tab-item:: {{ unix_bash }}
      :sync: bash

      You can use ``rm`` to delete a file or ``rm -r`` to delete a folder using the Terminal. 

      1. Type and enter in your Terminal: ``rm -r NewPythonFolder``

      2. Type and enter in your Terminal: ``ls``

      This should look *something* like this in your **Terminal**:   

      
      .. image:: ../../../os/gifs/Unix/rm.gif
         :width: 100%
         :align: center


.. _os-terminal-python-version:

6. Which Python version?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tab-set::

   .. tab-item::  {{ win_powershell }} 
      :sync: powershell

      To check which Python version you have you can use ``python --version``

      To enter Python in your Terminal you can use ``python``

      To exit Python in your Terminal you can use ``exit()``

      1. Type and enter in your Terminal: ``python --version`` 

      2. Type and enter in your Terminal: ``python``

      3. Type and enter in your Terminal: ``exit()``
      

      This should look *something* like this in your **Terminal**:
      
      .. image:: ../../../os/gifs/PS/python.gif
         :width: 100%
         :align: center

   .. tab-item:: {{ win_batch }}
      :sync: batch

      To check which Python version you have you can use ``python --version``

      To enter Python in your Terminal you can use ``python``

      To exit Python in your Terminal you can use ``exit()``

      1. Type and enter in your Terminal: ``python --version`` 

      2. Type and enter in your Terminal: ``python``

      3. Type and enter in your Terminal: ``exit()``
      

      This should look *something* like this in your **Terminal**:

      .. image:: ../../../os/gifs/CMD/python.gif
         :width: 100%
         :align: center



   .. tab-item:: {{ unix_bash }}
      :sync: bash

      To check which Python version you have you can use ``python3 --version``

      **Note that this might change depending 
      whether you have more than one Python version installed**

      To enter Python in your Terminal you can use ``python3``

      To exit Python in your Terminal you can use ``exit()``

      1. Type and enter in your Terminal: ``python3 --version`` 

      2. Type and enter in your Terminal: ``python3``

      3. Type and enter in your Terminal: ``exit()``
      

      This should look *something* like this in your **Terminal**:

      .. image:: ../../../os/gifs/Unix/python.gif
         :width: 100%
         :align: center


.. _os-terminal-pip-list:

7. Which packages do I have? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. tab-set::

   .. tab-item:: {{ win_powershell }} 
      :sync: powershell
      
      To see which packages you currently have in Python, you can use ``pip list``. 

      This should look *something* like this in your **Terminal**:
      
      .. image:: ../../../os/gifs/PS/pip.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ win_batch }}
      :sync: batch
      
      To see which packages you currently have in Python, you can use ``pip list``. 

      This should look *something* like this in your **Terminal**:
      
      .. image:: ../../../os/gifs/CMD/pip.gif
         :width: 100%
         :align: center
    

   .. tab-item:: {{ unix_bash }}
      :sync: bash
      
      To see which packages you currently have in Python, you can use ``pip3 list``. 

      This should look *something* like this in your **Terminal**:
      
      .. image:: ../../../os/gifs/Unix/pip.gif
         :width: 100%
         :align: center
