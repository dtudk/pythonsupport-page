:orphan:

.. meta::
   :description: Technical University of Denmark (DTU) IT Cafe
   :keywords: IT, file, directory, directories, compress, zip

.. _it-skills:

Drop-in Café Basic IT skills
==================================


* Are you struggling with using your computer?
* Are you in doubt of how to organize your files in your new role as a student?


DTU has initiated a new initiative that teaches students how to manage, use,
and navigate their computer file systems. We also strive to make basic terminologies
apparent and descriptive to enable you as a student.


.. _it-skills-when:

When?
-------

The Drop-in Cafe will be open

* in weeks 38 --- 49 (except 42).
* in building 306, 1st floor
* Tuesday and Thursdays between 17-19.


.. _it-skills-activities:

Activities
------------

* Analogue file system scavenger hunt

  .. card::

     A visual exploration of how files and folders are organized on
     a computer.

     After this activity the student will have experience in:

     - Understanding the file-explorer

     - Know that renaming files is equivalent to moving files (and vice versa)

* Digital file system scavenger hunt

  .. card::

     File used during exercise:
     :download:`ScavengerHunt.pdf <files/ScavengerHunt.pdf>`

     A direct exploration of how files and folders are organized on
     a computer.

     After this activity the student will have experience in:

     - Understanding the file-explorer, navigating up/down in the file-tree

     - Understand what editing files *means* for a computer, i.e. that
       edits are not done implicitly on the file system

     - Know that renaming files is equivalent to moving files (and vice versa)

     - Understand where Downloaded files (from a browser) are placed in the
       file system.

* More are in the works...


.. _it-skills-terminology:

Terminology
------------

This is a non-exhaustive list of terminologies used when interacting with a computer.
Some are language specific which means they may have different names on your computer
if you have a different language setting
(e.g. Windows :guilabel:`File Explorer` is named :guilabel:`Stifinder` in the Danish version).


.. list-table:: Terminology
   :header-rows: 1

   * - English
     - Dansk
     - Explanation

   * - File/folder tree
     - Fil/mappe struktur
     - The hierarchical structure of directories and files on a computer.

   * - Filesystem
     - Filsystem
     - The actual representation of the file/folder tree on the computers harddrives (disks).

   * - .. _it-skills-tbl-file-explorer:

       File Explorer/Finder
     - Stifinder/Finder
     - The operating systems interactive view of the File/folder tree.
       This is the primary way for users of a computer to interact with their files
       and folders.

   * - .. _it-skills-tbl-extension:

       Extension
     - Filtypenavn
     - Files can have *extensions* that is formatted by a ``.`` and the extension.
       The extension informs the operating system how the file should
       be handled. For instance ``.docx`` files are Word documents, ``.py`` files
       are Python scripts.

   * - .. _it-skills-tbl-favorites:

       Favorites
     - Favoritter
     - Easy access folders in your :ref:`File Explorer/Finder <it-skills-tbl-file-explorer>`.
       These are typically located to the top-left with `Desktop`, `Downloads`, `Documents`, etc.
       Add your most commonly used folders here by drag-and-dropping folders into the list.

   * - .. _it-skills-tbl-desktop:

       Desktop
     - Skrivebord
     - A special folder that is shown when you turn on your machine.
       However, in the filesystem this is just a regular folder, like any other.

       This folder is user dependent, and thus exists in the file tree below
       the user.

   * - .. _it-skills-tbl-path:

       Path
     - Sti
     - The full file-tree name of a file or folder in the file/folder tree.
       E.g. ``C:\Users\MyName\my_document.docx``.

   * - Compressed files
     - Komprimeret filer
     - Files can be reduced in size by re-arranging the internals of the file.
       This makes them unreadable until one decompresses the files.

       Some files are more susceptible to large compression (text files), while
       others will rarely be compressed further (JPEG images).

   * - .. _it-skills-tbl-command:

       Command
     - Kommando
     - An instruction given to a computer program on the command line interface (terminal).

   * - Command line interface
     - Kommando linje
     - Another name for a :ref:`Terminal <it-skills-tbl-terminal>`.

   * - Directory separator
     - Mappe separator
     - On {{ windows }} the directory separator is ``\``, while for {{ macos }}, the separator
       is ``/``.

   * - .. _it-skills-tbl-hard-disk:

       Hard disk/drive
     - Hard disk/drev
     - The hardware that stores everything on the computer. The operating system, files
       required for the computer to work, as well as files that the user creates; images,
       text documents, etc.

   * - Memory/RAM
     - Hukommelse
     - A dedicated place of space meant for the operating system to hold temporary disk space.
       This is very fast for the computer to work with. As opposed to the :ref:`Hard disk <it-skills-tbl-hard-disk>` which is rather slow.

   * - Cloud/Remote storage
     - Skylager
     - A :ref:`hard disk <it-skills-tbl-hard-disk>` that is not physically on your computer.
       It is located somewhere else in the world, and requires internet access to interact
       with files on said storage.

   * - :guilabel:`Trash`
     - :guilabel:`Papirkurv`
     - Deleting files will, generally, move the files to the trash-bin (typically located
       on your :ref:`Desktop <it-skills-tbl-desktop>`, or in your :ref:`favourites <it-skills-tbl-favorites>`).

       This allows one to recover files that were not intended to be deleted, but most
       importantly, they still occupy disk-space on your :ref:`hard drive <it-skills-tbl-hard-disk>`. Deleting files in the :guilabel:`Trash` will completely delete it.

   * - .. _it-skills-tbl-terminal:

       Terminal
     - Terminal
     - A program that allows one to execute :ref:`commands <it-skills-tbl-command>`
       by *writing what to do*.

       See :ref:`this table for commands <it-skills-tbl-term>`.

   * - Shell
     - Skal
     - Another name for a :ref:`Terminal <it-skills-tbl-terminal>`.

   * - Console
     - Konsol
     - Another name for a :ref:`Terminal <it-skills-tbl-terminal>`.


.. _it-skills-tbl-term:

.. list-table:: Terminal :ref:`commands <it-skills-tbl-command>`
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
       will rename the file from ``file1`` to ``file2``.

   * - ``rm <?>``
     - Deletes files/folders named ``<?>``.

   * - ``pwd``
     - Shows the currently *opened* directory in the terminal.

   * - ``conda``
     - Package manager for Python programs.

   * - ``python``/``python3``
     - Used to run Python programs from the terminal. Either scripts or interactively.


.. _it-skills-tbl-mac:

.. list-table:: {{macos}} specific terms
   :header-rows: 1

   * - English
     - Dansk
     - Explanation

   * - :guilabel:`Applications` folder
     - :guilabel:`Programmer` folder
     - The directory on {{macos}} where installed applications are stored.
       Deleting applications here will uninstall them.

   * - :guilabel:`Dock`
     - :guilabel:`Dock`
     - The Dock is a place to fast access certain applications and features.
       It can be re-arranged to any of the screen edges. By default
       it is located at the bottom of the screen.

   * - :guilabel:`Finder`
     - :guilabel:`Finder`
     - The :ref:`File Explorer <it-skills-tbl-file-explorer>` for {{macos}}.

   * - ``/``
     - ``/``
     - The directory separator for {{macos}}.

   * - ``bash``
     - ``bash``
     - A commonly encountered terminal program in {{macos}}.

       ``bash`` and ``zsh`` can be considered equivalent.

   * - ``zsh``
     - ``zsh``
     - A commonly encountered terminal program in {{macos}}.

       ``bash`` and ``zsh`` can be considered equivalent.


.. _it-skills-tbl-windows:

.. list-table:: {{windows}} specific terms
   :header-rows: 1

   * - English
     - Dansk
     - Explanation

   * - :guilabel:`Add/Remove Programs`
     - :guilabel:`Tilføj/Fjern Programmer`
     - Allows uninstalling Programs. Generally applications are installed through
       dedicated files, so this feature is typically only used for uninstalling software.

   * - :guilabel:`File Explorer`
     - :guilabel:`Stifinder`
     - The :ref:`File Explorer <it-skills-tbl-file-explorer>` for {{windows}}.

   * - ``\``
     -
     - The directory separator for {{windows}}.

   * - PowerShell
     - PowerShell
     - The recommended terminal program in Windows.

   * - .. _it-skills-tbl-windows-command-prompt:

       Command prompt
     - Kommando prompt
     - A non-recommended terminal program in Windows.

       Many :ref:`commands <it-skills-tbl-command>` listed in :ref:`it-skills-tbl-term`
       does not work in the command prompt. We thus highly recommend users to
       stick with PowerShell.

   * - CMD
     - CMD
     - Same as :ref:`Command prompt <it-skills-tbl-windows-command-prompt>`.


