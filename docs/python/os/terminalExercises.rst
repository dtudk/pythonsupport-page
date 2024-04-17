.. _os-terminal:

What's a Terminal?
==================


``The Terminal`` may sound complicated, but it is a fundamental part of every computer and a key element used in development for handling most tasks in your coding environment.

You can think of the terminal as a direct line of communication between you and the computer. For instance, when you install an extension in one of your apps or create a new file using an app, you are actually using the terminal indirectly. 
Learning how to use the Terminal allows you to give the computer the exact commands you want and to know precisely **where** and **how** new files are being created. This knowledge comes in handy when developing software or working with large databases.

Commands
--------

Commands executed on the terminal comprises of the application name ``<command>``, followed by arguments to the command ``<command> <arguments>``. For instance, a command creating a new directory would be expected to have
a single mandatory argument which equals the name of the new folder. Other commands may have several mandatory arguments.

.. admonition:: Optional arguments and spaces in names
   :class: dropdown
   
   Most commands have *optional* arguments prefixed with ``--`` (Mac/Unix, sometimes Windows) or ``/`` (Windows).

   Spaces in file/folder names has to be escaped by encapsulating in quotation marks.
   For instance ``cd "New Folder"``, or ``rm "my file"``.


pwd (Print Working Directory)
+++++++++++++++++++++++++++++++

The ``pwd`` command displays the current working directory. It is particularly helpful when you need to know your current location within the file system.

.. tab-set::

   .. tab-item:: {{win_powershell}}
      :sync: powershell

      .. code-block:: bash

         pwd

   .. tab-item:: {{win_batch}}
      :sync: batch

      .. code-block:: bash

         cd

   .. tab-item:: {{mac_bash}}
      :sync: mac

      .. code-block:: bash

         pwd

   .. tab-item:: {{linux_bash}}
      :sync: bash

      .. code-block:: bash

         pwd


cd (Change Directory)
++++++++++++++++++++++

The ``cd`` command is used to change the current working directory. It enables you to navigate through various folders and explore different parts of the file system.

.. tab-set::

   .. tab-item:: {{win_powershell}}
      :sync: powershell

      .. code-block:: bash

         cd NewFolder

   .. tab-item:: {{win_batch}}
      :sync: batch

      .. code-block:: bash

         cd NewFolder

   .. tab-item:: {{mac_bash}}
      :sync: mac

      .. code-block:: bash

         cd NewFolder

   .. tab-item:: {{linux_bash}}
      :sync: bash

      .. code-block:: bash

         cd NewFolder


ls (List)
+++++++++

The ``ls`` command is used to list all files and directories in the current working directory. It allows you to view the contents of the folder you are currently in.

.. tab-set::

   .. tab-item::  {{win_powershell}}
      :sync: powershell

      .. code-block:: powershell

         ls

   .. tab-item:: {{win_batch}}
      :sync: batch

      .. code-block:: winbatch

         dir

   .. tab-item:: {{mac_bash}}
      :sync: mac

      .. code-block:: bash

         ls

   .. tab-item:: {{linux_bash}}
      :sync: bash

      .. code-block:: bash

         ls


mkdir (Create Directory)
+++++++++++++++++++++++++

The ``mkdir`` command is used to create a new directory. It is particularly helpful when you need to create a new folder for your project.

.. tab-set::

   .. tab-item::  {{win_powershell}}
      :sync: powershell

      .. code-block:: powershell

           mkdir NewFolder

   .. tab-item:: {{win_batch}}
      :sync: batch

      .. code-block:: winbatch

           mkdir NewFolder

   .. tab-item:: {{mac_bash}}
      :sync: mac

      .. code-block:: bash

           mkdir NewFolder

   .. tab-item:: {{linux_bash}}
      :sync: bash

      .. code-block:: bash

           mkdir NewFolder


rm (Remove)
+++++++++++

The ``rm`` or ``del`` command is used to delete files and ``rm -r`` or ``rmdir /s`` to delete directories permanently. It is a powerful command that can help you remove unnecessary files from the file system.

.. tab-set::

   .. tab-item::  {{win_powershell}}
      :sync: powershell

      .. code-block:: powershell

         rm NewFile.txt
         rm -r NewFolder

   .. tab-item:: {{win_batch}}
      :sync: batch

      .. code-block:: winbatch

         del NewFile.txt
         rmdir /s NewFolder

   .. tab-item:: {{mac_bash}}
      :sync: mac

      .. code-block:: bash

         rm NewFile.txt
         rm -r NewFolder

   .. tab-item:: {{linux_bash}}
      :sync: bash

      .. code-block:: bash

         rm NewFile.txt
         rm -r NewFolder


pip (Package Installer for Python)
+++++++++++++++++++++++++++++++++++

The ``pip`` command is a package installer for Python that simplifies the process of managing and installing various Python

.. tab-set::

   .. tab-item::  {{win_powershell}}
      :sync: powershell

      .. code-block:: powershell

         pip install <package_name>

   .. tab-item:: {{win_batch}}
      :sync: batch
       
      .. code-block:: winbatch

         pip install <package_name>

   .. tab-item:: {{mac_bash}}
      :sync: mac

      .. code-block:: bash
       
         pip3 install <package_name>

   .. tab-item:: {{linux_bash}}
      :sync: bash

      .. code-block:: bash
       
         pip3 install <package_name>


How to make using the terminal easier
------------------------------------------

There are a few different tips/tricks to make using the terminal a lot smoother:

* Recycling old inputs with arrow-keys
   * If you have already input a command and need to use it again, pressing the upwards arrow key will go through your old inputs
   * This is especially useful for correcting typos in wrong input

* Using :kbd:`Tab` key to autocomplete input
   * The :kbd:`Tab` key is the one with two sideways arrows (usually placed above caps lock)
   * This is very efficient in combination commands which expects files/folders as arguments.
   * For example one can navigate to the folder ``MyFolderForCourse01006`` by simply typing ``cd My``, and then pressing :kbd:`Tab` and :kbd:`Enter`
     Pressing :kbd:`Tab` multiple times will cycle through all files/folders that starts with ``My``.

* Pasting code into the terminal
   * The terminal is just like any other document, in the sense that you can copy and paste anything
