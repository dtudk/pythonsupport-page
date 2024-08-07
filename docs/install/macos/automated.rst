.. _automated-reference-macos:


MacOS - Automated installation guide
====================================

.. button-ref:: automated-reference-windows
    :ref-type: ref
    :color: info

    Not using **MacOS**? Press here for **Windows** guides.

.. todo::
    Change color?

The first thing you need to do is open your terminal. This can be done by pressing "command" and "space" at the same time. Thereafter search for terminal and press enter.

.. todo::
    Insert image of spotlight search for terminal.

Next you need to copy the following line of code into your terminal and press enter:

.. tip::
    You can copy and paste all code in the grey code blocks below by hovering your mouse over the block and pressing the icon in the top right.

.. code-block:: bash

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/dtudk/pythonsupport-scripts/main/AutoInstallMacOS.sh)"

Please follow the instructions by the script. You might get asked for permissions and your password to make changes on your Mac. Please grant permission. Note that your password won't be shown when typing it.

Once the script is finished, Python and Visual Studio Code will be ready to use

.. note::

    During the installation you will see warnings and caveats ect. These will
    all be resolved automatically by the script. Please let the script finish. When you see Script
    finished, the installation has been successful

.. tip::
    When you have finished the guide, we **strongly recommend** checking out the :ref:`Python Essentials <essentials-reference>` to prepare you for coding.

Verification and Quick Troubleshooting
--------------------------------------
Open up a terminal again. if you see ``(base)`` next to your username, you can proceed. Otherwise
try to install miniconda again. Miniconda can be found on `this website  <https://docs.anaconda.com/miniconda/index.html#latest-miniconda-installer-links>`_. 
For further information, see step 1 :ref:`here <fully-manual-reference-mac>`

.. todo::
    Insert image of the terminal with ``(base)`` next to the username

Make sure that it says ``(base)`` next to your user name when opening the terminal.

Finally type ``idle3`` in the terminal and press enter. This should open up a new window in which you will able to run python code.

Now ensure the following:

• It says Python 3.11.xx in the top left.
• You get no errors when typing ``import dtumathtools, uncertainties`` and press enter. This should open a new line without any text, as shown bellow.

.. todo::
    Insert image of ``idle3`` after import dtumathtools and uncertainties so they can see what it should look like.


If it is not the case for one of the above, try to paste the following line of code in the terminal and press enter:

.. code-block:: bash

     conda install -c conda-forge python=3.11 dtumathtools uncertainties -y


If you are still having trouble or have any questions please do not hesitate visiting us at our office hours, or contact us via email or Discord. More information can be found at our :ref:`homepage <reach-us-reference>`.
