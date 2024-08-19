.. _automated-reference-windows:

{{ windows_icon }}  --- Automated Installation
===============================================

.. button-ref:: ../macos/automated
   :ref-type: doc
   :align: right
   :color: primary
   
    Press here for {{ macos }} {{ apple_icon }}


.. dropdown:: Video Guide
    :open:
    :color: info

    .. raw:: html 
    
        <iframe src="https://panopto.dtu.dk/Panopto/Pages/Embed.aspx?id=ffbe8bb5-accc-4bf1-be87-b1ce00aa5a97&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&captions=false&interactivity=all" height="405" width=100% style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>


Install everything at once
---------------------------------------------------

.. card:: 

    #. 
        Open PowerShell as an Administrator by opening the menu bar, then search for :menuselection:`Windows PowerShell`.
        

    #.
        Once you see Windows PowerShell, on the right hand side you can select *Run as Administrator*. If not, right-click the
        icon and select :menuselection:`Run as Administrator`. 

        .. image:: /images/install/windows-ps-run-admin.png
            :width: 400
            :align: center

    #. 
        Copy the following line of code into the PowerShell window and press :kbd:`Enter`:

        .. code:: pwsh

            PowerShell -ExecutionPolicy Bypass -Command "& {Invoke-Expression (Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/dtudk/pythonsupport-scripts/main/Windows_AutoInstall.ps1' -UseBasicParsing).Content}"

        .. include:: /_rst_includes/tip-copy.rst

    #.
        Wait until you see ``Script finished``

.. include:: /_rst_includes/tip-finish.rst

.. include:: verify.rst
