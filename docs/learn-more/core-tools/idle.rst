IDLE
====

.. tip::
    You can copy and paste all code in the grey code blocks below by hovering your mouse over the block and pressing the icon in the top right.

IDLE is an integrated development environment (IDE) that is installed automatically with your Python installation on Windows and MacOS computers. It provides you with an environment where you can write Python scripts and run them, or you can write Python codes line by line to execute immediately (this feature of an IDE is called interactive interpreter). 

IDLE provides a GUI (Graphical User Interface) which simplifies your coding process by allowing you to interact with buttons, icons, or menus. It also has automatic highlighting and automatic indentation which would simplify your coding process. It is quite lightweight, so it would be convenient to use IDLE while learning Python or using it for your small-sized projects as a beginner. 

Getting started
---------------

Your IDLE installation comes bundled with your Python installation. You can access it by using the Search feature in Windows or MacOS and typing up "IDLE" and starting it. 

When you open IDLE, you will see the following screen:

.. tab-set::

   .. tab-item:: Windows

        .. image:: images/idle_windows1.png
           :width: 550
           :align: center
           :alt: IDLE Shell

   .. tab-item:: MacOS

        .. image:: images/idle_mac1.png
           :width: 550
           :align: center
           :alt: IDLE Shell


The text you see indicates that you have opened a *Python Shell*, meaning that you are now working with an interpreter which will execute your commands, and is waiting for your input. You are also able to see your Python version. Try typing *print("Hello World!")* to the line starting with ">>>" and pressing Enter to see what happens!

Creating and running scripts
----------------------------

If you tried runing *print("Hello World!")*, you saw that IDLE executed your command and responded back by printing *Hello World!*. As the code you wanted to execute was a single line, it was very convenient to just type it up and give it to IDLE. However, when you have more complex jobs to do, it is not always convenient to provide multiple lines of code manually line by line, which makes it harder to program and also change your mistakes and typos. That's why we are able to create Python scripts to write our code and pass it to the Shell for it to execute. 

To create a Python script, go to *File > New File* in IDLE menu. 

.. tab-set::

   .. tab-item:: Windows

        .. image:: images/idle_windows2.png
           :width: 550
           :align: center
           :alt: IDLE Shell

   .. tab-item:: MacOS

        .. image:: images/idle_mac2.png
           :width: 450
           :align: center
           :alt: IDLE Shell


You should see a blank page waiting for you to write your code. As an example, try copying and pasting the following code to the textbox:


.. code-block:: Python

    # This program is for adding 2 numbers

    # Declaring the variables
    num1 = 18
    num2 = 29

    # Doing the addition
    sum = num1 + num2

    # Printing the sum
    print('Sum of {0} and {1} equals {2}'.format(num1, num2, sum))


.. tab-set::

   .. tab-item:: Windows

        .. image:: images/idle_windows3.png
           :width: 550
           :align: center
           :alt: IDLE Shell

   .. tab-item:: MacOS

        .. image:: images/idle_mac3.png
           :width: 550
           :align: center
           :alt: IDLE Shell

The program above is just a simple script which adds 2 numbers and prints the result of the sum. Notice how the title of the window changed from "untitled" to "\*untitled\*". This indicates that the script we have needs to be saved. Therefore, we now need to save our script. Go to *File > Save* to name and save your script at a convenient location in your computer. Let's name it *sum.py*.

.. tab-set::

   .. tab-item:: Windows

        .. image:: images/idle_windows4.png
           :width: 550
           :align: center
           :alt: IDLE Shell

   .. tab-item:: MacOS

        .. image:: images/idle_mac4.png
           :width: 550
           :align: center
           :alt: IDLE Shell


Now that we saved the file, we can run it. While you have the script open, at the top menu, go to *Run > Run Module* to run your script. When you run it, you should see the output "*Sum of 18 and 29 equals 47*".

We are also able to open Python scripts (which commonly end with the extension ".py") to open, edit and run any script we want to execute. To open a Python script and edit it, go to *File > Open...* and select your Python script. You can try to locate "*sum.py*" on your computer and open it to edit, and run it again by going to *Run > Run Module*. 

As you proceed with your journey in Python, you will probably have the need of an IDE with more integrated features such as extensions or source control. You can check our section on Visual Studio Code (VS Code) to learn more about another IDE with more capabilities.