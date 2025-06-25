Uninstalling Python
=========================================


.. note::

   If you are running Python using Miniconda, you will have to :ref:`uninstall Miniconda <uninstall-conda>`. 



Deleting Python might be helpful in the following scenarios. 

* Your current Python installation is not working correctly. 
* You have several versions of Python that conflict with each other. 
* You have tried to install Python, but something went wrong, and you want to start from scratch. 

Follow the steps below to delete Python. 

A version of Python comes pre-installed with {{ macos }}. The operating system uses this version of Python and should *not* be deleted.
Other versions of Python may be deleted using a script supplied here.
This may include versions installed from the official Python website, Anaconda or Miniconda.

The deletion script can be :download:`downloaded here </_downloads/deletePythonMac.sh>`.
Be sure to place the downloaded script on your *Desktop*.

Once you have downloaded and placed it on the *Desktop*, open a terminal (:kbd:`Command+Space`, then type ``terminal`` :kbd:`Enter`).

Then run the following command by copying, pasting into your terminal, and pressing :kbd:`Enter`:

.. code:: bash

   cd ~/Desktop
   bash deletePythonMac.sh

The script will ask you for your system password. Enter it and press :kbd:`Enter` (You will not be able to see your password as you type it).
The script will then delete all versions of Python that you have installed on your computer.

.. warning::

   This will delete all versions of Python installed on your computer,
   including packages installed using ``pip`` or ``conda install``.

