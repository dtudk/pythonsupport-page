
Windows Arm Support
===================

Currently conda is not officially supported on ARM windows machines.
Following our guides users currently install a x64 conda release which
is emulated by windows. For most use cases emulation is enough for
students to get by.

When Emulation is Not a Viable Option
-------------------------------------

For high performance tasks using emulation might not be an option since
this limits the speed of the program. Installing native package binaries 
(for example python.exe, numpy, pandas) is not an option with conda since 
most conda packages are not compiled for win-arm64. See compatibility here: 

* `conda-forge python <https://anaconda.org/conda-forge/python>`_
* `conda-forge numpy <https://anaconda.org/conda-forge/numpy>`_
* `conda-forge pandas <https://anaconda.org/conda-forge/pandas>`_


1. Solution: Native Python
~~~~~~~~~~~~~~~~~~~~~~~~~~
The first solution is not to use conda at all. By downloading Python from 
the official website at `python.org <https://www.python.org/downloads/>`_ 
and installing packages using pip, all binaries will compile to native Arm64.

**Pros**:

* Easy to set up

**Cons**:

* Can only use pip packages


2. Solution: Use WSL and conda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another solution is to use conda on a Windows Subsystem for Linux since most
conda packages are compiled to both linux-x64 and linux-arm64. This is a
viable option since the subsystem adds very little overhead compared to translation
of x64 to arm64.

**Pros**:

* Most conda packages can be used

**Cons**:

* More complicated to setup and use




