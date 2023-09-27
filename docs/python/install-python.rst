
.. _install-python:

Official Python distribution {{ pref_symbol }}
------------------------------------------------------

.. tip::

   DTU recommends using version {{ python_version }} of Python.

The `base Python <python-org_>`_ software can be downloaded and installed through
their `download page <python-org-down_>`_ and uses common installation processes.

Installing the official Python distribution forces you to choose a version, and continuously use that version. I.e. upgrading to
a new Python version requires re-installing a new version, starting from downloading a new installer
and subsequently installing packages, again, through :ref:`pip <pip>`.


.. tab:: {{ windows }}

   Here are the suggested (in priority order) ways of installing Python:

   1. **Windows 10 and above** {{pref_symbol}}: Launch a :ref:`terminal <os-terminal>`
      (press :kbd:`Win-R`, type ``cmd`` and :kbd:`enter`), and type ``python``
      If it runs the Python interpreter it is already installed, if not an ``App store``
      pane will open up, asking if you want to install Python, simply press install
      and continue. It will select the latest stable release which is good!

   2. Download and install Python from `here <python-org-down-win_>`__
      Select the **64bit** version.
      Ensure you check :far:`square-check` the
      ``Add Python {{ python_version }} to PATH``
      (at the bottom of the installation GUI)

.. tab:: {{ macos }}

   Here are the suggested (in priority order) ways of installing Python:

   1. **Homebrew** {{pref_symbol}}: Launch a :ref:`terminal <os-terminal>` (press :kbd:`Command-Space`),
      and execute the following code:

      .. code-block:: bash
      
         _TMP_FILE=$(mktemp) && /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" | tee >(grep "brew shellenv" | tee $_TMP_FILE) && eval "$(cat $_TMP_FILE)" && (echo; cat $_TMP_FILE >> $HOME/.profile) && brew install python

      Press :kbd:`Enter`, and after some moments it will ask you to **Press RETURN/ENTER**
      again. Once done, you will have Homebrew *and* Python.

      See `here <https://brew.sh/>`__ for more details on Homebrew.

   2. 
      - Download and install Python from `here <python-org-down-mac_>`__
      - Once installed, check if Python works (see further down)
      - If Python does not work *AND* if you have an M1 or M2 processor,
         you might need the
         `Rosetta 1 or 2 <https://support.apple.com/en-gb/HT211861>`__.
         You can figure this out by pressing the Apple icon (top left)
         and then ``About this Mac``/``Om denne Mac``.

      If there are problems, a more detailed instruction can be found
      `here <https://www.dataquest.io/blog/installing-python-on-mac/>`__.

      If you still have problems, please contact us at :mail:`pythonsupport@dtu.dk`.

.. tab:: {{ linux }}

   Almost all Linux distributions ships a Python at its core. If not, use your
   distributions package manager to install Python

   Something like:

   .. code-block:: bash

      # the exact package manager, or package name is distro dependent
      sudo apt install python3

Once completed it is appropriate to test whether it works, :ref:`open up a terminal <os-terminal>` and execute the following:

.. tab:: {{ win_powershell }}

   .. code-block::  powershell

         python -c "print('Hello world')"

.. tab:: {{ win_batch }}

   .. code-block::  winbatch

         python -c "print('Hello world')"

.. tab:: {{ mac_bash }}
   
   .. code-block::  bash

         python -c "print('Hello world')"

.. tab:: {{ linux_bash }}
   
   .. code-block::  bash

         python -c "print('Hello world')"


Once Python has been installed, head over to :ref:`using pip <pip>` which will be the typical
package installation back end.
