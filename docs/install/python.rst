.. _install-python-reference:

.. _install-python:

Install Python
==============

In this section, you will find different installation guides that cover the 
same components:

- ``conda`` as the Python package manager,
- Python and packages required for 1\ :sup:`st` year students,
- Visual Studio Code.

Importantly, these installation guides are specifically designed for students who meet at least one of the following criteria:

- First-year Bachelor students at DTU
- Students taking one of:

  - Mathematics 1a/1b (:course-base:`01001`/:course-base:`01002`/:course-base:`01003`/:course-base:`01004`)
  - Computer Programming (:course-base:`02002`/:course-base:`02003`)
  - Physics (:course-base:`10060`/:course-base:`10063`/:course-base:`10065`)
  - Statistics (:course-base:`02402`)

Although tailored for 1\ :sup:`st` year students, these guides are also ideal for anyone needing to use Python.

.. dropdown:: License and terms of use of Anaconda
   :color: warning

   Anaconda/Miniconda defaults to installing packages from the
   Anaconda repositories. There are license restrictions on how
   to use these. Please carefully
   `read them <https://www.anaconda.com/legal/terms/terms-of-service>`__ for your own sake.

   These terms does *not* apply to Miniforge (which is what our guides use)!

   The ``conda`` provided through our installation guidelines will default
   to use the ``conda-forge`` channel (and so are not under the Anaconda
   terms of service). However, one may accidentially follow a guide that adds
   the Anaconda repositories to the available download channels.
   Therefore users should be aware, at install time, where the packages originates from.

   .. todo::

      add examples of how this may look

      .. code-block:: shell

         numpy              conda-forge/linux-64::numpy-2.1.0-py311hed25524_0 

      vs.

      .. code-block:: shell

         numpy              pkgs/linux-64::numpy-2.1.0-py311hed257a2_0 

   Note that Anaconda is free to use in teaching (as of 2025) for students.
   For full details of the license, please read them on
   `here <https://www.anaconda.com/legal/terms/terms-of-service>`__.

   See :ref:`here <rec-conda>` for more details.


.. _install-python-windows-list:

{{ windows_icon }} --- Installation on {{windows}}
---------------------------------------------------

* **Recommended** {{ arrow_icon }} The :ref:`automated installation <automated-reference-windows>` requires minimal intervention.

* The :ref:`manual installation guide <install-python-windows-manual>` allows you to set up Python step by step. 


.. _install-python-macos-list:

{{ apple_icon }} --- Installation on {{macos}}
-----------------------------------------------

* **Recommended** {{ arrow_icon }} The :ref:`automated installation <automated-reference-macos>` requires minimal intervention.
* The :ref:`manual installation guide <install-python-macos-manual>` allows you to set up Python step by step. 

..  * The :ref:`package-managed installation guide <package-managed-reference-macos>` allows you to set up Python step by step.

.. _install-python-linux-list:

{{ linux_icon }} --- Installation on Linux
--------------------------------------------

* **Recommended** {{ arrow_icon }} The :ref:`manual installation guide <install-python-linux-manual>`.


.. note::

   If you are using a different operating system than the ones listed above,
   please send an :mailto:`email <pythonsupport@dtu.dk|Unsupported operating system: >` to us, and we will try to help you.


.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Windows

    windows/automated
    windows/manual.rst

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: MacOS

    macos/automated
    macos/manual.rst

.. macos/homebrew.rst

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Linux

    linux/manual.rst
