.. _terminalTutorial:

Terminal tutorial
===================

Welcome to the world of the Terminal! In this tutorial, you will learn the fundamentals of using the Terminal, 
a powerful tool for interacting with your computer through text commands. 
We will cover essential commands and tips to help you navigate and perform tasks efficiently.

You can learn more about what a Terminal is and the most useful commands :ref:`here <terminalExercise>`


Opening a terminal
^^^^^^^^^^^^^^^^^^

Each operating system opens terminals in a different way. 


.. tab:: {{ win_powershell }}

   Search for ``powershell`` in the Windows taskbar search or 
   press :kbd:`Win-R` buttons (simultaneously), then type
   ``powershell`` in the small run window appearing, press :kbd:`Enter`.

   This should open a **Terminal** looking *something* like this:

   .. termynal:: termynal:pythonPS
      :title:  Powershell
      :windows:

      -  value: ''
         type: input
         prompt: 'PS C:\User\youruser>'


.. tab:: {{ win_batch }}

   Search for ``cmd`` in the Windows taskbar search
   or press :kbd:`Win-R` buttons (simultaneously), then type
   ``cmd`` in the small run window appearing, press :kbd:`Enter`.
  
   This should open a **Terminal** looking *something* like this:

   .. termynal:: termynal:pythonCMD
         :title: Command Propmt
         :windows:

         -  value: ''
            type: input
            prompt: 'C:\User\youruser>'


.. tab:: {{ mac_bash }}

   Open the Launchpad icon in the Dock, or press :kbd:`Command-Space`; type ``Terminal`` and click on it.

   See more detailed explanation `here <https://support.apple.com/en-gb/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac>`__.
   
   This should open a **Terminal** looking *something* like this:

   .. termynal:: termynal:pythonMAC
      :title: bash
      :unix:

      -  value: ''
         type: input
         prompt: 'username@mac~$'

.. tab:: {{ linux_bash }}

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

   .. termynal:: termynal:pythonLINUX
         :title: bash
         :unix:

         -  value: ''
            type: input
            prompt: 'username@linux~$'






1. Where am I? (pwd and dir)
=============================


.. tab:: {{ win_powershell }} 
      
   To find out your current directory (location), you can use the 
   ``dir`` command on Windows. 

   -Type and enter ``dir`` in your Terminal.

   This should look *something* like this in your **Terminal**:
   
   .. termynal:: termynal:cdPS
      :title: Powershell
      :windows:

      -  value: dir
         type: input
         prompt: 'PS C:\User\youruser>'
      -  'PS C:\User\youruser>'

.. tab:: {{ win_batch }} 
   
   To find out your current directory (location), you can use the  
   ``dir`` command on Windows. 

   -Type and enter ``dir`` in your Terminal.

   This should look *something* like this in your **Terminal**:
   
   .. termynal:: termynal:cdCMD
      :title: Command Prompt
      :windows:

      -  value: dir
         type: input
         prompt: 'C:\User\youruser>'
      -  'C:\User\youruser>'

.. tab:: {{ mac_bash }} 

   To find out your current directory (location), you can use the 
   ``pwd`` command on Unix-based systems (Linux or macOS).

   -Type and enter ``pwd`` in your Terminal.

   This should look *something* like this in your **Terminal**:
   

   
   .. termynal:: termynal:pwdMAC
      :title: Bash
      :unix:

      -  value: pwd
         type: input
         prompt: 'username@mac~$'
      -  /home/username

.. tab:: {{ linux_bash }} 


   To find out your current directory (location), you can use the 
   ``pwd`` command on Unix-based systems (Linux or macOS). 

   -Type and enter ``pwd`` in your Terminal. 

   This should look *something* like this in your **Terminal**:
   
   
   .. termynal:: termynal:pwdLINUX
      :title: Bash
      :unix:

      -  value: pwd
         type: input
         prompt: 'username@linux~$'
      -  /home/username





2. What's in here?
===================================


.. tab:: {{ win_powershell }} 

   To list the contents of your current directory in PowerShell, you can use the ``dir`` cmdlet. 
   If you want to see only files and not directories, use ``dir /a``. 
   

   1- Type and enter in your Terminal:
   ``dir``

   2- Type and enter in your Terminal:
   ``dir /a``

   This should look *something* like this in your **Terminal**:


   .. termynal:: termynal:lsPS
      :title: Powershell
      :windows:

      -  value: ls
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
      -  value: ls -Force
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

   To list the contents of your current directory in Windows Command Prompt, you can use the ``dir`` command. If you want to see hidden files and directories as well, use ``dir /a``. 
   

   1- Type and enter in your Terminal:
   ``dir``

   2- Type and enter in your Terminal:
   ``dir /a``

   This should look *something* like this in your **Terminal**:

   
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

   To list the contents of your current directory, you can use the ``ls`` command. 
   If you want to see hidden files as well, use ``ls -a``.  
   

   1- Type and enter in your Terminal:
   ``ls``

   2- Type and enter in your Terminal:
   ``ls-a``

   This should look *something* like this in your **Terminal**:

  
   
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
   
   To list the contents of your current directory, you can use the ``ls`` command. If you want to see hidden files as well, use ``ls -a``.

   1- Type and enter in your Terminal:
   ``ls``

   2- Type and enter in your Terminal:
   ``ls -a``

   This should look *something* like this in your **Terminal**:

   
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



3. Changing directories (cd)
==========================================

.. tab:: {{ win_powershell }} 
   
   **Warning 1**:
   Note that instead of ``MyFolder`` you should use one of the folders listed in the previous exercise.

   **Warning 2 (for Windows)**:
   Note when typing the directory name of subfolders, that Windows uses backslashes ``\`` and **not** forward slashes ``/``

   To navigate to a different directory, you can use the ``cd`` command followed by the path to the desired 
   directory, and to navigate one step backwards, you can use the ``cd ..`` command.

   1- Type and enter in your Terminal: ``cd MyFolder``
   
   2-Type and enter in your Terminal: ``cd ..``
   
   This should look *something* like this in your **Terminal**:
   
   .. termynal:: termynal:chdirps
        :title: Powershell
        :windows:

         -  value: cd MyFolder
            type: input
            prompt: 'PS C:\User\youruser>'
         -  prompt: 'PS C:\User\youruser\MyFolder>'  
         -  value: cd ..
            type: input
            prompt: 'PS C:\User\youruser\Myfolder>'
         -  prompt: 'PS C:\User\youruser>'  


.. tab:: {{ win_batch }}

   **Warning 1**:
   Note that instead of ``MyFolder`` you should use one of the folders listed in the previous exercise.

   **Warning 2 (for Windows)**:
   Note when typing the directory name of subfolders, that windows uses backslashes ``\`` and NOT forward slashes ``/``

   To navigate to a different directory, you can use the ``cd`` command followed by the path to the desired 
   directory, and to navigate one step backwards, you can use the ``cd ..`` command.

   1- Type and enter in your Terminal: ``cd MyFolder``
   
   2-Type and enter in your Terminal: ``cd ..``
   
   This should look *something* like this in your **Terminal**:
   
   .. termynal:: termynal:chdircmd
        :title: Command prompt
        :windows:

         -  value: cd MyFolder
            type: input
            prompt: 'C:\User\youruser>'
         -  prompt: 'C:\User\youruser\MyFolder>'
         -  value: cd ..
            type: input
            prompt: 'C:\User\youruser\Myfolder>'
         -  prompt: 'C:\User\youruser>'

.. tab:: {{ mac_bash }}

   **Warning**:
   Note that instead of ``MyFolder`` you should use one of the folders listed in the previous exercise.

   To navigate to a different directory, you can use the ``cd`` command followed by the path to the desired 
   directory, and to navigate one step backwards, you can use the ``cd ..`` command.

   1- Type and enter in your Terminal: ``cd MyFolder``
   
   2-Type and enter in your Terminal: ``cd ..``

   This should look *something* like this in your **Terminal**:
   
   .. termynal:: termynal:chdirmac
        :title: bash
        :unix:

         -  value: cd MyFolder # On Unix-based systems (Linux or macOS)
            type: input
            prompt: 'username@mac~%'
         -  prompt: username@mac MyFolder~%
         -  value: cd ..
            type: input
            prompt: 'username@mac MyFolder~%'
         -  prompt: username@mac~%

   

   
.. tab:: {{ linux_bash }}

   **Warning**:
   Note that instead of ``MyFolder`` you should use one of the folders listed in the previous exercise.

   To navigate to a different directory, you can use the ``cd`` command followed by the path to the desired 
   directory, and to navigate one step backwards, you can use the ``cd ..`` command.

   1- Type and enter in your Terminal: ``cd MyFolder``
   
   2-Type and enter in your Terminal: ``cd ..``
   
   This should look *something* like this in your **Terminal**:


   .. termynal:: termynal:chdirlinux
        :title: bash
        :unix:

         -  value: cd MyFolder 
            type: input
            prompt: 'username@linux~$'
         -  prompt: 'username@linux MyFolder~$'
         -  value: cd ..
            type: input
            prompt: 'username@linuxMyFolder~$'
         -  prompt: 'username@linux~$'



A good trick to use in Visual Studio Code is to open a folder in your sidebar, and copy the names of folders/directories that you would like to work in. This is done by completing the steps below:

#. Press the icon in the top left of the screen that looks like 2 pieces of paper on top of each other
#. Press "open folder"
#. Visual studio code will now open your files. Select the folder that you would like to work with by clicking on it
#. Now you should see all the files and subfolders contained in the folder taht you selected on the left side of the screen
#. You can now right click a folder and press "copy path"
#. type cd in your terminal and paste the path that you just copied 

In general it is a good idea to change your directory, to the place of whatever you are working with. For example, if a large dataset is in a specific folder, you can change your directory to that folder. 



4. How can I create a new folder? (mkdir)
=============================

.. tab::  Windows (Powershell) 

   To create a new folder you can use ``mkdir`` on your Terminal. Then, you can use ``ls`` to see 
   if the folder was successfully created.

   1-Type and enter in your Terminal: ``mkdir NewPythonFolder``

   2-Type and enter in your Terminal: ``ls``

   This should look *something* like this in your **Terminal**:

   
   .. termynal:: termynal:mkdirPS
        :title: Powershell
        :windows:

        -   value: mkdir NewPythonFolder
            type: input
            prompt: 'PS C:\User\youruser>'
        -   value: ls
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
        -  '   d-----        8/1/2021  10:00 AM              NewPythonFolder'     



.. tab:: Windows (Command prompt)

   To create a new folder you can use ``mkdir`` on your Terminal. Then, you can use ``dir`` to see 
   if the folder was successfully created.
   
   1-Type and enter in your Terminal: ``mkdir NewPythonFolder``

   2-Type and enter in your Terminal: ``dir``

   This should look *something* like this in your **Terminal**:
   
   .. termynal:: termynal:mkdirCMD
        :title: Command prompt
        :windows:

        -   value: mkdir NewPythonFolder
            type: input
            prompt: 'C:\User\youruser>'
        -   value: dir
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
        -  '   d-----        8/1/2021  10:00 AM              NewPythonFolder'    



.. tab:: Mac Terminal

   To create a new folder you can use ``mkdir`` on your Terminal. Then, you can use ``ls`` to see 
   if the folder was successfully created.
   
   1-Type and enter in your Terminal: ``mkdir NewPythonFolder``

   2-Type and enter in your Terminal: ``ls``

   This should look *something* like this in your **Terminal**:

   
   .. termynal:: termynal:mkdirMAC
        :title: Command prompt
        :unix:

        -   value: mkdir NewPythonFolder 
            type: input
            prompt: 'username@mac ~ %'
        -   value: ls
            type: input
            prompt: 'username@mac~$'
        -   myfolder1 myfolder2 myfile.txt myscript.py NewPythonFolder


        




.. tab:: Linux Terminal

   To create a new folder you can use ``mkdir`` on your Terminal. Then, you can use ``ls`` to see 
   if the folder was successfully created.
   
   1-Type and enter in your Terminal: ``mkdir NewPythonFolder``

   2-Type and enter in your Terminal: ``ls``

   This should look *something* like this in your **Terminal**:

   
   .. termynal:: termynal:mkdirLINUX
        :title: Command prompt
        :unix:

        -   value: mkdir NewPythonFolder
            type: input
            prompt: 'username@linux~$'
        -   value: ls
            type: input
            prompt: 'username@linux~$'     
        -   myfolder1 myfolder2 myfile.txt myscript.py NewPythonFolder
    



5. How can I delete a folder or a file using a Terminal? (rm and rm -r)
=============================


.. tab::  Windows (Powershell) 

   You can use ``rm`` to delete a file or ``rm -r`` to delete a folder using the Terminal. 

   1-Type and enter in your Terminal: ``rm -r NewPythonFolder``

   2-Type and enter in your Terminal: ``ls``

   This should look *something* like this in your **Terminal**:


   
   .. termynal:: termynal:rmPS
        :title: Powershell
        :windows:

        -   value: rm -r NewPythonFolder
            type: input
            prompt: 'PS C:\User\youruser>'
        -   value: ls
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

.. tab:: Windows (Command prompt)
   
   You can use ``rm`` to delete a file or ``rm -r`` to delete a folder using the Terminal. 

   1-Type and enter in your Terminal: ``rm -r NewPythonFolder``

   2-Type and enter in your Terminal: ``dir``

   This should look *something* like this in your **Terminal**:

   
   .. termynal:: termynal:rmCMD
        :title: Command prompt
        :windows:

        -   value: rm -r NewPythonFolder
            type: input
            prompt: 'C:\User\youruser>'
        -   value: dir
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



.. tab:: Mac Terminal

   You can use ``rm`` to delete a file or ``rm -r`` to delete a folder using the Terminal. 

   1-Type and enter in your Terminal: ``rm -r NewPythonFolder``

   2-Type and enter in your Terminal: ``ls``

   This should look *something* like this in your **Terminal**:   

   
   .. termynal:: termynal:rmMAC
        :title: Command prompt
        :unix:

        -   value: rm -r NewPythonFolder 
            type: input
            prompt: 'username@mac ~ %'
        -   value: ls
            type: input
            prompt: 'username@mac~$'
        -   myfolder1 myfolder2 myfile.txt myscript.py NewPythonFolder


        


   
.. tab:: Linux Terminal

   You can use ``rm`` to delete a file or ``rm -r`` to delete a folder using the Terminal. 

   1-Type and enter in your Terminal: ``rm -r NewPythonFolder``

   2-Type and enter in your Terminal: ``ls``

   This should look *something* like this in your **Terminal**:

   
   .. termynal:: termynal:rmLINUX
        :title: Command prompt
        :unix:

        -   value: rm -r NewPythonFolder
            type: input
            prompt: 'username@linux~$'
        -   value: ls
            type: input
            prompt: 'username@linux~$'     
        -   myfolder1 myfolder2 myfile.txt myscript.py NewPythonFolder        
        




6. Which Python version? (python --version or python3 --version)
==================================




.. tab::  Windows (Powershell) 

   To check which Python version you have you can use ``python --version``

   To enter Python in your Terminal you can use ``python``

   To exit Python in your Terminal you can use ``exit()``

   1-Type and enter in your Terminal: ``python --version`` 

   2-Type and enter in your Terminal: ``python``

   3-Type and enter in your Terminal: ``exit()``
   

   This should look *something* like this in your **Terminal**:

   
   
   .. termynal:: termynal:pythonversionPSS
        :title: Powershell
        :windows:

        -   value: python --version
            type: input
            prompt: 'PS C:\User\youruser>'
        -   'Python 3.11.4' 
        -   value: python
            type: input
            prompt: 'PS C:\User\youruser>'
        -  'Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on Windows'
        -  'Type "help", "copyright", "credits" or "license" for more information.'
        -   value: exit()
            type: input
            prompt: '>>>'
        -   value: ''
            type: input
            prompt: 'PS C:\User\youruser>' 

.. tab:: Windows (Command prompt)

   To check which Python version you have you can use ``python --version``

   To enter Python in your Terminal you can use ``python``

   To exit Python in your Terminal you can use ``exit()``

   1-Type and enter in your Terminal: ``python --version`` 

   2-Type and enter in your Terminal: ``python``

   3-Type and enter in your Terminal: ``exit()``
   

   This should look *something* like this in your **Terminal**:

   
   .. termynal:: termynal:pythonversionCMD
        :title: Command prompt
        :windows:

        -   value: python --version
            type: input
            prompt: 'C:\User\youruser>'
        -   'Python 3.11.4'  
        -   value: python
            type: input
            prompt: 'PS C:\User\youruser>'
        -  'Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on Windows'
        -  'Type "help", "copyright", "credits" or "license" for more information.'
        -   value: exit()
            type: input
            prompt: '>>>'
        -   value: ''
            type: input
            prompt: 'PS C:\User\youruser>' 



.. tab:: Mac Terminal

   To check which Python version you have you can use ``python --version`` or ``python3 --version``

   **Note that this might change depending 
   whether you have more than one Python version installed**

   To enter Python in your Terminal you can use ``python`` or ``python3``

   To exit Python in your Terminal you can use ``exit()``

   1-Type and enter in your Terminal: ``python3 --version`` 

   2-Type and enter in your Terminal: ``python3``

   3-Type and enter in your Terminal: ``exit()``
   

   This should look *something* like this in your **Terminal**:

   

   .. termynal:: termynal:pythonversionMAC
        :title: Command prompt
        :unix:

        -   value: python --version 
            type: input
            prompt: 'username@mac ~ %'
        -   'Python 3.11.4' 
        -   value: python3
            type: input
            prompt: 'username@mac ~ %'
        -  'Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on darwin'
        -  'Type "help", "copyright", "credits" or "license" for more information.'
        -   value: exit()
            type: input
            prompt: '>>>'
        -   value: ''
            type: input
            prompt: 'username@mac ~ %' 


    


  

.. tab:: Linux Terminal
   
   To check which Python version you have you can use ``python --version`` or ``python3 --version``

   **Note that this might change depending 
   whether you have more than one Python version installed**

   To enter Python in your Terminal you can use ``python`` or ``python3``

   To exit Python in your Terminal you can use ``exit()``

   1-Type and enter in your Terminal: ``python version`` 

   2-Type and enter in your Terminal: ``python``

   3-Type and enter in your Terminal: ``exit()``
   

   This should look *something* like this in your **Terminal**:

   

   
   .. termynal:: termynal:pythonversionLINUX
        :title: Command prompt
        :unix:

        -   value: python --version
            type: input
            prompt: 'username@linux~$'
        -   'Python 3.11.4'  
        -   value: python3
            type: input
            prompt: 'username@linux~$'
        -  'Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux'
        -  'Type "help", "copyright", "credits" or "license" for more information.'
        -   value: exit()
            type: input
            prompt: '>>>'
        -   value: ''
            type: input
            prompt: 'username@linux~$' 



7. Which packages do I have? 
==================================================


.. tab:: {{ win_powershell }} 
   
   To see which packages you currently have in Python, you can use ``pip list``. 

   This should look *something* like this in your **Terminal**:
   
   .. termynal:: termynal:pip3list
        :title: Powershell
        :windows:

        -   value: pip list
            type: input
            prompt: 'PS C:\User\youruser>'
        -   "numpy     3.0.2"
        -   "sympy     2.0.4"



.. tab:: {{ win_batch }}
   
   To see which packages you currently have in Python, you can use ``pip list``. 

   This should look *something* like this in your **Terminal**:
   
   .. termynal:: termynal:pip3listcmd
        :title: Command prompt
        :windows:

        -   value: pip list
            type: input
            prompt: 'C:\User\youruser>'
        -   "numpy   3.0.2"
        -   "sympy   2.0.4"

 

.. tab:: {{ mac_bash }}
   
   To see which packages you currently have in Python, you can use ``pip3 list``. 

   This should look *something* like this in your **Terminal**:

   
   .. termynal:: termynal:pip3listmac
        :title: bash
        :unix:

        -   value: pip3 list # On Unix-based systems (Linux or macOS)
            type: input
            prompt: 'username@mac~%'
        -   "numpy   3.0.2"
        -   "sympy   2.0.4"

   



.. tab:: {{ linux_bash }}
   
   To see which packages you currently have in Python, you can use ``pip3 list``. 

   This should look *something* like this in your **Terminal**:

   .. termynal:: termynal:pip3listlinux
        :title: bash
        :unix:

        -   value: pip3 list # On Unix-based systems (Linux or macOS)
            type: input
            prompt: 'username@linux~$'
        -   "numpy   3.0.2"
        -   "sympy   2.0.4"




    
