Terminal
===================================


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

      .. image:: ../../os/gifs/PS/terminal.gif
         :width: 100%
         :align: center



   .. tab-item:: {{ mac_bash }}
      :sync: bash

      Open the Launchpad icon in the Dock, or press :kbd:`Command-Space`; type ``Terminal`` and click on it.

      See more detailed explanation `here <https://support.apple.com/en-gb/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac>`__.
      
      This should open a **Terminal** looking *something* like this:

      .. image:: ../../os/gifs/Unix/terminal.gif
         :width: 100%
         :align: center



Opening Python in a Terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tab-set::

   .. tab-item:: {{ win_powershell }} 
      :sync: powershell
      
      To launch Python using the Terminal, you can use ``python``. 

      This should look *something* like this in your **Terminal**:
      
      .. image:: ../../os/gifs/PS/openPython.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ mac_bash }}
      :sync: bash
      
      To launch Python using the Terminal, you can use ``python3``.

      This should look *something* like this in your **Terminal**:
      
      .. image:: ../../os/gifs/Unix/openPython.gif
         :width: 100%
         :align: center


Exiting Python in a Terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tab-set::

   .. tab-item::  {{ win_powershell }} 
      :sync: powershell

      To exit Python in your Terminal you can use ``exit()``
      
      This should look *something* like this in your **Terminal**:
      
      .. image:: ../../os/gifs/PS/exitPython.gif
         :width: 100%
         :align: center



   .. tab-item:: {{ mac_bash }}
      :sync: MacOs

      To check which Python version you have you can use ``python3 --version``

      **Note that this might change depending 
      whether you have more than one Python version installed**

      To exit Python in your Terminal you can use ``exit()``

      This should look *something* like this in your **Terminal**:

      .. image:: ../../os/gifs/Unix/exitPython.gif
         :width: 100%
         :align: center



Running a Python script in the Terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tab-set::

   .. tab-item:: {{ win_powershell }} 
      :sync: powershell
      
      To run a Python script using the terminal, you can use ``python`` + ``space`` + ``absolute path of your script``. 

      For example, if you wanted to run a script that has the absolute path ``C:\Users\python\test\helloWorld.py`` containing only the line ``print("Hello World")``, this should look *something* like this in your **Terminal**:
      
      .. image:: ../../os/gifs/PS/runPython.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ mac_bash }}
      :sync: MacOs/Unix
      
      To run a Python script using the terminal, you can use ``python3`` + ``space`` + ``absolute path of your script``.

      For example, if you wanted to run a script that has the absolute path ``/Users/yourname/Desktop/helloWorld.py`` containing only the line ``print("Hello World")``, this should look *something* like this in your **Terminal**:
      
      .. image:: ../../os/gifs/Unix/runPython.gif
         :width: 100%
         :align: center


.. card:: Printing Working Directory

   Use the command ``pwd`` to print your current working directory. This tells you where in your file system, the terminal is operating.


.. card:: Seeing What is in a Directory 

   Use the command ``ls`` to print everything in the current working directory 

.. card:: Changing Directories

   | The command ``cd`` can be used to change your directory. For example one could write 
   | ``cd .\Desktop`` in order to move to the desktop


.. card:: Moving Backwards

   The command ``cd ..\`` will move you backwards by one directory. For example, if a folder named ``sub-folder`` is inside a folder nambed ``parent-folder`` and the current working directory is ``sub-folder``, using ``cd ..\`` will take you back to ``parent-folder``

.. card:: Creating a folder

   Use ``mkdir`` followed by the desired name of a new folder to create a new folder in the current working directory. For example ``mkdir new_folder`` will create a new folder with the name ``new-folder``


.. card:: Removing a Folder 

   | ``rm -r`` followed by a folder name, will remove the given folder.
   | For example ``rm -r new_folder`` will remove the folder named ``new_folder``

.. card:: Clearing output

   ``clear`` will clear all output from the terminal





