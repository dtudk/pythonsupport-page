.. _install-python-reference:

.. _install-python:

Install Python
==============


.. dropdown:: License and terms of use of Anaconda
   :color: warning

   Anaconda/Miniconda defaults to installing packages from the
   Anaconda repositories. There are license restrictions on how
   to use these. Please carefully
   `read them <https://legal.anaconda.com/policies/en/?name=terms-of-service>`__ for your own sake.

   The ``conda`` provided through our installation guidelines will default
   to use the ``conda-forge`` channel. However, the Anaconda repositories
   are hard-coded in the ``conda`` infrastructure as fallback.
   Therefore users should be aware, at install time, where the packages originates from.

   .. todo::

      add examples of how this may look

      .. code:: shell

         numpy              conda-forge/linux-64::numpy-2.1.0-py311hed25524_0 

      vs.

      .. code:: shell

         numpy              pkgs/linux-64::numpy-2.1.0-py311hed257a2_0 

   We are pursuing strategies to completely remove the Anaconda repositories
   to ensure that employees will not break the terms of service as outlined by Anaconda.

   Note that Anaconda is free to use in teaching (as of 2024).
   For full details of the license, please read them on
   `here <https://legal.anaconda.com/policies/en/?name=terms-of-service#anaconda-terms-of-service>`__.

   See :ref:`here <rec-conda>` for more details.


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


.. _install-python-windows-list:

{{ windows_icon }} --- Installation on {{windows}}
---------------------------------------------------

* **Recommended** {{ arrow_icon }} The :doc:`automated installation <windows/automated>` requires minimal intervention.

* The :doc:`manual installation guide <windows/manual>` allows you to set up Python step by step. 


.. _install-python-macos-list:

{{ apple_icon }} --- Installation on {{macos}}
-----------------------------------------------

* **Recommended** {{ arrow_icon }} The :doc:`automated installation <macos/automated>` requires minimal intervention.
* The :doc:`package-managed installation guide <macos/homebrew>` allows you to set up Python step by step.
* The :doc:`manual installation guide <macos/manual>` is recommended if you have had previous failures with both of the above options. 


.. _install-python-linux-list:

{{ linux_icon }} --- Installation on Linux
--------------------------------------------

* **Recommended** {{ arrow_icon }} The :doc:`manual installation guide <linux/manual>`.


.. note::

   If you are using a different operating system than the ones listed above,
   please send an `email <mailto:pythonsupport@dtu.dk>`_ to us, and we will try to help you.


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
    macos/homebrew.rst
    macos/manual.rst

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Linux

    linux/manual.rst
