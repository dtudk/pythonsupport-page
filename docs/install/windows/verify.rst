
Verification and Quick Troubleshooting
--------------------------------------

To ensure that your installation is working correctly, please go through the following steps.
Open up PowerShell again. if you see ``(base)`` next to your username, you can proceed. If unsure see the image below:

.. image:: ../images/windows-ps-base.admin.png
            :width: 400
            :align: center

Otherwise do the following:

* Search for ``Miniconda PowerShell`` prompt on your computer and open it up. (if you cannot find it, try to install Miniconda again)
* After opening the Miniconda shell, type ``conda init`` and press :kbd:`Enter`.
* Open up PowerShell again and verify that you now see ``(base)``.
* Finally type ``idle`` in PowerShell and press :kbd:`Enter`. This should open up a new window in which you will able to run Python code.

Now ensure the following:

* It says Python {{ python_version }}.xx in the top left (or in the range {{python_version_min}} -- {{python_version_max}}).
* You get no errors when typing ``import dtumathtools, uncertainties`` and press :kbd:`Enter`. This should open a new line (``>>>``) without any text, as shown below.

.. image:: ../images/windows-IDLE-import.png
            :width: 400
            :align: center



If it is not the case for any of the above, try to paste the following line of code in PowerShell and press :kbd:`Enter`:

.. code-block:: bash

     conda install -c conda-forge python={{ pythen_version_recommended }} dtumathtools uncertainties -y


If you are still having trouble or have any questions please do not hesitate to visit us at our office hours, or contact us via email or Discord. More information can be found at our :ref:`homepage <reach-us-reference>`.
