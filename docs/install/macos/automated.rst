.. _automated-reference-macos:


{{ apple_icon }} --- Automated Installation
============================================

.. button-ref:: ../windows/automated
   :ref-type: doc
   :align: right
   :color: primary
   
    Press here for Windows {{ windows_icon }}


.. dropdown:: Video Guide
    :open:
    :color: info

    .. raw:: html
    
        <iframe src="https://panopto.dtu.dk/Panopto/Pages/Embed.aspx?id=9f43eb27-2f54-46eb-b8cc-b1ce01428f3d" height="405" width="640" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>


Install everything at once
---------------------------------------------------

.. card:: 

    #.
       Open your Terminal by pressing :kbd:`Command+Space` at the same time.

    #.    
       Search for :menuselection:`Terminal` and press :kbd:`Enter`.

        .. image:: /images/install/MacOS-SpotlightSearch-Terminal.png
            :width: 100%
            :align: center

    #.
        Copy the following line of code into your Terminal and press :kbd:`Enter`:

        .. code:: bash

            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/dtudk/pythonsupport-scripts/main/MacOS_AutoInstall.sh)"


        .. include:: /_rst_includes/tip-copy.rst

    #.
        Follow the script instructions.
        You might get asked for permissions and your password to make changes on your Mac.
        Please grant permission. Note that your password will not be shown while typing it. 
        Once the script has finished, Python and Visual Studio Code will be ready to use.

        .. note::

            During the installation, you will see warnings and caveats, etc.
            The script will resolve these automatically.
            Please let the script finish.
            When you see ``Script finished``, the installation has been successful!


.. include:: /_rst_includes/tip-finish.rst

.. include:: verify.rst
