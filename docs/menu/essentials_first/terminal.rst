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


   .. tab-item:: {{ win_batch }}
      :sync: batch

      Search for ``cmd`` in the Windows taskbar search
      or press :kbd:`Win-R` buttons (simultaneously), then type
      ``cmd`` in the small run window appearing, press :kbd:`Enter`.
     
      This should open a **Terminal** looking *something* like this:

      .. image:: ../../os/gifs/CMD/terminal.gif
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


   .. tab-item:: {{ win_batch }}
      :sync: batch
      
      To launch Python using the Terminal, you can use ``python``.

      This should look *something* like this in your **Terminal**:
      
      .. image:: ../../os/gifs/CMD/openPython.gif
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

   .. tab-item:: {{ win_batch }}
      :sync: batch

      To exit Python in your Terminal you can use ``exit()``

      This should look *something* like this in your **Terminal**:

      .. image:: ../../os/gifs/CMD/exitPython.gif
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



Running a Python script using the Terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tab-set::

   .. tab-item:: {{ win_powershell }} 
      :sync: powershell
      
      To run a Python script using the terminal, you can use ``python`` + ``space`` + ``absolute path of your script``. 

      For example, if you wanted to run a script that has the absolute path ``C:\Users\python\test\helloWorld.py`` containing only the line ``print("Hello World")``, this should look *something* like this in your **Terminal**:
      
      .. image:: ../../os/gifs/PS/runPython.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ win_batch }}
      :sync: batch
      
      To run a Python script using the terminal, you can use ``python`` + ``space`` + ``absolute path of your script``. . 

      For example, if you wanted to run a script that has the absolute path ``C:\Users\python\test\helloWorld.py`` containing only the line ``print("Hello World")``, this should look *something* like this in your **Terminal**:
      
      .. image:: ../../os/gifs/CMD/runPython.gif
         :width: 100%
         :align: center
    

   .. tab-item:: {{ mac_bash }}
      :sync: MacOs/Unix
      
      To run a Python script using the terminal, you can use ``python`` + ``space`` + ``absolute path of your script``.

      For example, if you wanted to run a script that has the absolute path ``/Users/yourname/Desktop/helloWorld.py`` containing only the line ``print("Hello World")``, this should look *something* like this in your **Terminal**:
      
      .. image:: ../../os/gifs/Unix/runPython.gif
         :width: 100%
         :align: center
