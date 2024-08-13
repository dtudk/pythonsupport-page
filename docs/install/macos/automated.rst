.. _automated-reference-macos:


{{ apple_icon }} - Auto installation
=====================================

.. button-link:: ../windows/automated.html
   :align: right
   :color: primary
   
    Press here for Windows {{ windows_icon }}

.. todo::
    Change color?

The first thing to do is to open your terminal. This can be done by pressing :kbd:`Command-Space` at the same time. Thereafter search for :menuselection:`Terminal` and press :kbd:`Enter`.

.. todo::
    Insert image of spotlight search for terminal.

Next, copy the following line of code into your terminal and press :kbd:`Enter`:

.. tip::

    You can copy and paste all code in the grey code blocks below by hovering your mouse over the block and pressing the icon in the top right.

.. code-block:: bash

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/dtudk/pythonsupport-scripts/main/AutoInstallMacOS.sh)"

Please follow the script instructions. You might get asked for permissions and your password to make changes on your Mac. Please grant permission. Note that your password won't be shown when typing it.

Once the script has finished, Python and Visual Studio Code will be ready to use.

.. note::

    During the installation you will see warnings and caveats etc. These will
    all be resolved automatically by the script. Please let the script finish. When you see ``Script
    finished``, the installation has been successful!

.. tip::

    When you have finished the guide, we **strongly recommend** checking out the :ref:`Python Essentials <essentials-reference>` to prepare you for coding.


Verification and Quick Troubleshooting
--------------------------------------

Open up a terminal again. if you see ``(base)`` next to your username, it indicates that everything worked as intended.
Otherwise try to install Miniconda again. Miniconda can be found on `this website <https://docs.anaconda.com/miniconda/index.html#latest-miniconda-installer-links>`_. 
For further information, see :ref:`step 1 here <fully-manual-reference-mac>`.

.. todo::
    Insert image of the terminal with ``(base)`` next to the username

Make sure that it says ``(base)`` next to your user name when opening the terminal.

Finally type ``idle3`` in the terminal and press :kbd:`Enter`. This should open up a new window in which you will able to run python code.

Now ensure the following:

* It says Python {{ python_version }}.xx in the top left (or in the range {{python_version_min}} -- {{python_version_max}}.
* You get no errors when typing ``import dtumathtools, uncertainties`` and press :kbd:`Enter`. This should open a new line (``>>>``) without any text, as shown below.

.. todo::
    Insert image of ``idle3`` after import dtumathtools and uncertainties so they can see what it should look like.


If it is not the case for one of the above, try to paste the following line of code in the terminal and press enter:

.. code-block:: bash

     conda install -c conda-forge python={{ python_version_recommended }} dtumathtools uncertainties -y


If you are still having trouble or have any questions please do not hesitate visiting us at our office hours, or contact us via :mailto:`email <pythonsupport@dtu.dk>` or `Discord <ps-discord-invite>`_. More information can be found at our :ref:`homepage <reach-us-reference>`.
