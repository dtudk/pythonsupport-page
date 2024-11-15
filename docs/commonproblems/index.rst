.. _common_problems:

Common Problems
================


Here you will find some quick fixes for common problems and errors

Problems with Python and its Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. dropdown:: "The term import is not recognized..."

    It is likely that Python code is being run in the terminal and not in the Python interpreter. To fix this, run the code in the Python interpreter either by running `python` in the terminal or by running the code in a Python script.
    
    Terminal example:
    =================

    .. code-block:: bash

        % import "module_name"
        import: The term import is not recognized as the name of a cmdlet, function, script file, or operable program. 
        Check the spelling of the name, or if a path was included, verify that the path is correct and try again.

        % python
        Python 3.9.7 (default, Sep 16 2021, 16:59:01) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import "module_name"
        >>>

    


.. dropdown:: "unable to initialize device PRN"

    It is likely that Python code is being run in the terminal and not in the Python interpreter. To fix this, run the code in the Python interpreter either by running `python` in the terminal or by running the code in a Python script.
    
    Terminal example:
    =================

    .. code-block:: bash

        % print("Hello, World!")
        unable to initialize device PRN

        % python
        Python 3.9.7 (default, Sep 16 2021, 16:59:01) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>> print("Hello, World!")
        Hello, World!
        >>>


.. dropdown:: "urllib2.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]..."

    This is likely due to missing certificates in the Python installation. 
    
    To fix this:

    1. Open Finder or file browser press the Apps or Applications folder to the left.

    2. Find the Python 3.X folder.

    3. Locate the file name “Install Certificates.com” and and press it, it will quickly run a terminal command to install the certificates.

    (Optional) Another fix could be to install the certifi package from pip by running ``pip3 install certifi`` in the terminal.


.. dropdown:: Local TeX Live (2023) is older than remote repository (2024)

    This is due to the TeX Live version being outdated. To fix this reinstall TeX Live with the latest version.

.. dropdown:: Getting requirements to build editable did not run successfully

    This is likely due to corrupt files inside the folder. To fix this remove the corrupt files and try again.

.. dropdown:: "Error loading webview: Error: Could not register service workers: InvalidStateError: Failed to register a ServiceWorker: The document is in an invalid state"

    This problem is likely due to the Visual Studio Code cache. To fix this, clear the cache by follwing the steps below:

    .. tab-set::

        .. tab-item:: Windows

            1. Close VSCode and kill any background processes running in the task manager.

            2. Go to the file explorer and to the path :file:`C:\Users\<user_name>\AppData\Roaming\Code` and clear the contents of the folders Cache, CachedData, CachedExtensions, CachedExtensionVSIXs (if this folder exists) and Code Cache.

            3. Restart VSCode.

        .. tab-item:: MacOS

            1. Close VSCode and kill any background processes running in the task manager.

            2. Go to the file explorer and to the path :file:`/Users/<user_name>/Library/Application Support/Code` and clear the contents of the folders Cache, CachedData, CachedExtensions, CachedExtensionVSIXs (if this folder exists) and Code Cache.

            3. Restart VSCode.

        .. tab-item:: Linux

            1. Close VSCode and kill any background processes running in the task manager.

            2. Go to the file explorer and to the path :fil:`/home/<user_name>/.config/Code` and clear the contents of the folders Cache, CachedData, CachedExtensions, CachedExtensionVSIXs (if this folder exists) and Code Cache.

            3. Restart VSCode.
      

.. dropdown:: "OSError: [Error 86] Bad CPU type in executable: <path_to_cbc_binaries> "

    This is due to Pulp complaining about bad CPU type on arm Mac as cbc (pulp dependency) doesn't have arm binaries. This can be fixed using rosetta translation layer. Run the following command in the terminal:

    .. code-block:: bash

        /usr/sbin/softwareupdate --install-rosetta --agree-to-license 

.. dropdown:: While loop getting stuck in IDLE

    This is a problem native to the installation, which occur in all version of idle from 11.4 and newer. This can be solved by downgrading the idle version, by running the following command in the terminal:

    .. code-block:: bash

        conda install python=3.11.3
 

.. dropdown:: "OSError: ... Error loading ....\lib\fbgemm.dll.."

    This is a windows specific error. This happens because of a problem that is related to the released torch version and is likely due to a conflict between pip and conda. To fix this, uninstall the torch package and reinstall it using conda:

    .. code-block:: bash

        pip uninstall torch
        conda install -c pytorch pytorch==2.4.0


Problems with Conda and Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. dropdown:: Incompatible Architecture

    This is common when switching computers and transferring files through one drive and icloud.
    The solution is the same on MacOS, Linux and Windows:

    .. code-block:: bash
        
        conda install --upgrade --force-reinstall <package>


.. dropdown:: "Module not found... " or "No Module Named"

    If you have not previously installed the package the solution is to open your `Terminal` and write:

    .. code-block:: bash
        
        conda install <package>


.. dropdown:: "Module not found" - when you've installed the module

    If you have installed the package before, you need to change your kernel.
    If you are using a `Jupyter Notebook` you have to go to the to right corner, where it says `Python 3.XX.XX` (this is the python version you are using). You need to click on it, after which a dropdown will come down.
    Here you need to click `Select Another Kernel...` -> `Python Environments` -> `base (Python 3.11.XX)`.
    This will open the Python downloaded using our installation guides.

    If you are using a normal Python script, go to the bottom right corner. Her it will only show the Python version, for example `3.12.XX 64-bit`. You need to click this, after which a dropdown will come down. Here you can see your Python versions. If you want to use the version installed using our guides, select `Python 3.11.XX ('base')`. 


.. dropdown:: Sympy pretty print not functioning properly

    When using sympy and the printing does not work after writing:

    .. code-block:: python

        import sympy as*
        init_printing()

    Most of the cases can be solved by wrinting the following in stead:

    .. code-block:: python

        import sympy as*
        init_printing(use_latex='mathjax')


.. dropdown:: Multiple conda installations

    If you have multiple installations of conda we highly recommend that you uninstall Anaconda using `this link <https://pythonsupport.dtu.dk/uninstall/conda.html>`__ .



Problems with Visual Studio Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. dropdown:: EPERM: Operation Not Permitted

    This error occurs when your folder is in restricted mode, when you do not have access to the folder or when the folder is not trusted. To fix this:

    1. Check if the folder is in restricted mode. If it is, change the permissions.

    2. Check if you have access to the folder. If you do not, ask the owner for access.

    3. Check if the folder is trusted. If it is not, make sure that VS Code is allowed to access the folder.




.. dropdown:: "Module not found... "


    This error occurs when you either have not installed the module or when the module is installed in a different environment. To fix this:

    1. Try to import the module in another environment (see :ref:`here <learn-more-vscode-script-select-interpreter>`).

    2. If the module is not installed, install it using the command ``conda install module_name``.


.. dropdown:: Missing "Run and debug" in Python files

    This error occurs when you have not installed the Python extension. To fix this:

    1. Install the Python extension by clicking on the Extensions icon in the Activity Bar on the side of the window, searching for Python, and clicking on the Install button.

    2. If it still does not work, right-click on the three dots in the upper right corner next to where the run and debug button normally is. Then make sure that the run and debug have a checkmark.

    .. image:: /commonproblems/images/Run-and-debug.png
        :alt: Run and Debug
        :align: center
        :width: 400px



