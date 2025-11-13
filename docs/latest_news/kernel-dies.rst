.. meta::
  :title: Kernel Has Died
  :date: 21-10-2025
  :keywords: vscode, jupyter notebook



Kernel Has Died
====================================

Description
-------------------------------------


This problem occurs when the Jupyter kernel unexpectedly stops working while running code in a Jupyter notebook.

This appears as `Kernel has died` message in red in the notebook interface and will result in none of the code cells being executable.

Solution
-------------------------------------
To resolve the "Kernel has died" issue, you need to create a new Conda environment. Following the steps below will guide you through the process of creating an environment named "DTU" with the necessary packages installed.

**Step 1: Open your terminal or command prompt**
On MacOs search for menuselection`Terminal` using your Spotlight search (:kbd:`Command+Space`) and press :kbd:`Enter`.

On windows open PowerShell by opening the menu bar, then search for :menuselection:`Windows PowerShell`


**Step 2: Create a new Conda Environment** 
Copy and paste the following line of code into your terminal and press :kbd:`Enter`:

.. code-block:: bash

      conda create --name DTU python={{ python_version_recommended }} dtumathtools pandas scipy statsmodels uncertainties -y

.. TODO: upgrade ipykernel may solve it

 
**Step 3: Select the new environment as your Kernel in VS Code**
Open VS Code and select `DTU(Python 3.12.XX)` as your Kernel.



.. note::
  If you need any help with how to select the kernel in VS Code or other related issues, please refer to the guide ref`here <jupyter-notebooks>`.

