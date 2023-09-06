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
- https://sphinx-design.readthedocs.io/en/furo-theme/

If you have questions, feel free to discuss on our Discord channel.


Using Git
=========

The documentation is hosted {{ ps_repository }}.

To start hacking on the repository, follow these steps:

0. Create a GitHub account `join <https://github.com/join>`__.
1. Go to {{ps_repository}}
   
   1. Fork the repository by pressing the :fas:`code-fork` icon
      
      *First time only*: If this is your first time, you probably need
      to enable an SSH key for cloning and pushing to GitHub.
      Follow `this instruction <https://docs.github.com/en/github-ae@latest/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account>`__.

   2. Clone your local repository to your local drive.

      Open a terminal, and change directory to where you want
      the documentation development to occur.
      Then press the green button :bdg-success:`<> Copy` and copy the line marked.
      Type ``git clone`` and paste the copied line after ``git clone`` and press
      enter.

   3. Now you should have a folder named ``pythonsupport-page`` at the 

