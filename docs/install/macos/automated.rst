.. _automated-reference-macos:


{{ apple_icon }} --- Automated Installation
============================================

.. button-link:: ../windows/automated.html
   :align: right
   :color: primary
   
    Press here for Windows {{ windows_icon }}


Install everything at once
----------------------------

.. card:: 


    #.
        Open thing to do is to open your terminal by pressing :kbd:`Command+Space` at the same time.

    #.    
        Then search for :menuselection:`Terminal` and press :kbd:`Enter`.


        .. image:: ../images/MacOS-spotlight-terminal.png
            :width: 100%
            :align: center

    #.

        Next, copy the following line of code into your terminal and press :kbd:`Enter`:

        .. code-block:: bash

            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/dtudk/pythonsupport-scripts/main/AutoInstallMacOS.sh)" 

        .. tip::

             You can copy and paste all code in the gray code blocks above by hovering your mouse over the block and pressing the icon in the top right.

    

    #.

        Follow the script instructions.
        You might get asked for permissions and your password to make changes on your Mac.
        Please grant permission. Note that your password will not be shown while typing it. 
        Once the script has finished, Python and Visual Studio Code will be ready to use.

        .. note::

            During the installation you will see warnings and caveats etc.
            These will all be resolved automatically by the script.
            Please let the script finish.
            When you see ``Script finished``, the installation has been successful!

        .. tip::

            When you have finished the guide, we **strongly recommend** checking out the :ref:`Python Essentials <essentials-reference>` to prepare you for coding.


.. include:: verify.rst
