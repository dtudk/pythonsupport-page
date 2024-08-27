IDLE
====

.. dropdown:: Video Tutorial
   :color: muted
   :open:

   .. raw:: html 
      
         <iframe src="https://panopto.dtu.dk/Panopto/Pages/Embed.aspx?id=81040637-95f5-4aa5-9133-b1ce0142fd86" height="405" width=100% style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>


.. include:: /_rst_includes/tip-copy.rst

:guilabel:`IDLE` is an integrated development environment (IDE) installed automatically with Python.
It provides you with an environment where you can write Python scripts and run them or write Python code line by line to execute immediately. 

:guilabel:`IDLE` is lightweight, simple, and great for introducing how to do coding projects. Therefore, it is well suited for beginners. 


.. warning::
   We only recommend introductory students to use IDLE while following :course-base:`02002`/:course-base:`02003`.

   There are other more advanced IDE's that has much greater functionality than IDLE.


Getting started
---------------


.. card::

   You can access :guilabel:`IDLE` by searching for `IDLE` in your search tab (both for {{ windows }} and {{ macos }}). 

   When you open :guilabel:`IDLE`, you will see the following screen:

   .. tab-set::
      :sync-group: os

      .. tab-item:: {{ windows }}
         :sync: windows

         .. image:: images/idle_windows1.png
            :width: 90%
            :align: center
            :alt: IDLE Shell


         The text you see indicates that you have opened a *Python Shell*. The lines starting with ">>>" are meant for Python code. Try typing or pasting in the following and press enter. 
   
         .. code:: python
               
            print("hello")

      .. tab-item:: {{ macos }}
         :sync: mac

         .. image:: images/idle_mac1.png
            :width: 90%
            :align: center
            :alt: IDLE Shell

         The text you see indicates that you have opened a *Python Shell*. The lines starting with ">>>" are meant for Python code. Try typing or pasting in the following and press enter. 
   
         .. code:: python
               
            print("hello")


Creating and running scripts
----------------------------

A Python *script* is a file with Python code. Once the script is *run*, all the code is executed. This is great for larger jobs and allows for reusage of your code. 

.. tab-set::
   :sync-group: os

   .. tab-item:: {{ windows }}
      :sync: windows

      #. Go to :menuselection:`File --> New File` in the IDLE menu to create a Python script. 

         .. image:: images/idle_windows2.png
            :width: 90%
            :align: center
            :alt: IDLE Shell

      #. You should see a blank page. Type or paste the following code 

         .. code:: python

            # This program is for adding 2 numbers

            # Declaring the variables
            num1 = 18
            num2 = 29

            # Doing the addition
            sum = num1 + num2

            # Printing the sum
            print(f"Sum of {num1} and {num2} equals {sum}")

         .. image:: images/idle_windows3.png
            :width: 90%
            :align: center
            :alt: IDLE Shell

      #. Go to :menuselection:`File --> Save As` and save the script as ``sum.py``

         .. image:: images/idle_windows4.png
            :width: 90%
            :align: center
            :alt: IDLE Shell

      #. Run the script.
         In the top menu, go to :menuselection:`Run --> Run Module` (or press :kbd:`F5`).
         You should now see some output. 


   .. tab-item:: {{ macos }}
      :sync: mac

      #. Go to :menuselection:`File --> New File` in the IDLE menu to create a Python script.

         .. image:: images/idle_mac2.png
            :width: 90%
            :align: center
            :alt: IDLE Shell

      #. You should see a blank page. Type or paste the following code 

         .. code:: python

            # This program is for adding 2 numbers

            # Declaring the variables
            num1 = 18
            num2 = 29

            # Doing the addition
            sum = num1 + num2

            # Printing the sum
            print(f"Sum of {num1} and {num2} equals {sum}")

         .. image:: images/idle_mac3.png
            :width: 90%
            :align: center
            :alt: IDLE Shell

      #. Go to :menuselection:`File --> Save As` and save the script as ``sum.py``

         .. image:: images/idle_mac4.png
            :width: 90%
            :align: center
            :alt: IDLE Shell

      #. Run the script.
         In the top menu, go to :menuselection:`Run --> Run Module` (or press :kbd:`F5`).
         You should now see some output. 


You can now modify and run the script as much as you want.

As mentioned, the IDLE is best suited for simple projects. Later during the 1\ :sup:`st` semester
you will be introduced to Visual Studio Code.

