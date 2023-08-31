/*
This will force all external links to open in new tabs.
*/
$(document).ready(function () {
   $('a[href^="http://"], a[href^="https://"]').not('a[class*=internal]').attr('target', '_blank');
});
