.. Learning the Basics of the Terminal

Welcome to the world of the terminal! In this tutorial, you will learn the fundamentals of using the terminal, a powerful tool for interacting with your computer through text commands. We will cover essential commands and tips to help you navigate and perform tasks efficiently.

.. code:: termynal

   #0 What is a Terminal?
   [Type] A terminal is a text-based interface that allows you to communicate with your computer's operating system using text commands. It provides a way to navigate your file system, run programs, and perform various tasks without the need for a graphical user interface (GUI).

1. Where am I? (pwd and dir)
=============================
.. tab:: {{ bash }}

   To find out your current directory (location), you can use the ``pwd`` command on Unix-based systems (Linux or macOS) or the ``dir`` command on Windows. Open your terminal and type:

   .. termynal:: termynal:pwd

      -  value: pwd # On Unix-based systems (Linux or macOS)
         type: input
         prompt: 'username@mac~$'
      -  /home/username

   .. raw:: html

      <button type="button"
        class="btn btn-primary"
        onclick="new Termynal('#termynal-pwd')">↺</button>
   .. $ pwd  # On Unix-based systems (Linux or macOS)

.. tab:: {{ win_powershell }}

   .. termynal:: termynal:dir

      -  value: dir
         type: input
         prompt: 'PS C:\User\youruser>'
      -  Successfully installed spacy
   
   .. raw:: html

      <button type="button"
        class="btn btn-primary"
        onclick="new Termynal('#termynal-dir')">↺</button>
**Exercise:** Run the appropriate command for your system and note the directory where you are.

2. What's in here? (ls and ls -a)
===================================

To list the contents of your current directory, you can use the ``ls`` command. If you want to see hidden files as well, use ``ls -a``. Try these commands:

.. code:: termynal

   $ ls     # List visible files and folders

OR

.. code:: termynal

   $ ls -a  # List all files and folders, including hidden ones

**Exercise:** Run the commands and observe the files and folders in your current directory.

3. I want to get out of here (cd)
==================================

To navigate to a different directory, you can use the ``cd`` command followed by the path to the desired directory. For example, to move to a directory named "my_folder," you can use:

.. code:: termynal

   $ cd my_folder

**Exercise:** Change to a different directory using the ``cd`` command.

4. General Navigation Tips
==========================

Here are some helpful tips for efficient navigation:

- Use the ``Tab`` key to autocomplete file, folder, or package names.
- Use the arrow keys (up and down) to navigate through previously executed commands.

5. How can I create a new folder? (mkdir)
==========================================

To create a new directory (folder), use the ``mkdir`` command followed by the desired folder name:

.. code:: termynal

   $ mkdir my_new_folder

**Exercise:** Create a new folder using the ``mkdir`` command.

6. Which Python Version? (python/python3)
==========================================

To check your Python version, you can use either ``python`` or ``python3`` command:

.. code:: termynal

   $ python --version

OR

.. code:: termynal

   $ python3 --version

**Exercise:** Check the Python version installed on your system.

7. Python Interactive Shell and Normal Terminal Shell
=====================================================

To enter the Python interactive shell, simply type ``python`` or ``python3`` and press Enter. You will see a different prompt, indicating that you are now in the Python shell.

To exit the Python shell, you can type ``exit()`` or press ``Ctrl + D`` (Unix-based systems) or ``Ctrl + Z`` followed by ``Enter`` (Windows).

**Exercise:** Enter and exit the Python interactive shell to differentiate it from the normal terminal shell.

8. What Packages Do I Have in Python? (pip list)
=================================================

To list the installed Python packages, you can use the ``pip list`` command:

.. code:: termynal

   $ pip list

**Exercise:** List the Python packages installed on your system.

9. Installing and Uninstalling Packages Using pip
================================================

To install a Python package using ``pip``, use the ``pip install`` command followed by the package name:

.. code:: termynal

   $ pip install package_name

To uninstall a package, use ``pip uninstall``:

.. code:: termynal

   $ pip uninstall package_name

**Exercise:** Install and uninstall a Python package using ``pip``.

Congratulations! You've completed the basics of using the terminal. Continue exploring and practicing to become more proficient in using this powerful tool for various tasks and system administration.
