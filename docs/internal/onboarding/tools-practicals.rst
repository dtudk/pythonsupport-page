:orphan:
:nosearch:

===============================
Tools & Practicals
===============================

Primary Tools
=============

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

Registering Working Hours
=========================

To simplify the process, we have provided two options for registering hours: the official method, via Fusion, and the unofficial method, via an Excel sheet on Teams (Student Documents). In the Excel sheet, the actual hours are recorded, ensuring that the semester's total number of hours balances when the semester is over.

DTU FUSION
==========

.. tip::
   **About DTU FUSION**
   
   DTU FUSION serves as the central time tracking platform for all workers at the university. This system is mandatory for recording work hours and ensures compliance with labor regulations.

FUSION Hours Calculator
-----------------------

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
---------------------------

Follow these steps to record your working hours in FUSION:

1. **Log into FUSION**
   
   - Navigate to: https://www.fusion.dtu.dk

2. **Access Time Sheet**
   
   - Go to **'Time and Absence'** to edit your current time sheet
   
   .. figure:: ../../images/onboarding/fusion_steps/step1.png
      :alt: Step 2: Access time Sheet
      
      Step 2: Access time Sheet

3. **Register Working Hours**
   
   - Pick a day to register your total working hours for the month
   - Use the **FUSION Hours Calculator** above to calculate your exact hours, which automatically accounts for DTU paid holidays and your two free days per month
   
   .. figure:: ../../images/onboarding/fusion_steps/step2.png
      :alt: Step 3.1: Add Entry
      
      Step 3.1: Add Entry

   .. figure:: ../../images/onboarding/fusion_steps/step3.png
      :alt: Step 3.2: Register Hours
      
      Step 3.2: Register Hours

4. **Register Free Days**
   
   - Register two free days with 1.8 hours each (or 2.0 hours for exchange students): Chose absence under *Task*

5. **Submit Timesheet**
   
   - Review and submit your completed timesheet
   
   .. figure:: ../../images/onboarding/fusion_steps/step4.png
      :alt: Step 4: Submit Timesheet
      
      Step 4: Submit Timesheet

Getting Help with FUSION
-------------------------

If you need assistance with FUSION, contact:

- Your colleagues during shifts
- Your direct supervisor
- HR support for technical issues

.. important::
   **IMPORTANT: Monthly Deadline**
   
   You must register your hours before the end of the month. Otherwise you will get a warning from HR requiring you to do it.


SharePoint
==========

Monthly tasks also include:

- **Register personal working hours** on `SharePoint <https://dtudk.sharepoint.com/:f:/r/sites/PythonInstallationSupport/Delte%20dokumenter/Students%20documents?csf=1&web=1&e=eEhaCK>`_
- This is in addition to the DTU FUSION registration

Daily, Weekly and Monthly Tasks
===============================

Daily Tasks
-----------

.. note::
   **Every Shift**
   
   - **Check RT Ticketing System** for new support requests
   - **Monitor Discord channels** for team communications, updates and questions from students
   - **Follow the 4-step support workflow** for all user interactions
   - **Document solutions** as you resolve repeated issues (and notify the rest of the team on discord)

Weekly Tasks
------------

.. note::
   **Every Week**
   
   - **Review shift schedules** on Discord for any changes and updates

Monthly Tasks
-------------

.. important::
   **Before Month End**
   
   - **Register hours in DTU FUSION** 
   - **Register personal working hours** on SharePoint
   
   **Needs to be done before last team meeting in current month!**

Getting Help & Support
======================

Where to Get Help
-----------------

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Contact
     - Purpose
     - When to Use
   * - **The Team**
     - Support & collaboration
     - During your shift
   * - **Team Lead**
     - Daily questions & priorities
     - Regular guidance
   * - **Discord Channel**
     - Quick team-wide help
     - Immediate assistance
   * - **Knowledge Base**
     - Self-service resources
     - Research & learning