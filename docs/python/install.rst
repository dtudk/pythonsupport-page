
.. _install-python:


Installing Python
=================

Python can relatively easily be installed by following guidelines for each
of the distributions install guides.

.. note::

   Python is a commonly encountered programming language spanning nearly
   all areas of technology and commerce.

   As such the communities around Python are vast and there are **many**
   variants of its installation distributions.

In the following we will concentrate on a few of the most widely used
Python base installations.

.. contents::
   :depth: 1
   :local:
   :backlinks: none

.. warning::

   Choosing a Python software installation may seem like a minor decision.
   However, different courses may prefer, or require, a specific variant.
   Please take the time to know about the course requirements before going
   forward.



Python base installation
------------------------

The `base Python <python-org_>`_ software can be downloaded and installed through
their `download page <python-org-down_>`_ and uses common installation processes.

Installing this forces you to choose a version, and continuously use that version. I.e. upgrading to
a new Python version requires re-installing a new version, starting from downloading a new installer
and subsequently installing packages through :ref:`pip <install-pip>`.

This variant will *only* install a bare minimum Python executable and standard libraries
associtated. Subsequent packages can be installed using :ref:`pip <install-pip>`.

.. todo:

   Make more beautiful documentation, notes, or something else
   Add links to the environments and other vital information.


Conda installation
------------------

This variant is a fully flegded Python stack. It enables one to more easily swap between different
Python versions (via :ref:`environments <install-conda-env>`). It requires basic knowledge of
how to traverse a 

.. warning::

   Users are adviced to not mix :code:`pip` commands and :code:`conda` package installations.
   There may be unforseen consequences.

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

