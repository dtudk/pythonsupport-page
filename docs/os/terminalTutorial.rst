.. _os-terminal:

Terminal tutorial
===================

Terminals is one the most widely used methods for running and interacting
with any Python environment. It may also be known under the name *Shell*'s.

`Terminals <https://en.wikipedia.org/wiki/Terminal_emulator>`_ comes in a variety of different forms.

It is used to execute commands in an interactive manner.


Opening a terminal
^^^^^^^^^^^^^^^^^^

Each operating system opens terminals in a different way. In the following a ``#`` is
a comment in the terminal, i.e. it is *not* considered a command.


.. tab:: {{ win_powershell }}
   
   Either of
   
   1. Search for ``powershell`` in the Windows taskbar search
   2. A short-cut: press :kbd:`Win-R` buttons (simultaneously), then type
      ``powershell`` in the small run window appearing, press :kbd:`Enter`.
   3. Launch Python
      
   .. termynal:: termynal:pythonPS
      :title:  Powershell
      :windows:

      -  value: python
         type: input
         prompt: 'PS C:\User\youruser>'
      -  'Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux'
      -  'Type "help", "copyright", "credits" or "license" for more information.'
      -  '>>>'

.. tab:: {{ win_batch }}

   Either of

   1. Search for ``cmd`` in the Windows taskbar search
   2. A short-cut: press :kbd:`Win-R` buttons (simultaneously), then type
      ``cmd`` in the small run window appearing, press :kbd:`Enter`.
   3. Launch Python

      .. termynal:: termynal:pythonCMD
         :title: Command Propmt
         :windows:

         -  value: python
            type: input
            prompt: 'C:\User\youruser>'
         -  'Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux'
         -  'Type "help", "copyright", "credits" or "license" for more information.'
         -  '>>>'


.. tab:: {{ mac_bash }}

   Open the Launchpad icon in the Dock, or press :kbd:`Command-Space`; type ``Terminal`` and click on it.

   See more detailed explanation `here <https://support.apple.com/en-gb/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac>`__.

   Launch Python

   .. termynal:: termynal:pythonMAC
      :title: bash
      :unix:

      -  value: python3
         type: input
         prompt: 'username@mac~$'
      -  'Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux'
      -  'Type "help", "copyright", "credits" or "license" for more information.'
      -  '>>>'


.. tab:: {{ linux_bash }}

   This depends on the distribution you are using. Nearly all Linux distributions
   has the Terminal icon near the Desktop.

   On Ubuntu one could do:

   1. Press :kbd:`Ctrl-Alt-T` simultaneously.
   2. Press the :kbd:`Win` key which should open up a search box, type
      ``terminal`` and press :kbd:`Enter`
   3. Lastly, one option is to open up a file explorer and right-click a folder,
      there should be an option name ``Open in Terminal`` which will open that
      folder in the terminal.
   4. Launch Python

      .. termynal:: termynal:pythonLINUX
         :title: bash
         :unix:

         -  value: python
            type: input
            prompt: 'username@linux~$'
         -  'Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux'
         -  'Type "help", "copyright", "credits" or "license" for more information.'
         -  '>>>'


In the terminal one can navigate the `file system <https://en.wikipedia.org/wiki/File_system>`__
by using commands specific to your operating systems shell.


Welcome to the world of the terminal! In this tutorial, you will learn the fundamentals of using the terminal, a powerful tool for interacting with your computer through text commands. We will cover essential commands and tips to help you navigate and perform tasks efficiently.

.. code:: 

   #0 What is a Terminal?
   [Type] A terminal is a text-based interface that allows you to communicate with your computer's operating system using text commands. It provides a way to navigate your file system, run programs, and perform various tasks without the need for a graphical user interface (GUI).





1. Where am I? (pwd and dir)
=============================
To find out your current directory (location), you can use the ``pwd`` command on Unix-based systems (Linux or macOS) or the ``dir`` command on Windows. Open your terminal and type:

.. tab:: {{ win_powershell }} 

   
   .. termynal:: termynal:cdPS
      :title: Powershell
      :windows:

      -  value: cd
         type: input
         prompt: 'PS C:\User\youruser>'
      -  'PS C:\User\youruser>'

.. tab:: {{ win_batch }} 

   
   .. termynal:: termynal:cdCMD
      :title: Command Prompt
      :windows:

      -  value: cd
         type: input
         prompt: 'C:\User\youruser>'
      -  'C:\User\youruser>'

.. tab:: {{ mac_bash }} 

   
   .. termynal:: termynal:pwdMAC
      :title: Bash
      :unix:

      -  value: pwd
         type: input
         prompt: 'username@mac~$'
      -  /home/username

.. tab:: {{ linux_bash }} 

   
   .. termynal:: termynal:pwdLINUX
      :title: Bash
      :unix:

      -  value: pwd
         type: input
         prompt: 'username@linux~$'
      -  /home/username

**Exercise:** Run the appropriate command for your system and note the directory where you are.





2. What's in here?
===================================


.. tab:: {{ win_powershell }} 

   To list the contents of your current directory in PowerShell, you can use the ``Get-ChildItem`` cmdlet. If you want to see only files and not directories, use ``Get-ChildItem -File``. To show hidden files and directories, use ``Get-ChildItem -Force``. Try these commands:
   
   .. termynal:: termynal:lsPS
      :title: Powershell
      :windows:

      -  value: Get-ChildItem -Path "C:\User\youruser"
         type: input
         prompt: 'PS C:\User\youruser>'
      -  ' Directory: C:\User\youruser'
      -
      -  '   Mode                LastWriteTime         Length Name'
      -  '   ----                -------------         ------ ----'
      -  '   d-----        8/1/2021  10:00 AM              myfolder1'
      -  '   d-----        8/1/2021  10:00 AM              myfolder2'
      -  '   -a----        8/1/2021  10:00 AM              0 myfile.txt'
      -  '   -a----        8/1/2021  10:00 AM              0 myscript.py'
      -  value: Get-ChildItem -Path "C:\User\youruser" -Force
         type: input
         prompt: 'PS C:\User\youruser>'
      -  ' Directory: C:\User\youruser'
      -
      -  '   Mode                LastWriteTime         Length Name'
      -  '   ----                -------------         ------ ----'
      -  '   d-----        8/1/2021  10:00 AM              .hiddenfolder'
      -  '   -a----        8/1/2021  10:00 AM              0 .hiddenfile'
      -  '   -a----        8/1/2021  10:00 AM              0 myfile.txt'
      -  '   -a----        8/1/2021  10:00 AM              0 myscript.py'

.. tab:: {{ win_batch }}

   To list the contents of your current directory in Windows Command Prompt, you can use the ``dir`` command. If you want to see hidden files and directories as well, use ``dir /a``. Try these commands:
   
   .. termynal:: termynal:dirCMD
      :title: Command prompt
      :windows:

      -  value: dir
         type: input
         prompt: 'C:\User\youruser>'
      -  ' Volume in drive C has no label.'
      -  '   Volume Serial Number is 1234-5678'
      -  
      -  '   Directory of C:\User\youruser'
      -  
      -  '   08/01/2021  10:00 AM    <DIR>          .'
      -  '   08/01/2021  10:00 AM    <DIR>          ..'
      -  '   08/01/2021  10:00 AM    <DIR>          myfolder1'
      -  '   08/01/2021  10:00 AM    <DIR>          myfolder2'
      -  '   08/01/2021  10:00 AM                 0 myfile.txt'
      -  '   08/01/2021  10:00 AM                 0 myscript.py'
      -  '                  2 File(s)              0 bytes'
      -  '                  4 Dir(s)  1,234,567,890 bytes free'
      -  value: dir /a
         type: input
         prompt: 'C:\User\youruser>'
      -  ' Volume in drive C has no label.'
      -  '   Volume Serial Number is 1234-5678'
      -  
      -  '   Directory of C:\User\youruser'
      -  
      -  '   08/01/2021  10:00 AM    <DIR>          .'
      -  '   08/01/2021  10:00 AM    <DIR>          ..'
      -  '   08/01/2021  10:00 AM    <DIR>          .hiddenfolder'
      -  '   08/01/2021  10:00 AM                 0 .hiddenfile'
      -  '   08/01/2021  10:00 AM    <DIR>          myfolder1'
      -  '   08/01/2021  10:00 AM    <DIR>          myfolder2'
      -  '   08/01/2021  10:00 AM                 0 myfile.txt'
      -  '   08/01/2021  10:00 AM                 0 myscript.py'
      -  '                  3 File(s)              0 bytes'
      -  '                  5 Dir(s)  1,234,567,890 bytes free'

.. tab:: {{ mac_bash }}
   
   To list the contents of your current directory, you can use the ``ls`` command. If you want to see hidden files as well, use ``ls -a``. Try these commands:
   
   .. termynal:: termynal:lsMAC
        :title: bash
        :unix:

        -   value: ls
            type: input
            prompt: 'username@mac~$'
        -   myfolder1 myfolder2 myfile.txt myscript.py
        -   value: ls -a
            type: input
            prompt: 'username@mac~$'
        -   .hiddenfolder .hiddenfile myfolder1 myfolder2 myfile.txt myscript.py


.. tab:: {{ linux_bash }}
   
   To list the contents of your current directory, you can use the ``ls`` command. If you want to see hidden files as well, use ``ls -a``. Try these commands:
   
   .. termynal:: termynal:lsLINUX
        :title: bash
        :unix:

        -   value: ls
            type: input
            prompt: 'username@linux~$'
        -   myfolder1 myfolder2 myfile.txt myscript.py
        -   value: ls -a
            type: input
            prompt: 'username@linux~$'
        -   .hiddenfolder .hiddenfile myfolder1 myfolder2 myfile.txt myscript.py


**Exercise:** Run the commands and observe the files and folders in your current directory.





3. Changing directories (cd)
==========================================

To navigate to a different directory, you can use the ``cd`` command followed by the path to the desired directory. For example, to move to a directory named "MyFolder," do as explained below:

Type and enter in your Terminal:
   .. code:: termynal 

      cd MyFolder

It should look something like this:

.. tab:: {{ win_powershell }} 

   
   .. termynal:: termynal:chdirps
        :title: Powershell
        :windows:

         -  value: cd MyFolder
            type: input
            prompt: 'PS C:\User\youruser>'
         -  prompt: 'PS C:\User\youruser\MyFolder>'  


.. tab:: {{ win_batch }}

   
   .. termynal:: termynal:chdircmd
        :title: Command prompt
        :windows:

         -  value: cd MyFolder
            type: input
            prompt: 'C:\User\youruser>'
         -  prompt: 'C:\User\youruser\MyFolder>'

.. tab:: {{ mac_bash }}

   
   .. termynal:: termynal:chdirmac
        :title: bash
        :unix:

         -  value: cd MyFolder # On Unix-based systems (Linux or macOS)
            type: input
            prompt: 'username@mac~%'
         -  prompt: username@mac MyFolder~%

   
.. tab:: {{ linux_bash }}


   .. termynal:: termynal:chdirlinux
        :title: bash
        :unix:

         -  value: cd MyFolder # On Unix-based systems (Linux or macOS)
            type: input
            prompt: 'username@linux~$'
         -  prompt: 'username@linux MyFolder~$'

A good trick to use in visual studio code, is to open a folder in your sidebar, and copy the names of folders/directories that you would like to work in. This is done by completing the steps below:

#. Press the icon in the top left of the screen that looks like 2 pieces of paper on top of each other
#. Press "open folder"
#. Visual studio code will now open your files. Select the folder that you would like to work with by clicking on it
#. Now you should see all the files and subfolders contained in the folder taht you selected on the left side of the screen
#. You can now right click a folder and press "copy path"
#. type cd in your terminal and paste the path that you just copied 

In general it is a good practice, it is a good idea to change your directory, to the place of whatever you are working with. For example, if a large dataset is in a specific folder, you can change your directory to that folder. 




To navigate one step backwards, you can use the ``cd ..`` command:

It might look something like this:


.. tab:: {{ win_powershell }} 

   
   .. termynal:: termynal:backdir
        :title: Powershell
        :windows:

         -  value: cd ..
            type: input
            prompt: 'PS C:\User\youruser\Myfolder>'
         -  prompt: 'PS C:\User\youruser>'  


.. tab:: {{ win_batch }}

   
   .. termynal:: termynal:backdircmd
        :title: Command prompt
        :windows:

         -  value: cd ..
            type: input
            prompt: 'C:\User\youruser\Myfolder>'
         -  prompt: 'C:\User\youruser>'

.. tab:: {{ mac_bash }}

   
   .. termynal:: termynal:backdirmac
        :title: bash
        :unix:

         -  value: cd .. # On Unix-based systems (Linux or macOS)
            type: input
            prompt: 'username@mac MyFolder~%'
         -  prompt: username@mac~%

   
.. tab:: {{ linux_bash }}


   .. termynal:: termynal:backdirlinux
        :title: bash
        :unix:

         -  value: cd .. # On Unix-based systems (Linux or macOS)
            type: input
            prompt: 'username@linux MyFolder~$'
         -  prompt: 'username@linux~$'


.. code:: termynal 

   cd .. 

**exercise:** try to navigate to a directory, and then leaving it using ``cd ..``





4. How can i make using the terminal easier? 
==================================================

There are a few different tips/tricks to make using the terminal a lot smoother:

* Recycling old inputs with arrow-keys
   * If you have already input a command and need to use it again, pressing the upwards arrow key will go through your old inputs
   * This is especially useful for correcting typos in wrong input

* Using tab key to autocomplete input
   * The tab key is the one with two sideways arrows (usually placed above caps lock)
   * This is very efficient in combination with the ``cd`` command 
   * For example one can navigate to the folder "MyFolderForCourse01006" by simply typing ``cd My``, and then pressing tab followed by enter
   * This also works for importing packages 

* Pasting code into the terminal
   * The terminal is just like any other document, in the sense that you can copy and paste anything
   * **Warning: In the terminal, pasting is done by simply rightclicking or pressing with two fingers on the mousepad , not by using ``ctrl + v``**





5. How can I create a new folder? (mkdir)
=============================
To create a new folder you can use ``mkdir`` on your Terminal. In this exercise you will create a new folder called ``NewPythonFolder``

1-Type and enter in your Terminal:
   .. code-block:: 

      mkdir NewPythonFolder

2-Type and enter in your Terminal:
   .. code-block:: 

      ls

This should look *something* like this in your **Terminal**:


.. tab::  Windows (Powershell) 

   
   .. termynal:: termynal:mkdirPS
        :title: Powershell
        :windows:

        -   value: mkdir NewPythonFolder
            type: input
            prompt: 'PS C:\User\youruser>'
        -   value: ls
            type: input
            prompt: 'PS C:\User\youruser>'
        -   'PS C:\User\youruser>'  



.. tab:: Windows (Command prompt)

   
   .. termynal:: termynal:mkdirCMD
        :title: Command prompt
        :windows:

        -   value: mkdir NewPythonFolder
            type: input
            prompt: 'C:\User\youruser>'
        -   value: ls
            type: input
            prompt: 'C:\User\youruser>'   
        -   'C:\User\youruser>'



.. tab:: Mac Terminal

   
   .. termynal:: termynal:mkdirMAC
        :title: Command prompt
        :unix:

        -   value: mkdir NewPythonFolder 
            type: input
            prompt: 'username@mac ~ %'
        -   value: ls
            type: input
            prompt: 'username@mac ~ %' 
        -   'username@mac ~ %'


   .. $ pwd  # On Unix-based systems (Linux or macOS)

.. tab:: Linux Terminal

   
   .. termynal:: termynal:mkdirLINUX
        :title: Command prompt
        :unix:

        -   value: mkdir NewPythonFolder
            type: input
            prompt: 'username@linux~$'
        -   value: ls
            type: input
            prompt: 'username@linux~$'     
        -   'username@linux~$'



After these two simple steps you should get a list as you did before when you learned how to use ``ls``. 
In this list you should be able to see the 'NewPythonFolder' you have just created.





6. How can I delete a folder or a file using a Terminal? (rm and rm -r)
=============================
To eliminate a folder you can use ``rm`` to eliminate a file or ``rm -r`` to eliminate a folder using the Terminal. 
In this exercise you will eliminate the folder you created in the previous exercise. 

1-Type and enter in your Terminal:
   .. code-block:: 

      rm -r NewPythonFolder

2-Type and enter in your Terminal:
   .. code-block:: 

      ls

This should look like this in your **Terminal**:


.. tab::  Windows (Powershell) 

   
   .. termynal:: termynal:rmPS
        :title: Powershell
        :windows:

        -   value: rm -r NewPythonFolder
            type: input
            prompt: 'PS C:\User\youruser>'
        -   value: ls
            type: input
            prompt: 'PS C:\User\youruser>'
        -   'PS C:\User\youruser>'  



.. tab:: Windows (Command prompt)

   
   .. termynal:: termynal:rmCMD
        :title: Command prompt
        :windows:

        -   value: rm -r NewPythonFolder
            type: input
            prompt: 'C:\User\youruser>'
        -   value: ls
            type: input
            prompt: 'C:\User\youruser>'   
        -   'C:\User\youruser>'



.. tab:: Mac Terminal

   
   .. termynal:: termynal:rmMAC
        :title: Command prompt
        :unix:

        -   value: rm -r NewPythonFolder 
            type: input
            prompt: 'username@mac ~ %'
        -   value: ls
            type: input
            prompt: 'username@mac ~ %' 
        -   'username@mac ~ %'


   .. $ pwd  # On Unix-based systems (Linux or macOS)

.. tab:: Linux Terminal

   
   .. termynal:: termynal:rmLINUX
        :title: Command prompt
        :unix:

        -   value: rm -r NewPythonFolder
            type: input
            prompt: 'username@linux~$'
        -   value: ls
            type: input
            prompt: 'username@linux~$'     
        -   'username@linux~$'



After these two simple steps you should get a list as you did before when you learned how to use ``ls``. 
In this list you should not be able to see the 'NewPythonFolder' you have just deleted.





7. Which Python version? (python --version or python3 --version)
==================================

Check which Python version you have.  **Note that this might change depending on what system you 
have and wether you have more than one Python version installed**

You will have to run either:
.. code-block:: 

   python --version

or

.. code-block:: 

   python3 --version

This should look like this in your **Terminal**:


.. tab::  Windows (Powershell) 

   
   .. termynal:: termynal:pythonversionPS
        :title: Powershell
        :windows:

        -   value: python --version
            type: input
            prompt: 'PS C:\User\youruser>'
        -   'Python 3.11.4'  



.. tab:: Windows (Command prompt)

   
   .. termynal:: termynal:pythonversionCMD
        :title: Command prompt
        :windows:

        -   value: python --version
            type: input
            prompt: 'C:\User\youruser>'
        -   'Python 3.11.4'  


.. tab:: Mac Terminal

   .. termynal:: termynal:pythonversionMAC
        :title: Command prompt
        :unix:

        -   value: python --version 
            type: input
            prompt: 'username@mac ~ %'
        -   'Python 3.11.4'  


   .. $ pwd  # On Unix-based systems (Linux or macOS)

.. tab:: Linux Terminal

   
   .. termynal:: termynal:pythonversionLINUX
        :title: Command prompt
        :unix:

        -   value: python --version
            type: input
            prompt: 'username@linux~$'
        -   'Python 3.11.4'  





8. How to know when you are in the python shell
================================================

When you start the Python interpreter, you will see a prompt that looks like this:

.. tab:: {{ win_powershell }} 

   
   .. termynal:: termynal:pythonIdPS
      :title: Powershell
      :windows:

      -  value: python
         type: input
         prompt: 'PS C:\User\youruser>'
      -  'Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux'
      -  'Type "help", "copyright", "credits" or "license" for more information.'
      -  value: ''
         type: input
         prompt: '>>>'
.. tab:: {{ win_cmd }} 

   
   .. termynal:: termynal:pythonIdCMD
      :title: Command Prompt
      :windows:

      -  value: python
         type: input
         prompt: 'C:\User\youruser>'
      -  'Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux'
      -  'Type "help", "copyright", "credits" or "license" for more information.'
      -  value: ''
         type: input
         prompt: '>>>'

.. tab:: {{ mac_bash }} 

   
   .. termynal:: termynal:pythonIdMac
      :title: Bash
      :unix:

      -  value: python
         type: input
         prompt: 'youruser@yourcomputer ~ % '
      -  'Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux'
      -  'Type "help", "copyright", "credits" or "license" for more information.'
      -  value: ''
         type: input
         prompt: '>>>'


.. tab:: {{ linux_bash }} 

   
   .. termynal:: termynal:pythonIdLinux
      :title: Bash
      :unix:

      -  value: python
         type: input
         prompt: 'youruser@yourcomputer:~$ '
      -  'Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux'
      -  'Type "help", "copyright", "credits" or "license" for more information.'
      -  value: ''
         type: input
         prompt: '>>>'

The ``>>>`` prompt indicates that you are inside the Python shell. This means that you can enter Python commands and they will be executed by the interpreter. You can also import modules, define functions, and perform other tasks that you would normally do in a Python script.





9. How to exit python shell
==================================

To exit the Python shell, type ``exit()`` and press Enter.

.. tab:: {{ win_powershell }} 

   
   .. termynal:: termynal:exitPS
      :title: Powershell
      :windows:

      -  value: python
         type: input
         prompt: 'PS C:\User\youruser>'
      -  'Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux'
      -  'Type "help", "copyright", "credits" or "license" for more information.'
      -  value: exit()
         type: input
         prompt: '>>>'
      -  value: ''
         type: input
         prompt: 'PS C:\User\youruser>'

.. tab:: {{ win_cmd }} 

   
   .. termynal:: termynal:exitCMD
      :title: Command Prompt
      :windows:

      -  value: python
         type: input
         prompt: 'C:\User\youruser>'
      -  'Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux'
      -  'Type "help", "copyright", "credits" or "license" for more information.'
      -  value: exit()
         type: input
         prompt: '>>>'
      -  value: ''
         type: input
         prompt: 'C:\User\youruser>'

.. tab:: {{ mac_bash }} 

   
   .. termynal:: termynal:exitMac
      :title: Bash
      :unix:

      -  value: python3
         type: input
         prompt: 'youruser@yourcomputer ~ % '
      -  'Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux'
      -  'Type "help", "copyright", "credits" or "license" for more information.'
      -  value: exit()
         type: input
         prompt: '>>>'
      -  value: ''
         type: input
         prompt: 'youruser@yourcomputer ~ % '

.. tab:: {{ linux_bash }} 

   
   .. termynal:: termynal:exitLinux
      :title: Bash
      :unix:

      -  value: python3
         type: input
         prompt: 'youruser@yourcomputer:~$ '
      -  'Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux'
      -  'Type "help", "copyright", "credits" or "license" for more information.'
      -  value: exit()
         type: input
         prompt: '>>>'
      -  value: ''
         type: input
         prompt: 'youruser@yourcomputer:~$ '





10. Which packages do i have? 
==================================================

To see which packages you currently have, you can type ``pip3 list`` in the terminal.
After a couple of seconds, your terminal will list every package that you have downloaded

You can paste the following code directly in to your terminal:

.. code:: termynal 

      pip3 list

It should look something like this (but you will probably have a lot more packages than 2):

.. tab:: {{ win_powershell }} 

   
   .. termynal:: termynal:pip3list
        :title: Powershell
        :windows:

        -   value: pip list
            type: input
            prompt: 'PS C:\User\youruser>'
        -   "numpy     3.0.2"
        -   "sympy     2.0.4"


.. tab:: {{ win_batch }}

   
   .. termynal:: termynal:pip3listcmd
        :title: Command prompt
        :windows:

        -   value: pip list
            type: input
            prompt: 'C:\User\youruser>'
        -   "numpy   3.0.2"
        -   "sympy   2.0.4"


.. tab:: {{ mac_bash }}

   
   .. termynal:: termynal:pip3listmac
        :title: bash
        :unix:

        -   value: pip3 list # On Unix-based systems (Linux or macOS)
            type: input
            prompt: 'username@mac~%'
        -   "numpy   3.0.2"
        -   "sympy   2.0.4"



.. tab:: {{ linux_bash }}


   .. termynal:: termynal:pip3listlinux
        :title: bash
        :unix:

        -   value: pip3 list # On Unix-based systems (Linux or macOS)
            type: input
            prompt: 'username@linux~$'
        -   "numpy   3.0.2"
        -   "sympy   2.0.4"






