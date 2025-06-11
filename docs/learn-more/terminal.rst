.. _learn-more.terminal:

Terminal
===================================

.. dropdown:: Video Tutorial
   :open:
   :color: muted

   .. tab-set::

      .. tab-item:: {{windows}}

         .. raw:: html

            <iframe src="https://panopto.dtu.dk/Panopto/Pages/Embed.aspx?id=b581660d-9d46-4142-91fd-b1ce00897b4d" height="405" width=100% style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

      .. tab-item:: {{macos}}

         .. raw:: html

            <iframe src="https://panopto.dtu.dk/Panopto/Pages/Embed.aspx?id=b6c29370-cf95-493c-8c02-b1ce00897b51" height="405" width=100% style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>



.. _learn-more-open-terminal:

Opening a terminal
^^^^^^^^^^^^^^^^^^

Each operating system opens terminals in a different way.

.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      Search for ``powershell`` in the Windows taskbar search or
      press :kbd:`Win+R` buttons (simultaneously), then type
      ``powershell`` in the small run window appearing, press :kbd:`Enter`.

      This should open a **Terminal** looking *something* like this:

      .. image:: /os/gifs/PS/terminal.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ macos }}
      :sync: mac

      Open the Launchpad icon in the Dock, or press :kbd:`Command+Space`; type ``Terminal`` and click on it.

      See more detailed explanation `here <https://support.apple.com/en-gb/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac>`__.

      This should open a **Terminal** looking *something* like this:

      .. image:: /os/gifs/Unix/terminal.gif
         :width: 100%
         :align: center



Opening Python in a Terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      To launch Python using the Terminal, you can use ``python``.

      This should look *something* like this in your **Terminal**:

      .. image:: /os/gifs/PS/openPython.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ macos }}
      :sync: mac

      To launch Python using the Terminal, you can use ``python3``.

      This should look *something* like this in your **Terminal**:

      .. image:: /os/gifs/Unix/openPython.gif
         :width: 100%
         :align: center


Exiting Python in a Terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      To exit Python in your Terminal you can use ``exit()``

      This should look *something* like this in your **Terminal**:

      .. image:: /os/gifs/PS/exitPython.gif
         :width: 100%
         :align: center



   .. tab-item:: {{ macos }}
      :sync: mac

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
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      To run a Python script using the terminal, you can use ``python`` + ``space`` + ``absolute path of your script``.

      For example, if you wanted to run a script that has the absolute path ``C:\Users\python\test\helloWorld.py`` containing only the line ``print("Hello World")``, this should look *something* like this in your **Terminal**:

      .. image:: /os/gifs/PS/runPython.gif
         :width: 100%
         :align: center


   .. tab-item:: {{ macos }}
      :sync: mac

      To run a Python script using the terminal, you can use ``python3`` + ``space`` + ``absolute path of your script``.

      For example, if you wanted to run a script that has the absolute path ``/Users/yourname/Desktop/helloWorld.py`` containing only the line ``print("Hello World")``, this should look *something* like this in your **Terminal**:

      .. image:: /os/gifs/Unix/runPython.gif
         :width: 100%
         :align: center


Printing Working Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. card::

   .. tab-set::
      :sync-group: os

      .. tab-item:: {{ windows }}
         :sync: windows

         Use the command ``pwd`` to print your current working directory. This tells you where in your file system, the terminal is operating.

         .. image:: /os/gifs/PS/pwd.gif
            :width: 100%
            :align: center

      .. tab-item:: {{ macos }}
         :sync: mac

         Use the command ``pwd`` to print your current working directory. This tells you where in your file system, the terminal is operating.

         .. image:: /os/gifs/Unix/pwd.gif
            :width: 100%
            :align: center

Seeing What is in a Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. card::

   .. tab-set::
      :sync-group: os

      .. tab-item:: {{ windows }}
         :sync: windows

         Use the command ``ls`` to print everything in the current working directory

         .. image:: /os/gifs/PS/ls.gif
            :width: 100%
            :align: center

      .. tab-item:: {{ macos }}
         :sync: mac

         Use the command ``ls`` to print everything in the current working directory

         .. image:: /os/gifs/Unix/ls.gif
            :width: 100%
            :align: center

Changing Directories
^^^^^^^^^^^^^^^^^^^^^^

.. card::

   .. tab-set::
      :sync-group: os

      .. tab-item:: {{ windows }}
         :sync: windows

         The command ``cd`` can be used to change your directory. For example one could write
         ``cd MyFolder`` in order to move to the folder named ``MyFolder``
         The command ``cd ..`` can be used to move backwards by one directory.

         .. image:: /os/gifs/PS/cd.gif
            :width: 100%
            :align: center


      .. tab-item:: {{ macos }}
         :sync: mac

         The command ``cd`` can be used to change your directory. For example one could write
         ``cd MyFolder`` in order to move to the a folder named ``MyFolder``
         The command ``cd ..`` can be used to move backwards by one directory

         .. image:: /os/gifs/Unix/cd.gif
            :width: 100%
            :align: center


Creating a Folder
^^^^^^^^^^^^^^^^^^

.. card::

   .. tab-set::
      :sync-group: os

      .. tab-item:: {{ windows }}
         :sync: windows

         Use ``mkdir`` followed by the desired name of a new folder to create a new folder in the current working directory. For example ``mkdir NewPythonFolder`` will create a new folder with the name ``NewPythonFolder`` in the current working directory


         .. image:: /os/gifs/PS/mkdir.gif
            :width: 100%
            :align: center

      .. tab-item:: {{ macos }}
         :sync: mac

         Use ``mkdir`` followed by the desired name of a new folder to create a new folder in the current working directory. For example ``mkdir NewPythonFolder`` will create a new folder with the name ``NewPythonFolder`` in the current working directory


         .. image:: /os/gifs/Unix/mkdir.gif
            :width: 100%
            :align: center

Removing a Folder
^^^^^^^^^^^^^^^^^

.. card::

   .. tab-set::
      :sync-group: os

      .. tab-item:: {{ windows }}
         :sync: windows

         | ``rm -r`` followed by a folder name, will remove the given folder.
         | For example ``rm -r NewPythonFolder`` will remove the folder named ``NewPythonFolder``

         .. image:: /os/gifs/PS/rm.gif
            :width: 100%
            :align: center

      .. tab-item:: {{ macos }}
         :sync: mac

         | ``rm -r`` followed by a folder name, will remove the given folder.
         | For example ``rm -r NewPythonFolder`` will remove the folder named ``NewPythonFolder``

         .. image:: /os/gifs/Unix/rm.gif
            :width: 100%
            :align: center

Clearing output
^^^^^^^^^^^^^^^

.. card::

   .. tab-set::
      :sync-group: os

      .. tab-item:: {{ windows }}
         :sync: windows

         ``clear`` will clear all output from the terminal


      .. tab-item:: {{ macos }}
         :sync: mac

         ``clear`` will clear all output from the terminal

