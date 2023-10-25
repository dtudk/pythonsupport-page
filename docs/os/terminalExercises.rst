What's a Terminal?
============


“The Terminal” may sound complicated, but it is a fundamental part of every computer and a key element used in development for handling most tasks in your coding environment.

You can think of the terminal as a direct line of communication between you and the computer. For instance, when you install an extension in one of your apps or create a new file using an app, you are actually using the terminal indirectly. 
Learning how to use the Terminal allows you to give the computer the exact commands you want and to know precisely **where** and **how** new files are being created. This knowledge comes in handy when developing software or working with large databases.

Commands
--------

pwd (Print Working Directory)
+++++++++++++++++++++++++++++++

The `pwd` command displays the current working directory. It is particularly helpful when you need to know your current location within the file system.

.. tab::  Windows (Powershell)

   .. code-block:: bash

      pwd

.. tab::  Windows (Batch)

   .. code-block:: bash

      echo %cd%

.. tab::  MacOS|Bash

   .. code-block:: bash

      pwd

.. tab::  Linux|Bash

   .. code-block:: bash

      pwd

cd (Change Directory)
++++++++++++++++++++++

The `cd` command is used to change the current working directory. It enables you to navigate through various folders and explore different parts of the file system.

.. tab::  Windows (Powershell)

   .. code-block:: bash

      cd NewFolder

.. tab::  Windows (Batch)

   .. code-block:: bash

      cd NewFolder

.. tab::  MacOS|Bash

   .. code-block:: bash

      cd NewFolder

.. tab::  Linux|Bash

   .. code-block:: bash

      cd NewFolder

ls (List)
+++++++++

The `ls` command is used to list all files and directories in the current working directory. It allows you to view the contents of the folder you are currently in.

.. tab::  Windows (Powershell)

   .. code-block:: bash

      ls

.. tab::  Windows (Batch)

   .. code-block:: bash

      dir

.. tab::  MacOS|Bash

   .. code-block:: bash

      ls

.. tab::  Linux|Bash

   .. code-block:: bash

      ls

mkdir (Create Directory)
+++++++++++++++++++++++++

The `mkdir` command is used to create a new directory. It is particularly helpful when you need to create a new folder for your project.

.. tab::  Windows (Powershell)

   .. code-block:: bash

        mkdir NewFolder

.. tab::  Windows (Batch)

   .. code-block:: bash

        mkdir NewFolder

.. tab::  MacOS|Bash

   .. code-block:: bash

        mkdir NewFolder

.. tab::  Linux|Bash

   .. code-block:: bash

        mkdir NewFolder

rm (Remove)
+++++++++++

The `rm` command is used to delete files or directories permanently. It is a powerful command that can help you remove unnecessary files from the file system.

.. tab::  Windows (Powershell)

   .. code-block:: bash

      rm NewFile.txt

.. tab::  Windows (Batch)

   .. code-block:: bash

      del NewFile.txt

.. tab::  MacOS|Bash

   .. code-block:: bash

      rm NewFile.txt

.. tab::  Linux|Bash

   .. code-block:: bash

      rm NewFile.txt

pip (Package Installer for Python)
+++++++++++++++++++++++++++++++++++

The `pip` command is a package installer for Python that simplifies the process of managing and installing various Python

.. tab::  Windows (Powershell)

   .. code-block:: bash

      pip install package_name

.. tab::  Windows (Batch)
    
   .. code-block:: bash

      pip install package_name

.. tab::  MacOS|Bash

    .. code-block:: bash
    
        pip3 install package_name

.. tab::  Linux|Bash

    .. code-block:: bash
    
        pip3 install package_name