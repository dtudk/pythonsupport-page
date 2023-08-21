
.. _python-environments:

Environments
============

It is often necessary to retain two different but fully functional
package specifications. Imagine having two courses ``A`` and ``B``.
One has the requirement of ``numpy==1.23`` while the other has ``numpy==1.25``.
In cases where these are incompatible, for instance an `API <https://en.wikipedia.org/wiki/API>`_
change, one would be required to change the installed packages when participating in
each course.

Instead, one can use *environments* which allows one to retain a fully functional
package list and easily swap between them.

.. note::

   Using environments can be used for a variety of things:

   1. quickly test whether certain packages conflicts
   2. check whether a developed Python script is compatible with
      different package versions.
   3. ensures a minimal package list (no unused packages)
   4. have multiple functional package environments

   It is our clear recommendation to create an environment for
   each course. In this way you will ensure that anything you do
   in that course environment will not interfere with your other
   course environments.

.. contents::
   :depth: 2
   :backlinks: none
   :local:

.. include:: /python/environment-venv.rst.include 
.. include:: /python/environment-conda.rst.include 
.. include:: /python/environment-virtualenv.rst.include 
