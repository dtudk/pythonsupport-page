IDLE
====

.. tip::
    You can copy and paste all code in the grey code blocks below by hovering your mouse over the block and pressing the icon in the top right.

IDLE is an integrated development environment (IDE) that is installed automatically with Python. It provides you with an environment where you can write Python scripts and run them, or you can write Python code line by line to execute immediately. 

IDLE is lightweight, simple and great for smaller coding projects. Therefore it is well suited for beginners. 

Getting started
---------------


.. card::

   You can access IDLE by searching for "IDLE" in your search tab on both windows and macOS. 

   When you open IDLE, you will see the following screen:

   .. tab-set::

      .. tab-item:: Windows


         .. image:: images/idle_windows1.png
            :width: 550
            :align: center
            :alt: IDLE Shell


         The text you see indicates that you have opened a *Python Shell*. The lines starting with ">>>" are meant for Python code. Try typing or pasting in the following and press enter. 
   
            .. code-block:: Python
               
               print("Hello World!")

      .. tab-item:: MacOS

         .. image:: images/idle_mac1.png
            :width: 550
            :align: center
            :alt: IDLE Shell

         The text you see indicates that you have opened a *Python Shell*. The lines starting with ">>>" are meant for Python code. Try typing or pasting in the following and press enter. 
   
            .. code-block:: Python
               
               print("Hello World!")




Creating and running scripts
----------------------------

A Python *script* is a file with Python code. Once the script is *run* all the code is executed at once. This is great for larger jobs and allows for reusage of your code. 

.. tab-set::


   .. tab-item:: Windows

      #. To create a Python script, go to *File > New File* in IDLE menu. 

         .. image:: images/idle_windows2.png
            :width: 550
            :align: center
            :alt: IDLE Shell

      #. You should see a blank page. Type or paste the following code 

         .. code-block:: Python

            # This program is for adding 2 numbers

            # Declaring the variables
            num1 = 18
            num2 = 29

            # Doing the addition
            sum = num1 + num2

            # Printing the sum
            print('Sum of {0} and {1} equals {2}'.format(num1, num2, sum))

         .. image:: images/idle_windows3.png
            :width: 550
            :align: center
            :alt: IDLE Shell

      #. Go to *File* > *save as* and save the script as *sum.py*

          .. image:: images/idle_windows4.png
           :width: 550
           :align: center
           :alt: IDLE Shell

      #. Run the script.
         In the top menu, go to *run* > *run module*. You should now get some output. 


   .. tab-item:: MacOS

      #. to create a Python script, go to *File > New File* in the IDLE menu. 

         .. image:: images/idle_mac2.png
            :width: 550
            :align: center
            :alt: IDLE Shell

      #. You should see a blank page. Type or paste the following code 

         .. code-block:: Python

            # This program is for adding 2 numbers

            # Declaring the variables
            num1 = 18
            num2 = 29

            # Doing the addition
            sum = num1 + num2

            # Printing the sum
            print('Sum of {0} and {1} equals {2}'.format(num1, num2, sum))

         .. image:: images/idle_mac3.png
            :width: 550
            :align: center
            :alt: IDLE Shell

      #. Go to *File* > *save as* and save the script as *sum.py*

          .. image:: images/idle_mac4.png
           :width: 550
           :align: center
           :alt: IDLE Shell

      #. Run the script.
         In the top menu, go to *run* > *run module*. You should now get some output. 



You can now modify and run the script as much as you want. The advantage here, is that the code can be modified and used without having to type at all.

As mentioned, the IDLE is best suited for simple projects. Around week 8 you will probably start using VS Code. 