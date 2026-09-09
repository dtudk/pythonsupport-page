:orphan:

.. meta::
  :title: Failed execution on Windows
  :date: 01-09-2026
  :keywords: windows, python, vscode, jupyter notebook, smart apps
  :timeout: never
  :show-date: false


Failed execution on Windows
============================

Description
-------------------------------------

This problem may occur in many different variants.

It may be the culprit if you experience:

* failure to launch the :menuselection:`Miniforge Prompt`.
* failure to import some packages resulting in DLL load failure

   .. code-block:: python

      ImportError: DLL load failed while importing missing ...

* failure to use some extensions in VS Code

The problem is not specific to a single event or problem.

Windows has an applicaton called `Smart Apps` which by default monitors your usage pattern
and based on common patterns decide which applications are safe to run/execute.
Since Python is a programming language that can be used maliciously, it *may* prevent
you from executing Python code.

Therefore, some users may see one problem, other may experience other problems.


Solution
-------------------------------------

The current solution is to disable :menuselection:`Smart Apps`.

Go to :menuselection:`Settings -> Privacy & Security -> Windows Security -> App & Browsing Control -> Smart App Control Settings -> Turn Off`.

This will permanently disable the application, and will thus remove the protection it
may provide.

Use at your own responsibility.

