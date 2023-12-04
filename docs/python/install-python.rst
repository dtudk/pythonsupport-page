.. _install-python:

Official Python 
=================

.. admonition:: Remove older Python versions
   :class: dropdown warning

   We suggest removing any pre-installed Python versions and VS Code before 
   proceeding with this guide to ensure a smooth installation process.
   For help with this process, take a look at the section on `Deleting multiple versions of python <Deleting multiple versions of python>`_.



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

            However, if you find yourself on an adventurous detour and can't access it there, you can still opt for the `official Python release <{{python_org_rec}}>`_.

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

            You can download the official python directly from `here <{{python_org_rec}}/>`_.
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


Verifying installation
======================

To verify if python is installed correctly follow the steps below:  


.. tab-set::

   .. tab-item:: {{ windows }}
      :sync: win

      #. Give your keyboard's window key a friendly nudge.  
      #. Type ``powershell`` in the search bar, and hit enter to launch PowerShell.
      #. In the powershell window, type ``python --version``
      #. If you spot the ``Python x.xx.x`` smiling back at you, you're all set! You've got a Python in your machine |:snake:|.  

   .. tab-item:: {{ macos }}
      :sync: mac

      #. Give your keyboard's ``Command`` key a friendly nudge.
      #. Type ``terminal`` in the search bar, and press Enter to open Terminal.
      #. In the Terminal window, type ``python3 --version``
      #. If you see the ``Python x.xx.x`` smiling back at you, you're all set! You've got a Python friend on your machine |:snake:|.

   .. tab-item:: {{ linux}}
      :sync: linux

      #. Open a terminal
      #. In the Terminal window, type ``python3 --version``
      #. If you see the ``Python x.xx.x`` smiling back at you, you're all set! You've got a Python friend on your machine |:snake:|.

