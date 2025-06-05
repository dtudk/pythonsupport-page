{{course_full_name}} - {{metadata.course_identifier}}
---------------------------------------------------

In order to install python requirements for {{course_full_name}} {{metadata.course_identifier}} do the following steps.

.. card:: Install course environment steps

    #.

        Make sure that you have a Conda installation on your PC. If you do not have a Conda installation on your computer please follow :ref:`these instructions <install-python>`.

    #.
        Run the following command in a terminal to create a Conda environment with all course requirements. 

        .. code:: bash

            conda env create -f "{{metadata.env_path}}" -n "{{metadata.course_env_name}}"
    
    #.

        When the above command has finished, a new Conda environment named "{{metadata.course_env_name}}" will have been installed on your computer. In order to use it, follow the activation guides bellow.

.. dropdown:: Activate environment in Visual Studio Code

        1. Press :kbd:`Ctrl+Shift+P` (windows), :kbd:`Cmd+Shift+P` (macos)
        2. Type *Python: Select Interpreter* and press :kbd:`Enter` once this shows up under the options 

            .. image:: ../../learn-more/images/VScode_windows2.png
                :width: 100%
                :align: center
                :alt: IDLE Shell

        3. Choose the option similar to ``Python x.x.x ('{{metadata.course_env_name}}')``.
            
            .. image:: ../../learn-more/images/VScode_windows3.png
                :width: 100%
                :align: center
                :alt: IDLE Shell

.. dropdown:: Activate environment in Jupyter Notebook

    You can select the course environment by going to the upper right corner, clicking :menuselection:`Select Kernel`, and then choose ``{{metadata.course_env_name}} (Python x.x.x)``.

        .. image:: /learn-more/images/VSC-select-kernel.png
            :width: 100%
            :align: center

    .. tip::
        If you accidentally choose the wrong kernel, don't worry, you can always go back by clicking the Python version you're currently using and then changing it.


.. dropdown:: Activate environment in terminal

    In order to activate the course environment in a terminal, run the following command:

    .. code:: bash
        conda activate {{metadata.course_env_name}}
