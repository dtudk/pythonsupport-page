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

      .. image:: /os/gifs/PS/terminal.gif
         :width: 100%
         :align: center



   .. tab-item:: {{ mac_bash }}
      :sync: bash

      Open the Launchpad icon in the Dock, or press :kbd:`Command-Space`; type ``Terminal`` and click on it.

      See more detailed explanation `here <https://support.apple.com/en-gb/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac>`__.
      
      This should open a **Terminal** looking *something* like this:

      .. image:: /os/gifs/Unix/terminal.gif
         :width: 100%
         :align: center



Opening Python in a Terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tab-set::

   .. tab-item:: {{ win_powershell }} 
      :sync: powershell
      
      To launch Python using the Terminal, you can use ``python``. 

      This should look *something* like this in your **Terminal**:
      
      .. image:: /os/gifs/PS/openPython.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ mac_bash }}
      :sync: bash
      
      To launch Python using the Terminal, you can use ``python3``.

      This should look *something* like this in your **Terminal**:
      
      .. image:: /os/gifs/Unix/openPython.gif
         :width: 100%
         :align: center


Exiting Python in a Terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tab-set::

   .. tab-item::  {{ win_powershell }} 
      :sync: powershell

      To exit Python in your Terminal you can use ``exit()``
      
      This should look *something* like this in your **Terminal**:
      
      .. image:: /os/gifs/PS/exitPython.gif
         :width: 100%
         :align: center



   .. tab-item:: {{ mac_bash }}
      :sync: MacOs

      To check which Python version you have you can use ``python3 --version``

      **Note that this might change depending 
      whether you have more than one Python version installed**

      To exit Python in your Terminal you can use ``exit()``

      This should look *something* like this in your **Terminal**:

      .. image:: /os/gifs/Unix/exitPython.gif
         :width: 100%
         :align: center



Running a Python script in the Terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tab-set::

   .. tab-item:: {{ win_powershell }} 
      :sync: powershell
      
      To run a Python script using the terminal, you can use ``python`` + ``space`` + ``absolute path of your script``. 

      For example, if you wanted to run a script that has the absolute path ``C:\Users\python\test\helloWorld.py`` containing only the line ``print("Hello World")``, this should look *something* like this in your **Terminal**:
      
      .. image:: /os/gifs/PS/runPython.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ mac_bash }}
      :sync: MacOs/Unix
      
      To run a Python script using the terminal, you can use ``python3`` + ``space`` + ``absolute path of your script``.

      For example, if you wanted to run a script that has the absolute path ``/Users/yourname/Desktop/helloWorld.py`` containing only the line ``print("Hello World")``, this should look *something* like this in your **Terminal**:
      
      .. image:: /os/gifs/Unix/runPython.gif
         :width: 100%
         :align: center

Printing Working Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. card::

   .. tab-set::

      .. tab-item:: Windows

         Use the command ``pwd`` to print your current working directory. This tells you where in your file system, the terminal is operating.

         .. image:: /os/gifs/PS/pwd.gif
            :width: 100%
            :align: center
         
      .. tab-item:: MacOS

         Use the command ``pwd`` to print your current working directory. This tells you where in your file system, the terminal is operating.

         .. image:: /os/gifs/Unix/pwd.gif
            :width: 100%
            :align: center

Seeing What is in a Directory 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. card::

   .. tab-set::

      .. tab-item:: Windows

         Use the command ``ls`` to print everything in the current working directory 

         .. image:: /os/gifs/PS/ls.gif
            :width: 100%
            :align: center
         
      .. tab-item:: MacOS

         Use the command ``ls`` to print everything in the current working directory 

         .. image:: /os/gifs/Unix/ls.gif
            :width: 100%
            :align: center
   
Changing Directories
^^^^^^^^^^^^^^^^^^^^^^

.. card::

   .. tab-set::

      .. tab-item:: Windows

         | The command ``cd`` can be used to change your directory. For example one could write 
         | ``cd MyFolder`` in order to move to the a folder named ``MyFolder``
         | The command ``cd .. `` can be used to move backwards by one directory.

         .. image:: /os/gifs/PS/cd.gif
            :width: 100%
            :align: center

         
      .. tab-item:: MacOS

         | The command ``cd`` can be used to change your directory. For example one could write 
         | ``cd MyFolder`` in order to move to the a folder named ``MyFolder``
         | The command ``cd .. `` can be used to move backwards by one directory

         .. image:: /os/gifs/Unix/cd.gif
            :width: 100%
            :align: center


Creating a Folder
^^^^^^^^^^^^^^^^^^

.. card::

   .. tab-set::

      .. tab-item:: Windows

         Use ``mkdir`` followed by the desired name of a new folder to create a new folder in the current working directory. For example ``mkdir NewPythonFolder`` will create a new folder with the name ``NewPythonFolder`` in the current working directory


         .. image:: /os/gifs/PS/mkdir.gif
            :width: 100%
            :align: center  
      
      .. tab-item:: MacOS

         Use ``mkdir`` followed by the desired name of a new folder to create a new folder in the current working directory. For example ``mkdir NewPythonFolder`` will create a new folder with the name ``NewPythonFolder`` in the current working directory


         .. image:: /os/gifs/Unix/mkdir.gif
            :width: 100%
            :align: center  

Removing a Folder 
^^^^^^^^^^^^^^^^^

.. card:: 

   .. tab-set::

      .. tab-item:: Windows

         | ``rm -r`` followed by a folder name, will remove the given folder.
         | For example ``rm -r NewPythonFolder`` will remove the folder named ``NewPythonFolder``

         .. image:: /os/gifs/PS/rm.gif
            :width: 100%
            :align: center
         
      .. tab-item:: MacOS

         | ``rm -r`` followed by a folder name, will remove the given folder.
         | For example ``rm -r NewPythonFolder`` will remove the folder named ``NewPythonFolder``

         .. image:: /os/gifs/Unix/rm.gif
            :width: 100%
            :align: center

Clearing output
^^^^^^^^^^^^^^^

.. card::

   .. tab-set::

      .. tab-item:: Windows

         ``clear`` will clear all output from the terminal

         
      .. tab-item:: MacOS

         ``clear`` will clear all output from the terminal

   





