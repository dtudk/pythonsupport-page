
.. _install-python:

Official Python distribution
----------------------------

.. tip::

   DTU recommends using version {{ python_version }} of Python.

The `base Python <python-org_>`_ software can be downloaded and installed through
their `download page <python-org-down_>`_ and uses common installation processes.

Installing the official Python distribution forces you to choose a version, and continuously use that version. I.e. upgrading to
a new Python version requires re-installing a new version, starting from downloading a new installer
and subsequently installing packages, again, through :ref:`pip <pip>`.


.. tab:: {{ windows }}

   - Download and install Python from `here <python-org-down-win_>`__
   - Ensure you check :far:`square-check` the ``Add Python {{ python_version }} to PATH`` (at the bottom of the installation GUI)

.. tab:: {{ macos }}

   - Download and install Python from `here <python-org-down-mac_>`__
   - If you are using a newer Mac with an M1 or M2 processor, you need to enable the
     Rosetta 1 or 2, respectively to ensure Python works.

   If there are problems, a more detailed instruction can be found
   `here <https://www.dataquest.io/blog/installing-python-on-mac/>`__.

.. tab:: {{ linux }}

   Almost all Linux distributions ships a Python at its core. If not, use your
   distributions package manager to install Python

   Something like:

   .. code-block:: bash

      # the exact package manager, or package name is distro dependent
      sudo apt install python3

Once completed it is appropriate to test whether it works, :ref:`open up a terminal <os-terminal>` and execute the following:

.. todo:

   Make more beautiful documentation, notes, or something else
   Add links to the environments and other vital information.

Once Python has been installed, head over to :ref:`using pip <pip>` which will be the typical
package installation backend.
