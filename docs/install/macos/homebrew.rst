.. _package-managed-reference-macos:


{{ apple_icon }} --- Homebrew Installation
============================================

.. button-ref:: ../windows/manual
   :ref-type: doc
   :align: right
   :color: primary
   

    Press here for Windows {{ windows_icon }}


.. dropdown:: {{ video_install }}
    :open:
    :color: info

    .. raw:: html

        <iframe src="https://panopto.dtu.dk/Panopto/Pages/Embed.aspx?id=8c88a2cb-25a5-485a-8131-b1dc00bb2dee" height="405" width=100% style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>


.. _install-python-macos-homebrew:

Step 1: Install Homebrew 
--------------------------

.. card:: 

    #.
        Go to `this website <https://brew.sh>`__ and follow the instructions.
        
    #.  
        The Homebrew website will ask you to open a terminal.
        Find the :menuselection:`Terminal` using your Spotlight search (:kbd:`Command+Space`) and press :kbd:`Enter`.
        You might get asked several times for your password to grant permissions.
       
        **Note**: your password will not be shown while typing it.

        Do *not* close the terminal once the installation script has finished.

        .. image:: /images/install/MacOS-SpotlightSearch-Terminal.png
           :width: 100%
           :align: center

        .. image:: /images/install/macos-package-managed-homebrew.png
           :width: 400
           :align: center

    #.
        *NOTE*: Not all {{ macos }} requires this step!

        If Homebrew requests you to execute commands under :guilabel:`Next steps:`, then complete this step.

        Add Homebrew to the ``PATH`` by copying, pasting and running the code that Homebrew displays
        in the Terminal (look at the picture below for guidance). 
        Press :kbd:`Enter` once you have pasted the code. The code should look similar to the following image 
        but might differ slightly for different {{ macos }} versions.

        .. image:: /images/install/macos-package-managed-homebrew-terminal-instructions.png
           :width: 400
           :align: center


.. _install-python-macos-conda:
.. _install-python-macos-python:

Step 2: Install Miniconda and Python
--------------------------------------

.. card::
   
   Installs all packages required for the 1\ :sup:`st` year
   Polytechnical Foundation courses at DTU. 

   #.
      Close the previously used :menuselection:`Terminal`,
      and open up a new :menuselection:`Terminal` using
      Spotlight search (:kbd:`Command+Space` and search for ``Terminal``).

   #.
      Paste the following code in the Terminal and press :kbd:`Enter`.

      .. code:: bash

         brew install --cask miniconda

   #.
      Paste the following code in the Terminal and press :kbd:`Enter`.

      .. code:: bash

         conda init "$(basename "${SHELL}")"
         eval "$(conda "shell.$(basename "${SHELL}")" hook)"

   #.
      Run the following command in the Terminal by copying, pasting and pressing :kbd:`Enter`:

      .. code:: bash

         conda config --add channels conda-forge ; conda config --remove channels defaults ; conda config --set channel_priority strict

      .. include:: /_rst_includes/tip-copy.rst

   #.
      Run the following command in the Terminal by copying, pasting and pressing :kbd:`Enter`:

      .. code:: bash

         conda install python={{ python_version_recommended }} dtumathtools pandas scipy statsmodels uncertainties -y

    
.. _install-python-macos-vscode:

Step 3: Install Visual Studio Code 
---------------------------------------------------

.. card::
    
   Install Visual Studio Code by pasting the following in your terminal and pressing :kbd:`Enter`.

   .. code:: bash

      brew install --cask visual-studio-code


.. _install-python-macos-vscode-exts:

Step 4: Install extensions for Visual Studio Code
---------------------------------------------------

.. |extensions| image:: /images/install/extensions.png
    :height: 25px

.. card:: 

   #. 
       Open Visual Studio Code and select the Extensions |extensions| tab on the left.

       .. image:: /images/install/VSC-extensions.png
          :width: 400
          :align: center
   
   #.  
       Search for `Python`, and download the extension. Make sure that it is from Microsoft. 

       .. image:: /images/install/macos-package-managed-python.png
          :width: 200
          :align: center

   #. 
       Hereafter search for `Jupyter`, and download that extension as well. This also needs to be from Microsoft.
       
       .. image:: /images/install/macos-package-managed-jupyter.png
          :width: 200
          :align: center


.. include:: /_rst_includes/tip-finish.rst

.. include:: verify.rst
