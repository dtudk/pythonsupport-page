
.. meta::
   :description: Technical University of Denmark (DTU) IT Cafe
   :keywords: IT, file, directory, directories, compress, zip


Drop-in Café Basic IT skills
==================================


* Are you struggling with using your computer?
* Are you in doubt of how to organize your files in your new role as a student?


DTU has initiated a new initiative that teaches students how to manage, use,
and navigate their computer file systems. We also strive to make basic terminologies
apparent and descriptive to enable you as a student.



When?
-------

The Drop-in Cafe will be open 

* in weeks 38 --- 49 (except 42).
* in building 306, 1st floor
* Tuesday and Thursdays between 17-19.



Activities
------------

* File System scavenger hunt

   
  .. card::

     A visual exploration of how files and folders are organized on
     a computer.

     After this activity the student will have experience in:

     - Understanding the file-explorer, navigating up/down in the file-tree

     - Understand what editing files *means* for a computer, i.e. that
       edits are not done implicitly on the file system

     - Know that renaming files is equivalent to moving files (and vice versa)

     - Understand where Downloaded files (from a browser) is placed in the
       file system.

* More are in the works...



Terminology
------------

This is a non-exhaustive list of terminologies used when interacting with a computer.
Some are language specific which means they may have different names on your computer
if you have a different language setting (e.g. :guilabel:`File Explorer` on Windows is named :guilabel:`Stifinder` in the Danish version). 


.. list-table:: Terminology
   :header-rows: 1

   * - Term
     - Explanation

   * - File/folder tree
     - The hierarchical structure of directories and files on a computer.
   
   * - Filesystem
     - The actual representation of the file/folder tree on the computers harddrives (disks).

   * - .. _it-skills-tbl-file-explorer:

       File Explorer/Finder
     - The operating systems interactive view of the File/folder tree.
       This is the primary way for users of a computer to interact with their files
       and folders.

   * - Extension
     - Files can have *extensions* that is formatted by a ``.`` and the extension.
       E.g. ``.txt``. The extension informs the operating system how the file should
       be handled. For instance ``.docx`` files are Word documents, ``.py`` files
       are Python scripts.

   * - Path
     - The full file-tree name of a file or folder in the file/folder tree.
       E.g. ``C:\Users\MyName\my_document.docx``.

   * - Compressed files
     - Files can be reduced in size by re-arranging the internals of the file.
       This makes them unreadable until one decompresses the files.

       Some files are more susceptible to large compression (text files), while
       other files will rarely be compressed further (JPEG images).

   * - Command
     - An instruction given to a computer program on the command line interface (terminal)

   * - Directory separator
     - On {{ windows }} the directory separator is ``\``, while for {{ macos }}, the separator
       is ``/``.

   * - .. _it-skills-tbl-hard-disk:

       Hard disk/drive
     - The hardware that hosts everything on the computer. The operating system, files
       required for the computer to work, as well as files that the user creates, images,
       text documents, etc.

   * - Memory
     - A dedicated place of space meant for the operating system to hold temporary disk space.
       This is very fast for the computer to work with. As opposed to the :ref:`Hard disk <it-skills-tbl-hard-disk>` which is rather slow.

   * - Cloud/Remote storage
     - A :ref:`hard disk <it-skills-tbl-hard-disk>` that is not physically on your computer.
       It is located somewhere else in the world, and requires internet access to interact
       with files on said storage.

   * - Terminal
     - A program that allows one to execute commands by *writing what to do*.
       See :ref:`this table for commands <it-skills-tbl-term>`.

   * - PowerShell ({{windows}})
     - The recommended terminal program in Windows.

   * - Command prompt ({{windows}})
     - A non-recommended terminal program in Windows.

       Windows has both PowerShell and Command prompt. We highly encourage
       users to stick with PowerShell.


.. _it-skills-tbl-term:

.. list-table:: Terminal
   :header-rows: 1

   * - Command
     - What it does?
   * - ``cd <dir>``
     - Changes the current directory to ``<dir>``.
       Equivalent to double-clicking the folder ``<dir>`` in your :ref:`File Explorer/Finder <it-skills-tbl-file-explorer>`.
   * - ``ls``
     - List the files and directories in the the current directory.
       Equivalent to viewing files and folders in the :ref:`File Explorer/Finder <it-skills-tbl-file-explorer>`.

   * - ``mv <from> <to>``
     - Will move file/folder ``<from>`` to ``<to>``.

       Notice that ``mv file1 file2``
       will simply rename the file from ``file1`` to ``file2``.
   
   * - ``rm <?>``
     - Deletes files/folders named ``<?>``.

   * - ``python3``
     - Used to run Python programs from the terminal. Either scripts or interactively.


.. _it-skills-tbl-mac:

.. list-table:: {{macos}} specific terms
   :header-rows: 1

   * - Term
     - Explanation

   * - :guilabel:`Applications` folder
     - The directory on {{macos}} where installed applications are stored.
       Deleting applications here will uninstall them.

   * - :guilabel:`Dock`
     - The Dock is a place to fast access certain applications and features.
       It can be re-arranged to any of the screen edges. By default
       it is located at the bottom of the screen.
   
   * - :guilabel:`Finder`
     - The :ref:`File Explorer <it-skills-tbl-file-explorer>` for {{macos}}.

   * - ``/``
     - The directory separator for {{macos}}.


.. _it-skills-tbl-windows:

.. list-table:: {{windows}} specific terms
   :header-rows: 1

   * - Term
     - Explanation

   * - :guilabel:`Add/Remove Programs`
     - Allows uninstalling Programs. Generally applications are installed through
       dedicated files, so this feature is typically only used for uninstalling software.

   * - :guilabel:`File Explorer`
     - The :ref:`File Explorer <it-skills-tbl-file-explorer>` for {{windows}}.

   * - ``\``
     - The directory separator for {{windows}}.

