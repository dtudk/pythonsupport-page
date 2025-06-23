Uninstalling Visual Studio Code
===================================

This guide will help you uninstall Visual Studio Code from your computer. 
This can be useful if Visual Studio Code is not working correctly and you want a fresh start.

.. dropdown:: {{ video_install }}
    :open:
    :color: info

    .. raw:: html

       <iframe src="https://panopto.dtu.dk/Panopto/Pages/Embed.aspx?id=1896bd49-4741-43f1-b6e8-b30000b33232" height="405" width=100% style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>




1. In the ``Search`` tab, search for **add or remove programs**.
2. Search for **Visual Studio Code**
3. Press the three dots on the right hand side, click **uninstall** and follow the instructions. 

      .. image:: /images/install/vscode_uninstall.png
         :width: 500
         :align: center

.. note::

   This will leave behind some files, which you can delete manually if you want to. To do this follow the steps below. This is recommended if you are trying to fix an issue with Visual Studio Code by uninstalling and reinstalling. 

1. Press the {{ windows_icon }} button and :kbd:`R` at the same time
2. Type in ``%appdata%`` and press :kbd:`Enter`.
3. Find the folder named ``Code`` and delete it.
4. Press the {{ windows_icon }} button and :kbd:`R` at the same time
5. Type in ``%userprofile%`` and press :kbd:`Enter`.
6. Find the folder named ``.vscode`` and delete it.
