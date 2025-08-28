.. _automated-reference-windows:

{{ windows_icon }}  --- Automated Installation
===============================================

.. dropdown:: {{ video_install }}
    :open:
    :color: info

    .. raw:: html

        <iframe src="https://panopto.dtu.dk/Panopto/Pages/Embed.aspx?id=7ec56b9b-895a-4ad8-b617-b34700a303bb" height="405" width=100% style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>


Install everything at once
---------------------------------------------------

.. card:: 
   
   Installs all packages and tools required for the 1\ :sup:`st` year
   Polytechnical Foundation courses at DTU. 

   #. 
       Open PowerShell as an `Administrator` by opening the menu bar, then search for :menuselection:`Windows PowerShell`.

   #.
       Once you see Windows PowerShell on the right-hand side, you can select :menuselection:`Run as Administrator`.
       If not, right-click the icon and select :menuselection:`Run as Administrator`. 

       .. image:: /images/install/windows-ps-run-admin.png
          :width: 400
          :align: center

   #. 
       Copy the following line of code into the PowerShell window and press :kbd:`Enter`.

       **Note**: please copy *the entire line*.

       .. code-block:: pwsh

          PowerShell -ExecutionPolicy Bypass -Command "& {Invoke-Expression (Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/dtudk/pythonsupport-scripts/main/Windows/install.ps1' -UseBasicParsing).Content}"

       .. include:: /_rst_includes/tip-copy.rst

   #.
       The script has finished when you see something like:

       .. code-block:: bash

          Script has finished. You may now close the terminal...

       Now, Python and Visual Studio Code will be ready to use.

       .. note::

          During the installation, you will see warnings and caveats, etc.
          The script will resolve these automatically.
          Please let the script finish.


.. include:: /_rst_includes/tip-finish.rst

.. include:: verify.rst
