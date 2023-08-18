.. _install-conda:

`conda <anaconda_>`_
--------------------

``conda`` is a fully fledged Python stack. It enables one to easily swap between different
Python versions (via :ref:`environments <conda-env>`). It requires basic knowledge of
how to use the command line (terminal). 

.. warning::

   We advice users to not mix :code:`pip` commands and :code:`conda` package installations.
   There may be unforeseen consequences.


Conda installations comes in some variants:

`Miniconda <miniconda_>`_ |:1st_place_medal:|
   A minimal conda installation, requiring users to manually install packages subsequently.

   We recommend this Conda backend.


`Anaconda <anaconda-down_>`_ |:2nd_place_medal:| |:snail:|
   A full installation with all the most commonly used packages. These will be pre-installed
   with pre-selected versions for you. It takes up considerable disk-space >3GB.


`Mamba <mamba_>`_ |:3rd_place_medal:| |:timer:|
   Same as Miniconda, but has a much faster package resolution algorithm (determining which
   versions to install should be faster).

   If you frequently update or manage packages and are annoyed with the slow run-times of conda,
   you should try this one.

Once ``conda`` has been installed, head over to :ref:`using conda <conda>`.
