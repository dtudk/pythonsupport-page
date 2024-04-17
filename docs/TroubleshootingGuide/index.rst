Troubleshooting Guide
=======================

.. tip::
    You can copy the code in the grey code blocks below by hovering your mouse over it and pressing the icon that appears in the top right of the block.

If you are having issues with Python, it could be a problem with how it has been installed. Here are some common errors/and tips that may be an easy fix:

* **Check that conda is installed**
    | Try to search for conda on your pc.
    | It is also a good idea to open a terminal and simply type ``conda`` and pressing enter. If conda is not installed this will give you an error message.
    | If you do not have conda installed it can be installed by going to the following webpage and following the instructions for miniconda:
    | `conda website <https://docs.anaconda.com/miniconda/>`_

* **Check that conda has been allowed to run**
    | Sometimes you need to run "conda init" in a terminal before conda can be used.
    | On MacOS, you can simply open a terminal, type ``conda init`` and press enter.
    | On Windows you must open an **Anaconda prompt**, type ``conda init`` and press enter.
    | The anaconda prompt can be found in the search bar on Windows.

* **Check that python has been installed**
    | In your terminal simply type "conda install python 3.11" and press enter.



**Windows only issues:**

* **Execution Policy**
    | You may have gotten an error message saying something about your execution policy.
    | To fix this, start by searching for "Windows PowerShell" in the search bar, rightclicking the icon and selecting "Run As Administrator".
    | The execution policy can be changed by running the following code:
    .. code-block:: javascript

        Set-ExecutionPolicy Unrestricted

        
    | If you are still having issues try to instead set the execution policy to Unrestricted by running the following code:
    .. code-block:: javascript

        Set-ExecutionPolicy RemoteSigned

* **Long path support:**
    | If you have received an error message about long paths search for "Windows PowerShell" in search tab, rightclick the icon, select "Run As Administrator".
    | Paste in the following code and press enter:

    .. code-block:: javascript

        New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force








