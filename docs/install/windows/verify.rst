
Verification and Quick Troubleshooting
--------------------------------------

Please go through the following steps to ensure your installation is working correctly.
Open up PowerShell again.
You can proceed if you see ``(base)`` next to your username.
If unsure see the image below:

.. card::

    .. image:: /images/install/windows-ps-base.png
                :width: 100% 
                :align: center

If you do not see ``(base)`` in your Terminal, please do the following:

* Ensure that Miniconda is installed: Search for ``Miniconda PowerShell`` prompt on your computer and open it up. If you cannot find it, press :ref:`here to install Miniconda <install-python-windows-conda>`. 
* After opening the Miniconda Shell, type ``conda init`` and press :kbd:`Enter`.
* Open up PowerShell again and verify that you now see ``(base)``.

Now ensure the following:

* Open up Powershell and type ``idle``, then press :kbd:`Enter`.
  This should open a new window in which you can run Python code.
* The Idle window says ``Python {{ python_version }}.X`` in the top left (or in the range of {{python_version_min}} -- {{python_version_max}}).
* You get no errors when typing ``import dtumathtools, pandas, uncertainties`` and press :kbd:`Enter`. This should open a new line (``>>>``) without any text, as shown below.

.. card::

    .. image:: /images/install/windows-IDLE-import.png
                :width: 100% 
                :align: center


If this is not the case for any of the above, try to paste the following line of code in PowerShell and press :kbd:`Enter`:

.. code:: bash

   conda install python={{ python_version_recommended }} dtumathtools pandas scipy statsmodels uncertainties -y


If you are still having trouble or have any questions, please do not hesitate to visit us at during office hours
or contact us via :mail:`email <pythonsupport@dtu.dk>`
or `Discord <ps-discord-invite_>`_.
More information can be found on our :ref:`homepage <reach-us-reference>`.

