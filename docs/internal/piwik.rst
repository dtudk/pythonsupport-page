:nosearch:

.. _piwik-documentation:

Piwik
----

This page contains information on how to use Piwik. The parenthesis of the titles: "()" indicate where to find the topics of the section in piwik.

Helpful links
====

* `Piwik PRO Help Center <https://help.piwik.pro>`_
* `Piwik PRO YouTube Tutorial <https://www.youtube.com/watch?v=O_its-ChPTg&list=PLgjjMVHirGE_7ET0nb7ZUv7wN2P4sTRpE>`_


Segments (Analytics)
====
Segments are filters to be applied globally when viewing a dashboard of widgets.

Current segments:

#.
    **"Denmark"**: which filters IP-addresses from denmark. This is useful in accessing how well the website performs on DTU students.

Dashboards (Analytics)
====

Dashboards are a collection of widgets that presents a data collected over a period. This period can be set in the top right corner.

Current dashboards:

#. 
    **Weekly review**: Shows number of unique visitors, mean session time, mean time on install page, number of automated install errors, page views.


Widgets (Analytics)
====

Widgets are self contained graphs/tables/counters that display information about the site.
On creation of a widget you are presented with a list of:

* 
    dimensions (color=green, values that you can filter against), 
* 
    metrics (color=blue, values you can display).



Variables (Tag manager)
====

Variables can be used for setting conditions for when triggers are supposed to fire. Variables can get information from the URL, Cookies, DOM elements, and more.


Triggers (Tag manager)
====

When specific conditions are met a trigger can be fired. The code that a trigger executes is called a Tag. 
For example a trigger can executed when:

* 
    A user scrolls past a specific percentage down the screen
* 
    A user clicks on a specific element/button
* 
    A user visits a specific URL with query elements

When creating a trigger the following fields are required:

#. 
    Trigger name
#. 
    Condition on when the trigger is executed (can use variables)
#. 
    How many times a trigger can be called during a visit


Tags (Tag manager)
====

Tags are small self contained javascript functions that runs as a part of a trigger.





Current setup
====

We are currently tracking:

*
    User click heatmap

*
    User scroll heatmap

*
    Install errors from url ?error={{error}}

*
    How many clicks the "Download python" and "See tutorials" are getting

*
    How many clicks the "Reach us" sections are getting

*





