
Verification
--------------------------------------

.. dropdown:: {{ video_install }}
    :open:
    :color: info

    .. raw:: html

        <iframe src="https://panopto.dtu.dk/Panopto/Pages/Embed.aspx?id=377c5e44-55d6-41ca-ad03-b34700c0169a" height="405" width=100% style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

Verify that your installation is successful by following these steps:

1. Search for :menuselection:`Terminal` using your
   Spotlight search (:kbd:`Command+Space`) and press :kbd:`Enter`.
   Verify that ``(base)`` is shown to the
   left of your username.
   Something like the image below:

   .. card::

      .. image:: /os/gifs/Unix/conda-check-base.gif
         :width: 100%
         :align: center

2. Type ``idle3`` in the Terminal, then press :kbd:`Enter`.
   This should open a new window in which you can run Python code.

3. Verify the :guilabel:`IDLE` window says ``Python {{ python_version }}.X``
   in the top left
   (or in the range of {{python_version_min}} -- {{python_version_max}}).

4. Copy the following Python code into the :guilabel:`IDLE` window, then press :kbd:`Enter`:

   .. code-block:: python

      import dtumathtools, pandas, scipy, statsmodels, uncertainties

   Verify that a new line (``>>>``) appears without any text (indicating everything got imported correctly).
   See the below image for an example:

   .. card::

      .. image:: /images/install/MacOS-IDLE-import.png
         :width: 100%
         :align: center

If some steps result in a different than described above, please continue reading the Troubleshooting section.


Troubleshooting
^^^^^^^^^^^^^^^^

Only follow these troubleshooting steps if something in the previous section did not check out.


* Ensure that Miniforge is installed, follow
  :ref:`these instructions <install-python-macos-manual-conda>`.

* Ensure the packages are installed (if they are already installed, this will not do anything).

  Paste the following line of code to the Terminal and press :kbd:`Enter`:

  .. code-block:: bash

     conda install python={{ python_version_recommended }} dtumathtools pandas scipy statsmodels uncertainties -y


* Go back to the previous Verification section and check them again.

If you are still having trouble or have any questions, please do not hesitate to visit us during office hours
or contact us via :mailto:`email <pythonsupport@dtu.dk>`
or `Discord <ps-discord-invite_>`_.
More information can be found on our :ref:`homepage <reach-us-reference>`.

