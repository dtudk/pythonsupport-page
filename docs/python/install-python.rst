.. _install-python:

Official Python {{pref_symbol}} 
=====================================

.. tip::

   DTU recommends using version {{ python_version }} of Python.

   It is recommended to not have more Python versions installed (unless you feel confident in
   selectively using explicit versions).

   We suggest removing any pre-installed Python versions before 
   proceeding with this guide to ensure a smooth installation process.
   For help with this process, take a look at :ref:`this section <uninstall-python>`.



Download & Installation
-----------------------

.. admonition:: Do not install Python 3.12 or later
   :class: dropdown warning

    For the time being, we recommend **not** downloading version 3.12 (or later) of Python. This is because some of the course dependencies does not yet work with said versions.

.. tab-set::

   .. tab-item:: {{ windows }}
      :sync: win

      .. tab-set::

         .. tab-item:: App Store {{pref_symbol}}
            :sync: py-1st

            Installing Python through the App Store is by far the easiest!

            Search for `Python` in the store and select a suitable version (for instance `this <https://www.microsoft.com/store/productid/9NRWMJP3717K?ocid=pdpshare>`_).

            Alternatively you can open a terminal (press :kbd:`Win-R`, type ``cmd`` and :kbd:`Enter`) then type ``python`` and
            :kbd:`Enter` which should open up the App store where Python can be selected, remember to select the correct version!

         .. tab-item:: python.org
            :sync: py-2nd

            However, if you find yourself on an adventurous detour and can't access it there, you can still opt for the `official Python release <python-org-rec_>`_.

            Download the **64bit** version.

            **Just remember to check the Add Python to PATH box (at the bottom of the installation GUI)**.

            .. image:: images/python-win-step-1.png
                :width: 600px
                :align: center
                :alt: Add to path checkbox


   .. tab-item:: {{ macos }}
      :sync: mac

      .. tab-set::

         .. tab-item:: Homebrew {{pref_symbol}}
            :sync: py-1st

            Launch a :ref:`terminal <os-terminal>` (press :kbd:`Command-Space`),
            and execute the following code:

            .. code-block:: bash
            
               _TMP_FILE=$(mktemp) && /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" | tee >(grep "brew shellenv" | tee $_TMP_FILE) && eval "$(cat $_TMP_FILE)" && (echo; cat $_TMP_FILE >> $HOME/.profile) && brew install python

            Press :kbd:`Enter`, and after some moments it will ask you to **Press RETURN/ENTER**
            again. Once done, you will have Homebrew *and* Python.

            See `here <https://brew.sh/>`__ for more details on Homebrew.
            

         .. tab-item:: python.org
            :sync: py-2nd

            You can download the official python directly from `here <python-org-rec_>`_.
            After downloading the installer, the installation process should be relatively straightforward.

            Once installed, check it works. If it doesn't *and* you have an M1/M2/MX processor, you might
            need to use Rosetta to enable it:

            `Rosetta 1 or 2 <https://support.apple.com/en-gb/HT211861>`__.
            You can figure this out by pressing the Apple icon (top left)
            and then ``About this Mac``/``Om denne Mac``.

            If there are problems, a more detailed instruction can be found
            `here <https://www.dataquest.io/blog/installing-python-on-mac/>`__.

            If you still have problems, please contact us at :mail:`pythonsupport@dtu.dk`.

   .. tab-item:: {{ linux }}
      :sync: linux

      Almost all Linux distributions ships a Python at its core. If not, use your
      distributions package manager to install Python

      Something like:

      .. code-block:: bash

         # the exact package manager, or package name is distro dependent
         sudo apt install python3


.. _install-python-packages:

Installing packages
--------------------

.. admonition:: Unsure what a *terminal* is?
   :class: dropdown info

   Please head over :ref:`here <os-terminal>` to understand how to open and use a terminal.

Using this installation will require you to use :ref:`pip` (see link for more details).
Open up a terminal and run the following: 

.. tab-set::

   .. tab-item:: {{ win_powershell }}
      :sync: powershell

      .. code-block:: powershell

         python -m pip install numpy

   .. tab-item:: {{ mac_bash }}
      :sync: mac

      .. code-block:: bash

         python3 -m pip install numpy

   .. tab-item:: {{ linux_bash }}
      :sync: bash

      .. code-block:: bash

         python3 -m pip install numpy


Replace ``numpy`` by the package name you wish to install.

.. admonition:: Seeing ``(mach-o file, but is an incompatible architecture ...``?
   :class: dropdown warning

   If you get the error message ending in

   .. code-block:: shell
   
      (mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64'))``,

   Then run the following command:

   .. tab-set::

      .. tab-item:: {{ win_powershell }}
         :sync: powershell

         .. code-block:: powershell

            pip install --upgrade --force-reinstall numpy

      .. tab-item:: {{ mac_bash }}
         :sync: mac

         .. code-block:: bash

            pip3 install --upgrade --force-reinstall numpy

      .. tab-item:: {{ linux_bash }}
         :sync: bash

         .. code-block:: bash

            pip3 install --upgrade --force-reinstall numpy
