
Verification and Quick Troubleshooting
--------------------------------------

Please go through the following steps to ensure your installation is working correctly.
Open up a Terminal again (:kbd:`Command+Space`).
You can proceed if you see ``(base)`` next to your username.
If unsure see the image below:

.. card::

    .. image:: /images/install/MacOS-base-terminal.png
            :width: 100%
            :align: center

If you do not see ``(base)`` in your Terminal, please do the following:

* Ensure that Miniconda is installed, follow
  :ref:`these instructions <install-python-macos-conda>`.
* Open up a Terminal again and verify that you now see ``(base)``.


Now ensure the following:

* Open up a Terminal and type ``idle3``, then press :kbd:`Enter`.
  This should open a new window in which you can run Python code.
* The Idle window says ``Python {{ python_version }}.X`` in the top left (or in the range of {{python_version_min}} -- {{python_version_max}}).
* You get no errors when typing ``import dtumathtools, pandas, uncertainties`` and press :kbd:`Enter`. This should open a new line (``>>>``) without any text, as shown below.

.. card::

    .. image:: /images/install/MacOS-IDLE-import.png
            :width: 100%
            :align: center


If it is not the case for any of the above, try to paste the following line of code in the terminal and press :kbd:`Enter`:

.. code:: bash

   conda install python={{ python_version_recommended }} dtumathtools pandas scipy statsmodels uncertainties -y


If you are still having trouble or have any questions, please do not hesitate to visit us at during office hours
or contact us via :mail:`email <pythonsupport@dtu.dk>`
or `Discord <ps-discord-invite_>`_.
More information can be found on our :ref:`homepage <reach-us-reference>`.

