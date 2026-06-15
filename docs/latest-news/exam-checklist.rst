.. meta::
  :title: Exam Checklist
  :date: 12-11-2025
  :keywords: exams

Exam Checklist - Fall 2025
====================================

Description
-----------

This page goes through some items you should check to make sure that your Python
installation works before exams!

Checklist
-------------

**1) Check that Python is up-to-date**

Check that your installation is at the right version to avoid unexpected
differences during exams. As of 2025, Python version
{{python_version_min}}-{{python_version_max}} is expected. You can check this
with the following command in a terminal:

.. code-block:: bash

   python3 --version

If the shown version is outside the range, try running the installation scripts
or updating the software directly.

**2) Check that Python and VS Code works**

Run some Python code, check that you can import the modules you need for your
exams, and that you can run it in VS Code without errors. Here is an example:

.. code-block:: python

   # Adjust this with the packages you need.
   import numpy, scipy, pandas, uncertainties, sympy, dtumathtools, statsmodels
   print("Everything works!")


**3) Verify that everything works without Wi-Fi**

The Wi-Fi network provided during exams is highly restricted, so you should make
sure that nothing on your computer depends on the internet to run. Jupyter
Notebook, for example, runs in your browser. Turn of your Wi-Fi and ensure that
everything works as expected.

