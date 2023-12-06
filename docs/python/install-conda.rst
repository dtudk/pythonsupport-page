.. _install-conda:

`conda <anaconda_>`_ installation
----------------------------------

.. tip::

   DTU recommends using version {{ python_version }} of Python.

``conda`` is a fully fledged Python stack. It enables one to easily swap between different
Python versions (via :ref:`environments <conda-env>`). It requires basic knowledge of
how to use the command line (terminal). 

.. warning::
   :class: dropdown

   We advice users to not mix :code:`pip` commands and :code:`conda` package installations.
   There may be unforeseen consequences.


Conda installations comes in some variants:

`Miniconda <miniconda_>`_ |:1st_place_medal:|
   A minimal conda installation, requiring users to manually install packages subsequently.

   We recommend this Conda back end.


`Anaconda <anaconda-down_>`_ |:2nd_place_medal:| |:snail:|
   A full installation with all the most commonly used packages. These will be pre-installed
   with pre-selected versions for you. It takes up considerable disk-space >3GB.


`Mamba <mamba_>`_ |:3rd_place_medal:| |:timer:|
   Same as Miniconda, but has a much faster package resolution algorithm (determining which
   versions to install should be faster).

   If you frequently update or manage packages and are annoyed with the slow run-times of conda,
   you should try this one.

Once ``conda`` has been installed, head over to :ref:`using conda <conda>`.


.. _install-conda-packages:

Installing packages
--------------------

.. admonition:: Unsure what a *terminal* is?
   :class: dropdown info

   Please head over :ref:`here <os-terminal>` to understand how to open and use a terminal.

If you are using a :ref:`conda` distribution, you will need to use the :ref:`conda` package manager.

Open a terminal and type:


.. tab-set::

   .. tab-item:: {{ win_powershell }}
      :sync: powershell

      .. code-block:: powershell

         conda install numpy

   .. tab-item:: {{ mac_bash }}
      :sync: mac

      .. code-block:: bash

         conda install numpy

   .. tab-item:: {{ linux_bash }}
      :sync: bash

      .. code-block:: bash

         conda install numpy

Replace ``numpy`` by the package name for installing other packages.
