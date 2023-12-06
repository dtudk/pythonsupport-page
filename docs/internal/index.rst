:orphan:
:nosearch:

.. Ensure that the build does not create a warning
   when not explicitly included.
   Also ensure that the search function does not return
   results from this file.

.. _internal:


Internal information (Supporters)
=================================

This page is intended for the hired supporters and will be used to share information
and new technologies we (the Python support) will look into.
Thus our knowledge will be expanded as new things surface.

.. note::

   Please come with suggestions for how we should do stuff!



.. contents::
   :backlinks: none
   :local:

.. _internal-com-students:
 
Interacting with students
-------------------------

Students will arrive with a variety of backgrounds. Some are very interested
in programming, while others are not interested, *at all*, in the inner workings
of Python and simply want to be able to attend courses.

.. tip::
   Sometimes you will get frustrated that your message did not come across,
   or that the questioner keeps misunderstanding what you asked them to do.
   This is natural. There is no other way but to repeat the entire procedure, in
   greater detail, and politely explain them why things may go wrong. **Patience!**

Our goal is to support both ends of the student spectrum.
Information overload can be a problem for new students as there is already
enough on the plate. It is imperative that information is given at the level
of the student and at the pace that might be interesting for the student.
Always ask if they want more information, before recommending best practices for
something they do not really care for.

If it seems that the student *just* want a working installation, then opt in to
aid with few, if any, side steps.

   
.. danger::
   Engaging through online channels may, sometimes, spur comments that are
   inappropriate.

   It is important that you do not put anything personal into such comments.
   It is generally a sign of frustration! So take 2 min off the screen to
   cool down. And then return with a polite and firm message. Something
   like this could be used:

       Please keep the tone polite and open. We will not accept any form of
       harassment and/or bullying through our channels.
       We are trying to aid to the best of our abilities, and sometimes
       we encounter problems we have never experienced before.

   *search for 'handle inappropriate comments' and you'll find plenty of useful
   content*

   Then wait a bit more to engage further with the questioner to ensure the
   message came across.
   If you, at **any** time feel uncomfortable, let us know immediately. It shall not,
   and will not be tolerated!

   Please, openly, discuss this with the team. We are all here for each other! :fas:`people-group`


Questioners will undoubtedly ask questions outside our scope.
The best approach would be to *guess* who/where the question could be answered.
For instance if the question is related to a Python programming problem, one could
close it like this:

   We, the Python installation support, cannot engage in support on Python
   programming problems. If this is related to a DTU course, we have to refer
   you to the course teaching assistants, or the teacher.

   Otherwise, you can ask your question to other students in the #general
   channel.

   Thanks for your understanding!

General IT questions
   | If they have questions related to Wireless, getting Multi-Factor-Authentication
     (MFA) to work, etc. they should ask AIT.
   | Mail: :mail:`itsupport@student.dtu.dk`
   | Their phone number is: +45 452 55555.
   | Office hours 305.027 8:00--15:00.
DTU Learn
   Go here: :full-link:`https://learnsupport.dtu.dk`


.. warning::

   **Professional Secrecy**

   While working with the students, you might see and learn about things
   not directly relevant to your job. As an employee of DTU, you are obliged to keep that
   knowledge secret.

.. _internal-opening-questions:

Opening questions when mailing/chatting with questioners
--------------------------------------------------------

Here is a short item list of questions that may be useful for asking them.
They are in code blocks so you can easily copy paste them directly into
the Discord message/email system.

Quite often we tend to suggest solutions before we know the exact problem.
It can be very useful to get some basic information about the system, before suggesting
workarounds.

.. code-block:: shell

   - Which operating system, Windows, MacOS, Linux?
   - How did you install Python? App-store, download link, anaconda, other?
   - If Windows, did you remember to check the ``Add ... to PATH`` box? If unsure, reinstall using App-store.
   - Are you using virtual environments? If you are not sure, probably not. :)
   - Are you using multiple Python versions on the same machine? Can cause conflicts.


.. _internal-com-other:

Interacting with each other
---------------------------

Since we all have a variety of backgrounds, our ways of solving problems
will be a diverse set of methods.

Always respect your co-workers solution methods, even though you would prefer
other methods.

This is not to say that we can not learn from each other, but doing so should be done
with respect, and tolerance towards disagreements.

It is vital we also keep a nice and healthy internal tone.

.. note::
   Try not to engage in other supporters threads/tickets.

   If you really do think engaging would be a good idea, always, **always**,
   ask the supporter through private channels (RT: comment, Discord: @<username>)
   before engaging with the questioner.

   Secondly, you will sometimes see a thread/ticket open from another supporter.
   This could be due to their shift was over, or that they had some other things to
   attend to. If a lot of time has passed, you can *take over* the ticket/question.
   Please always remember to notify the original supporter that you took over the ticket.
   Something like this could be used:

       I saw that your time was limited on ticket/question ####, I took the liberty
       of continuing the ticket. Feel free to let me know if I should leave it to you,
       or if there is anything else you may find important for this question! Thanks!


.. include:: /internal/discord.rst.include
.. include:: /internal/rt.rst.include


:ref:`Exercises <internal-exercises>`
-------------------------------------

Go :ref:`here <internal-exercises>` for the exercises.


:ref:`Editing documentation <internal-documentation>`
-----------------------------------------------------

Go :ref:`here <internal-documentation>` for instructions on how to
fix/add new documentation.


.. toctree::
   :maxdepth: 1
   :hidden:

   exercises.rst
   documentation.rst
