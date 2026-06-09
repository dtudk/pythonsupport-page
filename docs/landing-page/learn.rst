:orphan:
:html_theme.sidebar_secondary.remove: true
:title: DTU Python Installation Support

.. meta::
   :description: DTU Python Installation Support landing page for Learn
   :keywords: DTU, Learn, Python, installation, support, VS Code, conda, terminal

Welcome to DTU Python Installation Support
==========================================

We help DTU students get a working Python setup. You can use our
installation guides to install Python yourself, visit us or reach us on
Discord if your current installation needs fixing, and use our tutorials
when you want help with VS Code, conda environments, the terminal, and
other tools used in Python courses.

Here we can help you with:
--------------------------

.. grid:: 1 1 1 1
   :gutter: 1
   :class-container: learn-landing-list

   .. grid-item-card:: Fixing your current Python installation
      :link: ../index.html#reach-us
      :link-type: url
      :class-card: learn-landing-card

      Reach DTU Python Support if your setup is broken, confusing, or course software is not working.

   .. grid-item-card:: Installing Python on your computer
      :link: ../install/python.html
      :link-type: url
      :class-card: learn-landing-card

      Go directly to the recommended installation guide for your operating system.

   .. grid-item-card:: Video tutorials and help with VS Code
      :link: ../learn-more/vscode/index.html#learn-more-vscode
      :link-type: url
      :class-card: learn-landing-card

      Learn how to write Python scripts, use notebooks, and select the right Python environment.

   .. grid-item-card:: Video tutorials and help with conda environments
      :link: ../learn-more/packages-and-environments/index.html#packages-and-environments
      :link-type: url
      :class-card: learn-landing-card

      Understand packages, environments, and how to keep course setups separate.

   .. grid-item-card:: Introductory video tutorials to the terminal
      :link: ../learn-more/terminal.html#learn-more-terminal
      :link-type: url
      :class-card: learn-landing-card

      Get comfortable with the command line commands used in Python courses and installation guides.

.. raw:: html

   <style>
     .prev-next-footer {
       display: none;
     }

     .bd-article-container {
       max-width: 1120px;
     }

     .learn-landing-list {
       margin-top: 0.75rem;
       --learn-badge-center: 5%;
       --learn-badge-size: 2.6rem;
       --learn-card-height: 7.2rem;
       --learn-icon-inset: 3%;
       --learn-text-start: 11%;
     }

     .learn-landing-list .sd-card.learn-landing-card {
       counter-increment: learn-landing-card;
       display: grid;
       grid-template-columns: minmax(0, 1fr);
       align-items: center;
       height: var(--learn-card-height);
       padding: 1rem 7% 1rem var(--learn-text-start);
       border-radius: 8px;
       position: relative;
       transition: border-color 160ms ease, box-shadow 160ms ease, transform 160ms ease;
     }

     .learn-landing-list .sd-card.learn-landing-card > .sd-stretched-link {
       grid-column: 1 / -1;
       grid-row: 1;
     }

     .learn-landing-list .sd-row {
       counter-reset: learn-landing-card;
     }

     .learn-landing-list .sd-card.learn-landing-card::before {
       content: counter(learn-landing-card);
       display: inline-grid;
       place-items: center;
       position: absolute;
       top: 50%;
       left: var(--learn-badge-center);
       transform: translate(-50%, -50%);
       width: var(--learn-badge-size);
       height: var(--learn-badge-size);
       border: 2px solid var(--dtu-red);
       border-radius: 8px;
       color: var(--dtu-red);
       font-size: 1.05rem;
       font-weight: 800;
       line-height: 1;
     }

     .learn-landing-list .sd-card.learn-landing-card::after {
       display: inline-grid;
       place-items: center;
       position: absolute;
       top: 50%;
       right: var(--learn-icon-inset);
       transform: translateY(-50%);
       color: var(--dtu-blue);
       font-family: "Font Awesome 6 Free";
       font-size: 1.35rem;
       font-weight: 900;
       line-height: 1;
     }

     .learn-landing-list .sd-col:nth-child(1) .sd-card.learn-landing-card::after {
       content: "\f061";
     }

     .learn-landing-list .sd-col:nth-child(2) .sd-card.learn-landing-card::after {
       content: "\f019";
     }

     .learn-landing-list .sd-col:nth-child(3) .sd-card.learn-landing-card::after {
       content: "\f121";
     }

     .learn-landing-list .sd-col:nth-child(4) .sd-card.learn-landing-card::after {
       content: "\f5fd";
     }

     .learn-landing-list .sd-col:nth-child(5) .sd-card.learn-landing-card::after {
       content: "\f120";
     }

     .learn-landing-list .sd-card.learn-landing-card:hover {
       border-color: var(--dtu-red) !important;
       box-shadow: 0 10px 26px rgba(0, 0, 0, 0.08);
       transform: translateY(-1px);
     }

     .learn-landing-list .sd-card-body {
       display: grid;
       grid-template-rows: 1.45rem 2.6rem;
       align-content: start;
       align-self: center;
       gap: 0.45rem;
       height: 4.5rem;
       min-width: 0;
       padding: 0;
     }

     .learn-landing-list .sd-card-title {
       font-size: 1.06rem;
       line-height: 1.25;
       margin-bottom: 0;
     }

     .learn-landing-list .sd-card-text {
       font-size: 0.95rem;
       line-height: 1.35;
       margin: 0;
     }

     @media (max-width: 600px) {
       .learn-landing-list .sd-card.learn-landing-card {
         grid-template-columns: 3.25rem minmax(0, 1fr);
         gap: 0.85rem;
         height: auto;
         min-height: var(--learn-card-height);
         padding: 1rem;
       }

       .learn-landing-list .sd-card.learn-landing-card::before {
         position: static;
         transform: none;
         width: 2.35rem;
         height: 2.35rem;
         font-size: 1rem;
       }

       .learn-landing-list .sd-card-body {
         height: auto;
         grid-template-rows: auto auto;
         align-content: center;
       }

       .learn-landing-list .sd-card.learn-landing-card::after {
         display: none;
       }
     }
   </style>
