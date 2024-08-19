
Verification and Quick Troubleshooting
--------------------------------------

Open up a Terminal again (:kbd:`Command+Space`). If you see ``(base)`` next to your username, it indicates that everything worked as intended.
Otherwise try to install Miniconda again. Miniconda can be found on `this website <https://docs.anaconda.com/miniconda/index.html#latest-miniconda-installer-links>`__. 
For further information, see :ref:`here <step2-homebrew-reference>`.


Make sure that it says ``(base)`` next to your user name when opening the Terminal.

.. card::

    .. image:: /images/install/MacOS-base-terminal.png
            :width: 100%
            :align: center

Finally type ``idle3`` in the Terminal and press :kbd:`Enter`. This should open up a new window in which you will able to run Python code.

Now ensure the following:

* It says ``Python {{ python_version }}.X`` in the top left (or in the range {{python_version_min}} -- {{python_version_max}}).
* You get no errors when typing ``import dtumathtools, uncertainties`` and press :kbd:`Enter`. This should open a new line (``>>>``) without any text, as shown below.

.. card::

    .. image:: /images/install/MacOS-IDLE-import.png
            :width: 100%
            :align: center


If it is not the case for any of the above, try to paste the following line of code in the terminal and press :kbd:`Enter`:

.. code:: bash

     conda install python={{ python_version_recommended }} dtumathtools pandas uncertainties -y

If you are still having trouble or have any questions please do not hesitate  to visit us at our office hours,
or contact us via :mail:`email <pythonsupport@dtu.dk>`
or `Discord <ps-discord-invite_>`_.
More information can be found at our :ref:`homepage <reach-us-reference>`.

