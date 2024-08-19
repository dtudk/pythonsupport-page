.. _install-python-reference:

.. _install-python:

Install Python 
=================


.. dropdown:: Are you a DTU employee?
   :color: warning

   Using Anaconda services in research will violate their licenses.

   However, the ``conda`` installation instructions in these guides ensures that
   all subsequent installation of packages are done from the ``conda-forge`` channel
   *only*, provided you don't actively re-enable the Anaconda default channels, do **NOT**
   re-add that channel!

   Note that Anaconda is still free to use in teaching (as of 2024).
   For full details of the license, please read them on `Anacondas homepage <anaconda_>`_.


In this section, you will find different installation guides that cover the 
same components:

- Python and packages required for 1\ :sup:`st` year students,
- ``conda`` and
- Visual Studio Code.

Importantly, these installation guides are specifically designed for students who meet at least one of the following criteria:

- First-year Bachelor students at DTU
- Students taking one of:

  - Mathematics 1a/1b (:course-base:`01001`/:course-base:`01002`/:course-base:`01003`/:course-base:`01004`)
  - Computer Programming (:course-base:`02002`/:course-base:`02003`)
  - Physics (:course-base:`10060`/:course-base:`10063`/:course-base:`10065`)

These guides, although tailored for 1\ :sup:`st` year students, are also ideal for anyone needing to use Python.


.. _install-python-windows:

{{ windows_icon }} --- Installation on {{windows}}
---------------------------------------------------

* **Recommended** {{ arrow_icon }} The :doc:`automated installation <windows/automated>` installs everything with minimal interventions required.

* The :doc:`manual installation guide <windows/manual>` allows you to set up Python step by step. 


.. _install-python-macos:

{{ apple_icon }} --- Installation on {{macos}}
-----------------------------------------------

* **Recommended** {{ arrow_icon }} The :doc:`automated installation <macos/automated>` installs everything with minimial interventions required
* The :doc:`package managed installation guide <macos/homebrew>` allows you to set up Python step by step.
* The :doc:`manual installation guide <macos/manual>` is recommended if you have had previous failures with both of the above options. 


.. _install-python-linux:

{{ linux_icon }} --- Installation on Linux
--------------------------------------------

Please contact us by sending an `email <mailto:pythonsupport@dtu.dk>`_.


.. note::
    If you are using other operating systems than the above listed, please send an `email <mailto:pythonsupport@dtu.dk>`_ to us and we will try to help you.


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
