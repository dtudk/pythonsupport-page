Common Errors
==============

Windows Specific Errors 
--------------------------

Windows execution policy in PowerShell
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   
   Some times a Windows setup has disabled default execution
   policies.

   This happens when you find an error message looking like:

   .. code:: powershell

      AuthorizationManager check failed.
      At line:1 char:1
      + C:\scriptpath\scriptname.ps1
      + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          + CategoryInfo          : SecurityError: (:) [], PSSecurityException
          + FullyQualifiedErrorId : UnauthorizedAccess

   Or, something similar (depending on versions etc.)

   To enable execution do the following:

   1. Open PowerShell in administrator mode:
      Search for ``powershell`` in the windows search bar
   2. Select ``Run as administrator``
   3. Execute this code:

      .. code:: powershell

         Set-ExecutionPolicy Unrestricted

      **Important**: Press :kbd:`A` when asked (*not* :kbd:`Y`)!

   Restart any terminals (including VS Code) and try again.

   `Click here to get more information about execution policies <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies>`__.



``ImportError: DLL load failed ...``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   When importing ``dtumathtools`` some Windows machines are missing certain libraries.

   The error can look similar to this:

   .. code:: powershell

      ImportError: DLL load failed while importing _cext: The specified module could not be found

   1. `Click here <https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022>`__
      and download (most likely) the X64 one.
   2. Install the application
   3. Re-start your editor (or machine) and try again
      If it still does not work, then try the X86 version.
   4. If problems still occur, please write us at :mailto:`pythonsupport@dtu.dk|{{mailto_subject}}|{{mailto_body}}>`



``ERROR: Could not install packages due to an OSError: ...``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   The exact error message can look different depending on when you encounter this
   error.
   It happens because of a default limitation of 260 characters in file names.

   The remedy is quite simple, download :download:`this script </_downloads/Remove260CharacterPathLimit.reg>`
   and double-click it.

   Now try to install the packages again.



Setting default terminal in VS code ( {{windows}} )
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The default terminal in VS Code can be changed in the following way:

#. Open a terminal in VS Code 

#. Next to the ``+`` icon select the downwards arrow

#. Click :menuselection:`Select Default Profile`

#. Choose the terminal, that you wish to have as your default (Windows PowerShell is recommended)
