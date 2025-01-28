.. _rec-conda:

Conda
=====

Conda will in this context be used to describe a ``conda`` command provider.
The programs listed here, all provide this ``conda`` command, which it-self enables
the installation and environment management commands required for a seamless
usage of open-source software.

When people refer to ``Conda``, some mean ``Miniconda``, others ``Anaconda``, and some
even ``Miniforge``.
However, generally users do not care if the ``conda`` provider is one or the other.

Similarly, when software recommends one or the other, it will likely still be installable
by using any of the other providers. So please select the provider once, and adapt
installation procedures as noted in the below sections.


.. _rec-conda-anaconda:

Anaconda
========

.. danger::

   Anaconda installations default to download content from
   a *channel* that is licensed, i.e. *not free*!

   The `terms of service <https://legal.anaconda.com/policies/en/>`__
   has this small snippet (as of January 2025):

   | Your registration, download, use, installation, access, or enjoyment
   | of all Anaconda Offerings on behalf of an organization that has two
   | hundred (200) or more employees or contractors (“Organizational Use”)
   | requires a paid license of Anaconda Business or Anaconda Enterprise.
   | For sake of clarity, use by government entities and nonprofit entities
   | with over 200 employees or contractors is considered Organizational Use.

   This means that in order to install and use software provided through the
   Anaconda channels (which is the default!) is requiring one to pay for the
   software.

DTU does *not* recommend the installation of **Anaconda** since any non-teaching
use will violate their terms of service.

Instead please follow the installation instructions :ref:`here <install-python>`
which will ensure that you are only installing things from the ``conda-forge`` channel,
which is free.



.. _rec-conda-miniconda:

Miniconda
=========

While Miniconda is hosted, and maintained by the Anaconda company, it can be used
in a *free* form by changing the default channel to ``conda-forge``.

.. danger::

   One will *have* to change the default channel *just after installation*
   to ensure no terms of service violation.


Miniconda will be installed if you follow the
:ref:`installation instructions <install-python>`.

The change is a one-time change that defaults the installation sources to the
correct tree.

.. code:: shell

   conda config --add channels conda-forge
   conda config --remove channels defaults

.. attention::

   Please be aware of installation instructions that install packages
   from the Anaconda channels. If in doubt, feel free to
   :mail:`contact us <pythonsupport@dtu.dk>`.



.. _rec-conda-miniforge:

Miniforge
===============================================

This ``conda`` provider defaults to not use any Anaconda channels, and will
thus be the easiest one to ensure no license violations.

