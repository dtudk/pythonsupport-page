.. _automated-reference-windows:

Windows - Automated installation guide
================================

.. note::
    Not using **Windows**? The automated installation guide for **MacOS** can be found :ref:`here <automated-reference-MacOS>`.

.. tip::
    You can copy and paste all code in the grey code blocks below by hovering your mouse over the block and pressing the icon in the top right.


#. 

    The first thing you need to do is to open Powershell as an administrator. This can be done
    by opening the menu bar, then search for *Windows Powershell*. Once you see Windows
    Powershell, on the right hand side you can select *Run as administrator*. If not, right-click the
    icon and select *Run as administrator*

#. 
    Next you need to copy the following line of code into your terminal and press enter:

    .. code-block::

        PowerShell -ExecutionPolicy Bypass -Command "& {Invoke-Expression (Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/dtudk/pythonsupport-scripts/main/AutoInstallWindows.ps1' -UseBasicParsing).Content}"

#.
    Wait until you see *Script finished*

.. tip::
    When you have finished the guide, we **strongly recommend** checking out the :ref:`Python Essentials <essentials-reference>` to prepare you for coding.

Verification and Quick Troubleshooting
--------------------------------------
To ensure that your installation is working correctly, please go through the following steps.
Open up PowerShell again. if you see (base) next to your username, you can proceed. Otherwise do the following:

• Search for Miniconda PowerShell promt on your computer and open it up. (if you cannot find it, try to install Miniconda again). Information on how to install conda can be found :ref:`here <manual-reference-windows>`
• After opening the Miniconda shell, type the following and press enter conda init.
• Open up PowerShell again and verify that you now see (base).
• Finally type ``idle`` in PowerShell and press enter. This should open up a new window in which you will able to run python code.

Now ensure the following:

• It says Python 3.11.xx in the top left.
• You get no errors when typing ``import dtumathools, uncertainties`` and press enter.(Nothing should happen)

If it is not the case for one of the above, try to paste the following line of code in PowerShell and press enter:

.. code-block::

     conda install -c conda-forge python=3.11 dtumathtools uncertainties -y

Once the script is finished, Python and Visual Studio Code will be ready to use.

Supporter's Notes
-----------------

You are always welcome to visit us at our office hours, or contact us via email or Discord. More information can be found at our :ref:`homepage <reach-us-reference>`.
