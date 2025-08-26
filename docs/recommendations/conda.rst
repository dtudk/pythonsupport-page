:orphan:


.. danger::

   All recommendations and comments here are provided *as is* and should not be taken as
   legal advice.

   Always consult the official license terms of the software you are using and installing.


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

   The `terms of service <https://www.anaconda.com/legal/terms/terms-of-service>`__
   has this small snippet (as of July 2025):

   | (1) you are an individual that is using the Platform for your own personal, non-commercial purposes; 
   | 
   | (2) you are using the Platform on behalf of or in association with an Eligible Academic Institution (as defined in our Academic Policy and conditioned upon your acceptance of the Academic End User License Agreement); 
   | 
   | (3) you are using the Platform on behalf of or in association with an Eligible Non-Profit and Research Organization (as defined in our Non-Profit and Research Policy); or 
   | 
   | (4) you are using the Platform on behalf of a for-profit organization with 200 or fewer total employees or contractors (including all Affiliates).  
   | 
   | Anaconda reserves the right to request proof of verification of your eligibility status for free usage from you. 


DTU does *not* recommend the installation of **Anaconda**.

Instead please follow the installation instructions :ref:`here <install-python>`
which will ensure that you are using Miniforge that only installs packages from
the ``conda-forge`` channel, which is free.



.. _rec-conda-miniconda:

Miniconda
=========

While Miniconda is hosted, and maintained by the Anaconda company, it can be used
in a *free* form by changing the default channel to ``conda-forge``.

.. danger::

   One will *have* to change the default channel *just after installation*
   to ensure no terms of service violation.


Since July 2025, Anaconda has changed its approach to enforcing the license
terms of service. We there do not recommend installing Miniconda either.

If you still want to use Miniconda, here is a one-time change that defaults
the installation sources to the correct tree.

.. code-block:: shell

   conda config --add channels conda-forge
   conda config --remove channels defaults

.. attention::

   Please be aware of installation instructions that install packages
   from the Anaconda channels. If in doubt, feel free to
   :mailto:`contact us <pythonsupport@dtu.dk>`.



.. _rec-conda-miniforge:

Miniforge
===============================================

This ``conda`` provider defaults to not use any Anaconda channels, and will
thus be the easiest one to ensure no license violations.

This is the ``conda`` provider that our guides will install for you.
It is not under any license terms and can be used for teaching and/or
commercial use.



.. _rec-conda-students:

Students
========

In general students can *freely* install and use the **Anaconda** software stack.

A student should, however, still be aware of the limitations of the above policy.
For instance, if the student is hired in a company with more than
200 employees, then the company is responsible for obeying the license.

Additionally, if a student creates work that is used in a DTU research project, it is
not fully clear how the interpretation should be. When a student has
signed a **G**-declaration then one could interpret the developed software/research as
a work from DTU.

Therefore, for simplicity, and to be future proof, we ask that you, as a student,
follow the same guidelines as DTU employees.
