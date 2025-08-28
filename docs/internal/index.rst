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


.. tip::

   We will share internal documents with you hosted
   :full-link:`here <https://www.student.dtu.dk/~nicpa/pythonsupport/internal-files>`.

.. note::

   Please come with suggestions for how we should do stuff!


External Resources
------------------

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Tool
     - Purpose
     - Access
   * - **RT Ticketing**
     - Ticket management
     - `RT System <https://pythonsupport-rt.dtu.dk/rt/>`_
   * - **Discord**
     - Internal communication
     - `Discord Server <https://discord.gg/CSp6xS22>`_
   * - **Support Website**
     - Main support portal
     - `Support Website <https://pythonsupport.dtu.dk/>`_
   * - **Website GitHub**
     - Documentation
     - `Website Repository <https://github.com/dtudk/pythonsupport-page/>`_
   * - **Scripts GitHub**
     - Scripts for auto installation ect.
     - `Scripts Repository <https://github.com/dtudk/pythonsupport-scripts/>`_
   * - **Teams/SharePoint**
     - Documents & Personal hour registration
     - `Students documents <https://dtudk.sharepoint.com/:f:/r/sites/PythonInstallationSupport/Delte%20dokumenter/Students%20documents?csf=1&web=1&e=eEhaCK>`_
   * - **Course Reference**
     - Programming materials
     - `Course Materials <https://02002.compute.dtu.dk/>`_
   * - **DTU FUSION**
     - Time registration system
     - `DTU FUSION <https://www.fusion.dtu.dk>`_

.. contents::
   :backlinks: none
   :local:
   :depth: 1

.. _internal-com-students:
 
Interacting with students
-------------------------

Students will arrive with a variety of backgrounds. Some are very interested
in programming, while others are not interested, *at all*, in the inner workings
of Python and want to be able to attend courses.

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
     (MFA) to work, VPN, etc. they should ask AIT.
   | Mail: :mail:`itsupport@student.dtu.dk`
   | Their phone number is: +45 452 55555.
   | Located in building 189
   | Other information can be found :full-link:`here <https://www.inside.dtu.dk/en/undervisning/faglig/it-systemer-og-vaerktoejer>`.

DTU Learn
   Go here: :full-link:`https://learnsupport.dtu.dk`
Counseling for students:
   Go here: :full-link:`https://www.dtu.dk/uddannelse/vejledning/studievejledningen`


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

Daily, Weekly and Monthly Tasks
-------------------------------

Daily Tasks
^^^^^^^^^^^

.. note::
   **Every Shift**
   
   - **Check RT Ticketing System** for new support requests
   - **Monitor Discord channels** for team communications, updates and questions from students
   - **Follow the 4-step support workflow** for all user interactions
   - **Document solutions** as you resolve repeated issues (and notify the rest of the team on discord)

Weekly Tasks
^^^^^^^^^^^^

.. note::
   **Every Week**
   
   - **Review shift schedules** on Discord for any changes and updates

Monthly Tasks
^^^^^^^^^^^^^

.. important::
   **Before Month End**
   
   - **Register hours in DTU FUSION** 
   - **Register personal working hours** on SharePoint
   
   **Needs to be done before last team meeting in current month!**

Time Registration (FUSION and SharePoint/Excel)
-----------------------------------------------

To simplify the process, we have provided two options for registering hours: the official method, via Fusion, and the unofficial method, via an Excel sheet on Teams (Student Documents). In the Excel sheet, the actual hours are recorded, ensuring that the semester's total number of hours balances when the semester is over.

DTU FUSION
^^^^^^^^^^

.. tip::
   **About DTU FUSION**
   
   DTU FUSION serves as the central time tracking platform for all workers at the university. This system is mandatory for recording work hours and ensures compliance with labor regulations.

FUSION Hours Calculator
^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <div class="fusion-calculator">
     <h4>Calculate Your Monthly Hours</h4>
     <p>Enter the year and month to automatically calculate your FUSION registration hours:</p>
     
     <div class="calc-inputs">
       <label for="calc-year">Year:</label>
       <input type="number" id="calc-year" value="2025" min="2020" max="2030">
       
       <label for="calc-month">Month:</label>
       <select id="calc-month">
         <option value="1">January</option>
         <option value="2">February</option>
         <option value="3">March</option>
         <option value="4">April</option>
         <option value="5">May</option>
         <option value="6">June</option>
         <option value="7">July</option>
         <option value="8">August</option>
         <option value="9">September</option>
         <option value="10">October</option>
         <option value="11">November</option>
         <option value="12">December</option>
       </select>
       
       <button onclick="calculateHours()" id="calc-button">Calculate</button>
     </div>
     
     <div id="calc-results" class="calc-results" style="display: none;">
       <div class="results-header">Results for <span id="result-month"></span>:</div>
       <div>Total weekdays: <strong><span id="total-days"></span></strong></div>
       <div id="holidays-info" class="holidays-info" style="display: none;"></div>
       <div id="error-info" class="error-info" style="display: none;"></div>
       <div>Working days (minus 2 free days): <strong><span id="work-days"></span></strong></div>
       <div class="hours-summary">
         <div><strong>Normal contract (1.8h/day):</strong> <span id="normal-hours"></span> hours</div>
         <div><strong>Exchange student (2.0h/day):</strong> <span id="exchange-hours"></span> hours</div>
       </div>
     </div>
   </div>

   <style>
   .fusion-calculator {
     border: 1px solid var(--pst-color-border, #d0d7de);
     padding: 16px;
     margin: 20px 0;
     border-radius: 6px;
     background-color: var(--pst-color-background, #ffffff);
   }

   [data-theme="dark"] .fusion-calculator {
     border-color: var(--pst-color-border, #30363d);
     background-color: var(--pst-color-background, #0d1117);
   }

   .calc-inputs {
     margin: 15px 0;
   }

   .calc-inputs label {
     display: inline-block;
     width: 80px;
     font-weight: bold;
     margin-right: 5px;
   }

   .calc-inputs input, .calc-inputs select {
     width: 80px;
     padding: 5px;
     margin-right: 20px;
     border: 1px solid var(--pst-color-border, #d0d7de);
     border-radius: 6px;
     background-color: var(--pst-color-background, white);
     color: var(--pst-color-text-base, #24292f);
   }

   [data-theme="dark"] .calc-inputs input,
   [data-theme="dark"] .calc-inputs select {
     border-color: var(--pst-color-border, #30363d);
     background-color: var(--pst-color-background, #0d1117);
     color: var(--pst-color-text-base, #f0f6fc);
   }

   .calc-inputs select {
     width: 120px;
   }

   #calc-button {
     margin-left: 15px;
     padding: 8px 16px;
     background-color: var(--pst-color-primary, #0969da);
     color: var(--pst-color-on-primary, #ffffff);
     border: none;
     border-radius: 6px;
     cursor: pointer;
     font-weight: 500;
     transition: background-color 0.2s;
   }

   #calc-button:hover {
     background-color: var(--pst-color-primary-highlight, #0550ae);
   }

   .calc-results {
     margin-top: 15px;
     padding: 16px;
     background-color: var(--pst-color-surface, #f6f8fa);
     border-radius: 6px;
     border: 1px solid var(--pst-color-border, #d0d7de);
   }

   [data-theme="dark"] .calc-results {
     background-color: var(--pst-color-surface, #161b22);
     border-color: var(--pst-color-border, #30363d);
   }

   .results-header {
     font-weight: bold;
     margin-bottom: 10px;
   }

   .holidays-info {
     color: var(--pst-color-text-muted, #6c757d);
     font-size: 14px;
     margin: 5px 0;
   }

   .error-info {
     color: var(--pst-color-danger, #dc3545);
     font-size: 14px;
     margin: 5px 0;
     font-weight: bold;
   }

   .hours-summary {
     margin-top: 12px;
     padding: 12px;
     background-color: var(--pst-color-success, #dafbe1);
     border-radius: 6px;
     border: 1px solid var(--pst-color-success-border, #2da44e);
   }

   [data-theme="dark"] .hours-summary {
     background-color: rgba(46, 164, 79, 0.15);
     border-color: var(--pst-color-success-border, #238636);
   }
   </style>

   <script>
   // DTU paid holidays hardcoded by year (based on DTU Medarbejderguide and Danish holidays)
   const dtuHolidays = {
     // Fixed DTU paid holidays (same date every year)
     fixed: {
       '01-01': 'Nytårsdag (New Year\'s Day)',
       '06-05': 'Grundlovsdag (Constitution Day)',
       '12-24': 'Juleaftensdag (Christmas Eve)',
       '12-25': 'Juledag (Christmas Day)',
       '12-26': '2. juledag (Boxing Day)',
       '12-31': 'Nytårsaftensdag (New Year\'s Eve)'
     },
     
     // Variable DTU paid holidays by year (Easter-dependent)
     variable: {
       2025: {
         '04-17': 'Skærtorsdag (Maundy Thursday)',
         '04-18': 'Langfredag (Good Friday)',
         '04-21': '2. påskedag (Easter Monday)',
         '05-01': 'Første maj (May Day)',
         '05-29': 'Kristi himmelfartsdag (Ascension Day)',
         '06-09': '2. pinsedag (Whit Monday)'
       }
       // Add more years as needed: 2026, 2027, etc.
     }
   };
   
   function getHolidayData(year) {
     if (!dtuHolidays.variable[year]) {
       throw new Error(`Holiday data for ${year} not available. Please add holidays for this year.`);
     }
     return {
       fixed: dtuHolidays.fixed,
       variable: dtuHolidays.variable[year]
     };
   }
   
   function isHoliday(date, holidayData) {
     const month = String(date.getMonth() + 1).padStart(2, '0');
     const day = String(date.getDate()).padStart(2, '0');
     const dateStr = `${month}-${day}`;
     
     // Check fixed holidays
     if (holidayData.fixed && holidayData.fixed[dateStr]) {
       return holidayData.fixed[dateStr];
     }
     
     // Check variable holidays
     if (holidayData.variable && holidayData.variable[dateStr]) {
       return holidayData.variable[dateStr];
     }
     
     return false;
   }
   
   function calculateHours() {
     const year = parseInt(document.getElementById('calc-year').value);
     const month = parseInt(document.getElementById('calc-month').value);
     
     // Clear previous results and errors
     document.getElementById('holidays-info').style.display = 'none';
     document.getElementById('error-info').style.display = 'none';
     
     try {
       // Get holiday data for the year
       const holidayData = getHolidayData(year);
       
       // Calculate working days with Danish holidays
       const date = new Date(year, month - 1, 1);
       const lastDay = new Date(year, month, 0).getDate();
       let workingDays = 0;
       let holidaysFound = [];
       
       for (let day = 1; day <= lastDay; day++) {
         date.setDate(day);
         const dayOfWeek = date.getDay();
         const holiday = isHoliday(date, holidayData);
         
         if (dayOfWeek !== 0 && dayOfWeek !== 6 && !holiday) {
           // Not weekend and not holiday
           workingDays++;
         } else if (holiday && dayOfWeek !== 0 && dayOfWeek !== 6) {
           // Holiday on weekday
           holidaysFound.push(holiday);
         }
       }
       
       const workDays = workingDays - 2; // Minus 2 free days
       const normalHours = workDays * 1.8;
       const exchangeHours = workDays * 2.0;
       
       // Display results
       const monthNames = ["", "January", "February", "March", "April", "May", "June", 
                          "July", "August", "September", "October", "November", "December"];
       
       document.getElementById('result-month').textContent = `${monthNames[month]} ${year}`;
       document.getElementById('total-days').textContent = `${workingDays} working days`;
       document.getElementById('work-days').textContent = workDays;
       document.getElementById('normal-hours').textContent = normalHours.toFixed(1);
       document.getElementById('exchange-hours').textContent = exchangeHours.toFixed(1);
       
       // Show holidays info if any were found
       if (holidaysFound.length > 0) {
         document.getElementById('holidays-info').textContent = `Holidays excluded: ${holidaysFound.join(', ')}`;
         document.getElementById('holidays-info').style.display = 'block';
       }
       
       document.getElementById('calc-results').style.display = 'block';
       
     } catch (error) {
       // Show error message
       document.getElementById('error-info').textContent = `Error: ${error.message}`;
       document.getElementById('error-info').style.display = 'block';
       document.getElementById('calc-results').style.display = 'block';
       
       // Hide other result elements when there's an error
       document.getElementById('total-days').textContent = 'N/A';
       document.getElementById('work-days').textContent = 'N/A';
       document.getElementById('normal-hours').textContent = 'N/A';
       document.getElementById('exchange-hours').textContent = 'N/A';
     }
   }
   
   // Set current month as default
   document.getElementById('calc-month').value = new Date().getMonth() + 1;
   </script>

How to Register Your Hours
^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow these steps to record your working hours in FUSION:

1. **Log into FUSION**
   
   - Navigate to: https://www.fusion.dtu.dk

2. **Access Time Sheet**
   
   - Go to **'Time and Absence'** to edit your current time sheet
   
   .. figure:: /images/onboarding/fusion_steps/step1.png
      :alt: Step 2: Access time Sheet
      
      Step 2: Access time Sheet

3. **Register Working Hours**
   
   - Pick a day to register your total working hours for the month
   - Use the **FUSION Hours Calculator** above to calculate your exact hours, which automatically accounts for DTU paid holidays and your two free days per month
   
   .. figure:: /images/onboarding/fusion_steps/step2.png
      :alt: Step 3.1: Add Entry
      
      Step 3.1: Add Entry

   .. figure:: /images/onboarding/fusion_steps/step3.png
      :alt: Step 3.2: Register Hours
      
      Step 3.2: Register Hours

4. **Register Free Days**
   
   - Register two free days with 1.8 hours each (or 2.0 hours for exchange students): Chose absence under *Task*

5. **Submit Timesheet**
   
   - Review and submit your completed timesheet
   
   .. figure:: /images/onboarding/fusion_steps/step4.png
      :alt: Step 4: Submit Timesheet
      
      Step 4: Submit Timesheet

Getting Help with FUSION
^^^^^^^^^^^^^^^^^^^^^^^^^

If you need assistance with FUSION, contact:

- Your colleagues during shifts
- Your direct supervisor
- HR support for technical issues

.. important::
   **IMPORTANT: Monthly Deadline**
   
   You must register your hours before the end of the month. Otherwise you will get a warning from HR requiring you to do it.

SharePoint
^^^^^^^^^^

Monthly tasks also include:

- **Register personal working hours** on `SharePoint <https://dtudk.sharepoint.com/:f:/r/sites/PythonInstallationSupport/Delte%20dokumenter/Students%20documents?csf=1&web=1&e=eEhaCK>`_
- This is in addition to the DTU FUSION registration

Onboarding
----------

Our Mission & Your Responsibilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   **Our Mission**
   
   We aim to provide prompt, dependable, and compassionate support to our users.

Team Values
^^^^^^^^^^^

.. note::
   **Our Core Principles**
   
   - **Empathy first:** Every interaction matters
   - **Be curious:** Ask questions, seek clarity
   - **Collaborate:** Work openly with team members
   - **Own it:** Take initiative, follow through
   - **Improve constantly:** Be proactive, suggest better processes and tools

Support Workflow
^^^^^^^^^^^^^^^^

The 4-Step Process
^^^^^^^^^^^^^^^^^^

1. **Ticket Intake**
   
   - Regularly check for new requests
   - Assign and acknowledge them within your shift

2. **Triage & Troubleshoot**
   
   - Identify the root issue
   - Check the documentation before escalating

3. **Resolution**
   
   - Provide solutions or workarounds
   - Follow up to confirm resolution

4. **Student Hands-on**
   
   - Guide the user in solving the issue(s)
   - Let the user do the work

Your Responsibilities
^^^^^^^^^^^^^^^^^^^^^

As a Python Installation Support team member, you will:

- Respond to requests, inquiries or tickets via physical presence/chat/support portal
- Troubleshoot technical or operational issues
- Document solutions and processes
- Report your findings in Discord
- Collaborate with team members to resolve issues
- Help maintain and improve our support knowledge base
- Participate in teamwork on various projects
- Suggest edits to existing articles
- Create internal guides when gaps are identified

.. tip::
   **Golden Rule**
   
   **If you solve a problem more than twice, document it in GitHub.**

Getting Started
^^^^^^^^^^^^^^^

Accounts & Access
^^^^^^^^^^^^^^^^^

You'll need access to these essential systems:

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - System
     - Purpose
     - Link
   * - **Discord**
     - Internal communication
     - `Discord Server <https://discord.gg/CSp6xS22>`_
   * - **RT Ticketing**
     - Ticket management
     - `RT System <https://pythonsupport-rt.dtu.dk/rt/>`_
   * - **SharePoint**
     - Documents & personal time registration
     - `SharePoint Documents <https://dtudk.sharepoint.com/:f:/r/sites/PythonInstallationSupport/Delte%20dokumenter/Students%20documents?csf=1&web=1&e=LVnQbU>`_
   * - **DTU FUSION**
     - Official time registration
     - `DTU Fusion <https://www.fusion.dtu.dk>`_

Key Meetings
^^^^^^^^^^^^

.. important::
   **Important Schedule**
   
   - **Team kick-off** approx. a month before the semester starts
   - **One-on-one** with your direct manager
   - **Team introductions** with all members
   - **During semester** weekly status meeting with all members (approx. 30 min)

Required before you start
^^^^^^^^^^^^^^^^^^^^^^^^^

Self-study:

- Getting familiar with the Python Installation Support site and subsites

You'll complete training on:

- Product walkthrough (internal tools, user-facing systems)
- Using the ticketing system and Discord
- DTU FUSION time registration system setup and usage

Success Milestones
^^^^^^^^^^^^^^^^^^

After 30 Days
^^^^^^^^^^^^^

By the end of your first month, you should be able to:

- **Confidently use all core tools**
- **Independently manage and resolve tickets**
- **Be familiar with team workflows**
- **Feel comfortable asking for help when needed**

:ref:`Customizing Sphinx  <internal-sphinx>`
--------------------------------------------

Sphinx documentation can be found :ref:`here <internal-sphinx>`.

Piwik setup
-----------

Piwik setup is documented :ref:`here <piwik-documentation>`.

Piwik custom event tutorial can be found :ref:`here <piwik-custom-event-tutorial>`.


:ref:`Panopto tutorial <internal-panopto>`
------------------------------------------

How to use Panopto and how to make video tutorials are documented :ref:`here <internal-panopto>`.

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
