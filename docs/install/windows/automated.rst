.. _automated-reference-windows:

{{ windows_icon }}  --- Automated installation guide
==========================================================

.. button-link:: ../macos/automated.html
   :align: right
   :color: primary
   
    Press here for macOs {{ apple_icon }}

.. todo::
    Change color?
#. 

    The first thing you need to do is to open PowerShell as an administrator. This can be done
    by opening the menu bar, then search for *Windows PowerShell*. Once you see Windows
    PowerShell, on the right hand side you can select *Run as administrator*. If not, right-click the
    icon and select *Run as administrator*. 

    .. todo::
        insert image of how to open PowerShell as described above.

#. 
    Next you need to copy the following line of code into your terminal and press enter:

    .. tip::
        You can copy and paste all code in the grey code blocks below by hovering your mouse over the block and pressing the icon in the top right.

    .. code-block:: bash

        PowerShell -ExecutionPolicy Bypass -Command "& {Invoke-Expression (Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/dtudk/pythonsupport-scripts/main/AutoInstallWindows.ps1' -UseBasicParsing).Content}"


#.
    Wait until you see *Script finished*

.. tip::
    When you have finished the guide, we **strongly recommend** checking out the :ref:`Python Essentials <essentials-reference>` to prepare you for coding.

Verification and Quick Troubleshooting
--------------------------------------
To ensure that your installation is working correctly, please go through the following steps.
Open up PowerShell again. if you see ``(base)`` next to your username, you can proceed. If unsure see the image bellow:

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
