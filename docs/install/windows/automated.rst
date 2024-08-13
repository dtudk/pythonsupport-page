.. _automated-reference-windows:

{{ windows_icon }}  --- Automated installation guide
==========================================================

.. button-link:: ../macos/automated.html
   :align: right
   :color: primary
   
    Press here for {{ macos }} {{ apple_icon }}

.. todo::
    Change color?

#. 
    The first thing you need to do is to open PowerShell as an administrator. This can be done
    by opening the menu bar, then search for :menuselection:`Windows PowerShell`.
    Once you see Windows PowerShell, on the right hand side you can select *Run as administrator*. If not, right-click the
    icon and select :menuselection:`Run as administrator`. 

    .. todo::
        insert image of how to open PowerShell as described above.

#. 
    Next you need to copy the following line of code into your terminal and press enter:

    .. tip::
        You can copy and paste all code in the gray code blocks below by hovering your mouse over the block and pressing the icon in the top right.

    .. code-block:: bash

        PowerShell -ExecutionPolicy Bypass -Command "& {Invoke-Expression (Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/dtudk/pythonsupport-scripts/main/AutoInstallWindows.ps1' -UseBasicParsing).Content}"


#.
    Wait until you see ``Script finished``

.. tip::
    When you have finished the guide, we **strongly recommend** checking out the :ref:`Python Essentials <essentials-reference>` to prepare you for coding.


.. include:: verify.rst
