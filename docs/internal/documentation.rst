:nosearch:


.. _internal-documentation:

Writing RST documentation
-------------------------

Documentation in the majority of Python projects uses the reStructuredText
format. This is the primary reason for also choosing this format.

To get a good idea of how to format the code, please have a look
at the ``docs/python/environments.rst`` file. This contains
pretty much everything that we use in the documentation.

These links should provide you with enough details
to get started:

- https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
- https://sphinx-design.readthedocs.io/en/sbt-theme/

If you have questions, feel free to discuss on our Discord channel.


.. include:: extensions.rst.include


.. _internal-doc-good-bad:

Good or bad documentation
=========================

Writing a good documentation is extremely difficult. Aspects such as content, audience,
understandability, layout etc. are all important for users interacting with
the documentation site.

Here are some guidelines for creating the documentation in groups:

1. Select a topic you wish to expand the documentation on.

2. Take a brainstorm round, see for instance `this site <https://www.indeed.com/career-advice/career-development/how-to-brainstorm>`__
   on how to do a proper brainstorm!

   *NOTE*: In a brainstorm, nothing is a bad idea, stay positive towards ideas, sorting comes after.

   Keeping this document for future works is a good idea. Future brainstorms should be done **without**
   this document, but it can be used as a cross reference or inspiration, after a 2nd future brainstorm.

3. Reflection of the brainstorm elements. Think about the audience group, who should read it?
   How will they understand or read the content? Should it be very basic? How basic? Should we split
   advanced and beginners material? Or, can they go together? Others?

   Each element of the brainstorm should be assigned pros/cons to decide whether it is eligible for the
   documentation.

4. All positive ideas should now be described in greater detail in an overview document.
   The document should clearly discuss what content should be there (not necessarily in great detail).

   This will be your working document for creating the actual documentation.
   It should describe:

   - overview of content
   - layout of content (how to present)
   - order of appearance
   - necessary links, both external and internal links

   It is important to understand how the documentation can expose the content in the
   most favorable way.

   **IMPORTANT**: Read `this document <https://documentation.divio.com/>`__.

5. Start writing the documentation. Iterate many times, get feedback.


Using Git
=========

The documentation is hosted {{ ps_repository }}.

To start hacking on the repository, follow these steps:

A more detailed description can be found `here <https://docs.github.com/en/get-started/quickstart/fork-a-repo>`__.

*Please do not merge in the ``main`` branch as that can cause problems.*


0. Create a GitHub account `join <https://github.com/join>`__.
1. Go to {{ps_repository}}
   
   1. Fork the repository by pressing the :fas:`code-fork` icon
      
      *First time only*: If this is your first time, you probably need
      to enable an SSH key for cloning and pushing to GitHub.
      Creating a key is described `here <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=windows>`__, subsequently you should 
      follow `this instruction <https://docs.github.com/en/github-ae@latest/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account>`__.

   2. Clone your local repository to your local drive.

      Open a terminal, and change directory to where you want
      the documentation development to occur.
      Then press the green button :bdg-success:`<> Copy` and copy the line marked.
      Type ``git clone`` and paste the copied line after ``git clone`` and press
      enter.

   3. Now you should have a folder named ``pythonsupport-page``.
      This contains all the files required to build the documentation.

   4. Create a virtual environment in the same folder.

      In this one follow the instructions in the `README.md` file.

2. Now you can build it using the top level makefile system.
   
   *NOTE* I haven't tried on a Windows machine yet. So we should
   probably sit together to fix the build there.

3. Once you have build the pages you can open up your browser
   using local files, something like this in the terminal
   would work:

   .. code-block:: shell

      cd <path to the pythonsupport-page folder>
      firefox build/html/index.html

   And then it opens up the browser page (prefixed with ``file://``
   to highlight it is a local file)

