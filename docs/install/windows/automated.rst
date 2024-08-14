.. _automated-reference-windows:

{{ windows_icon }}  --- Automated Installation
==========================================================

.. button-link:: ../macos/automated.html
   :align: right
   :color: primary
   
    Press here for {{ macos }} {{ apple_icon }}


Install everything at once
----------------------------

.. card:: 

    #. 
        Open PowerShell as an administrator by opening the menu bar, then search for :menuselection:`Windows PowerShell`.
        

    #.

        Once you see Windows PowerShell, on the right hand side you can select *Run as administrator*. If not, right-click the
        icon and select :menuselection:`Run as administrator`. 

        .. image:: /images/install/windows-ps-run-admin.png
            :width: 400
            :align: center

    #. 
        Copy the following line of code into your terminal and press enter:

        .. code-block:: pwsh

            PowerShell -ExecutionPolicy Bypass -Command "& {Invoke-Expression (Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/dtudk/pythonsupport-scripts/main/Windows_AutoInstall.ps1' -UseBasicParsing).Content}"

        .. tip::
            You can copy and paste all code in the gray code blocks above by hovering your mouse over the block and pressing the icon in the top right.


    #.
        Wait until you see ``Script finished``

    .. tip::
        When you have finished the guide, we **strongly recommend** checking out the :ref:`Python Essentials <essentials-reference>` to prepare you for coding.



.. include:: verify.rst
