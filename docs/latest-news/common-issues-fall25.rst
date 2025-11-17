:orphan:

.. meta::
  :title: Current Common Issues - Fall 2025
  :date: 19-10-2025
  :keywords: common issues
  :priority: 2


Current Common Issues - Fall 2025
====================================

Description
-----------

Current common Python related issues for DTU students and a
checklist for solving them.


Checklist
-------------
By following the steps below a lot of the common issues we have seen recently should be solved.
These items cover both MacOS and Windows users.

**Step 1: Disable "Python Environments" extension in VS Code**

- On the left hand side in VS Code press the extensions tab.
- Scroll down and find the extension called "Python Environments" and click it.
- Click :guilabel:`Disable` and then :guilabel:`Restart extension`.

**Step 2: Downgrade "Jupyter" extension in VS Code**

- On the left hand side in VS Code press the extensions tab.
- Scroll down and find the extension called "Jupyter" and click it.
- Click the arrow icon (:fas:`angle-down`) next to "Uninstall" and then click :guilabel:`Install Specific Version`.
- Select version 2024.11.0 and it will install.
- Click :guilabel:`Restart extension`.

.. TODO: Upgrading Ipykernel may solve it

**Step 3: Uninstall the VS Code PDF extension**

- On the left hand side in VS Code press the extensions tab.
- Scroll down and find the extension called "vscode-pdf" and click it.
- Click :guilabel:`Uninstall` and then :guilabel:`Restart` extension. 

**Step 3: Change Python Locator**

- On the left hand side in VS Code press the settings tab (:fas:`gear`).
- Click :guilabel:`Settings`.
- In the search bar at the top type "Python Locator".
- Click the drop-down menu displaying :guilabel:`native` and select :guilabel:`js`.

**Step 4: Restart VS Code**

- Close VS Code completely and then open it again.

