.. _manual-reference-windows:

Windows - Manual installation guide
===================================

.. button-ref:: package-managed-reference-macos
   :ref-type: ref
   :color: info

   .. raw:: html

      <i class="fa-brands fa-windows"></i> Not using **Windows**? Press here for **MacOS** guides.

.. dropdown:: Video guide
    :color: info

    .. raw:: html
    
        <iframe src="https://panopto.dtu.dk/Panopto/Pages/Embed.aspx?id=e5e4bea0-13f2-4b1e-85cd-b1c800e7391c&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&captions=false&interactivity=all" height=100%  style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>


    


.. todo::
    Change color?

Step 1: Install Miniconda
--------------------------

First thing you need to do is download Miniconda. This is done by going to `this website  <https://docs.anaconda.com/miniconda/index.html#latest-miniconda-installer-links>`_, and downloading the appropriate installer for your system.
Under the title "Latest Miniconda installer links", you will see different installers where you will have to download the correct one.
Here you need to click and download Miniconda3 Windows 64-bit.

.. image:: /images/install/windows-fully-manual-miniconda.png
    :width: 400
    :align: center


Then you need to follow the instructions during the installations. Make sure to cross of all the
options regarding **PATH** as shows below.

.. todo::
    Insert image showing **PATH** checkboxes when downloading miniconda on windows


Step 2: Install Python:
-------------------------

Now you need to open you PowerShell as an administrator and run the following commands in PowerShell one at a time by pasting them into the terminal and pressing enter.

If you are unsure on how to open PowerShell, it can be done by opening the menu bar and searching
for Windows PowerShell. Once you see Windows PowerShell, on the right hand side you can select
Run as administrator. If not, right-click on the icon and select Run as administrator as shown bellow. 

.. todo::
    Insert image showing how to open the windows PowerShell as described above.


.. tip::
    You can copy and paste all code in the grey code blocks below by hovering your mouse over the block and pressing the icon in the top right.

.. code-block:: bash

    conda install python=3.11 -y

.. code-block:: bash

    conda install -c conda-forge dtumathtools uncertainties -y

Step 3: Install VS Code:
-------------------------

After the installation is finished, you need to download Visual Studio Code. This is done by going
to `this website  <https://code.visualstudio.com>`_. Click the download button and follow the instructions.

.. image:: /images/install/windows-fully-manual-vsc-webpage.png
      :width: 500
      :align: center
      

Step 4: Install extensions for Visual Studio Code
-------------------------------------------------

.. |extensions| image:: /images/install/extensions.png
    :height: 25px


Open Visual Studio Code and select the Extensions |extensions| tab on the left. Here search for Python, and
download the extension. Make sure that it's from Microsoft. Hereafter search for Jupyter, and
download that extension as well. This also needs to be from Microsoft.

.. image:: /images/install/macos-package-managed-python.png
      :width: 200
      :align: center

.. image:: /images/install/macos-package-managed-jupyter.png
      :width: 200
      :align: center


.. tip::
    When you have finished the guide, we **strongly recommend** checking out the :ref:`Python Essentials <essentials-reference>` to prepare you for coding.

Verification and Quick Troubleshooting
--------------------------------------
To ensure that your installation is working correctly, please go through the following steps.
Open up PowerShell again. If you see ``(base)`` next to your username, you can proceed. If unsure see the image bellow:

.. todo::
    Insert image of the PowerShell with (base) next to the username

Otherwise do the following:

• Search for Miniconda PowerShell promt on your computer and open it up. (if you cannot find it, try to install Miniconda again)
• After opening the Miniconda shell, type ``conda init`` and press enter.
• Open up PowerShell again and verify that you now see ``(base)``.
• Finally type ``idle`` in PowerShell and press enter. This should open up a new window in which you will able to run python code.

Now ensure the following:

• It says Python 3.11.xx in the top left.
• You get no errors when typing ``import dtumathtools, uncertainties`` and press enter. This should open a new line without any text, as shown bellow.

.. todo::
    Insert image of ``idle`` after import dtumathtools and uncertainties so they can see what it should look like.


If it is not the case for one of the above, try to paste the following line of code in PowerShell and press enter:

.. code-block:: bash

     conda install -c conda-forge python=3.11 dtumathtools uncertainties -y


If you are still having trouble or have any questions please do not hesitate visiting us at our office hours, or contact us via email or Discord. More information can be found at our :ref:`homepage <reach-us-reference>`.
