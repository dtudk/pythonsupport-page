
{{course_full_name}} - {{course_year}} {{course_semester}}
--------------------------------------------------------------------------

In order to install Python requirements for ``{{course_full_name}}`` do the following steps.

.. card:: Install course environment steps

    #.

        Make sure that you have a Conda installation on your PC.
        If you do not have a Conda installation on your computer please follow :ref:`these instructions <install-python>`.

    #.
        Run the following command in a terminal to create a Conda environment with all course requirements.

        .. code:: bash

            conda env create -f "{{env_path}}" -n {{course_env_name}}

    #.
        When the above command has finished, a new Conda environment named ``{{course_env_name}}`` will have been installed on your computer.
        In order to use it, follow the activation guides bellow.

.. dropdown:: Activate in VS Code

        1. Press :kbd:`Ctrl+Shift+P` (Windows), :kbd:`Cmd+Shift+P` (MacOS)
        2. Type *Python: Select Interpreter* and press :kbd:`Enter` once this shows up under the options

            .. image:: /learn-more/images/VScode_windows2.png
                :width: 100%
                :align: center
                :alt: IDLE Shell

        3. Choose the option similar to ``Python 3.x.x ('{{course_env_name}}')``.

            .. image:: /learn-more/images/VScode_windows3.png
                :width: 100%
                :align: center
                :alt: IDLE Shell

.. dropdown:: Activate in Jupyter Notebook (VS Code)

    You can select the course environment by going to the upper right corner, clicking :menuselection:`Select Kernel`, and then choose ``{{course_env_name}} (Python 3.x.x)``.

        .. image:: /learn-more/images/VSC-select-kernel.png
            :width: 100%
            :align: center

    .. tip::
        If you accidentally choose the wrong kernel, do not worry, you can always go back by clicking the Python version you are currently using and then changing it.


.. dropdown:: Activate in Terminal

    In order to activate the course environment in a terminal, run the following command:

    .. code:: bash

        conda activate {{course_env_name}}
