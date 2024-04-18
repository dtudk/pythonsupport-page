.. _installation-index:

Installing Python
================================

.. raw:: html

   <head>
    <meta charset="UTF-8">
    <title>Questionnaire</title>
   </head>
   <body>
    <h1>Website Questionnaire</h1>
 <form action="" method="POST" name="pythonsupport-python-Q">
     <label for="question1">Which OS (Operating system) are you using?</label><br>
     <input type="radio" id="question1-windows" name="question1" value="Windows" checked=> Windows<br>
     <input type="radio" id="question1-macos" name="question1" value="MacOS"> MacOS<br>
     <input type="radio" id="question1-linux" name="question1" value="Linux"> Linux<br><br>

     <label for="question2">Do you already have Conda installed?</label><br>
     <input type="radio" id="question2-yes" name="question2" value="withConda"> Yes<br>
     <input type="radio" id="question2-no" name="question2" value="withoutConda"> No<br><br>

     <label for="question3">Type of installation</label><br>
     <input type="radio" id="question3-automated" name="question3" value="Automated" checked="checked" > Automated<br>
     <input type="radio" id="question3-package-managed" name="question3" value="packageManaged"> Package Managed<br>
     <input type="radio" id="question3-fully-manual" name="question3" value="fullyManual"> Fully manual<br><br>

     <label for="question4">Are you a first year student</label><br>
     <input type="radio" id="question4-yes" name="question4" value="firstYear" checked="checked"> Yes<br>
     <input type="radio" id="question4-no" name="question4" value="notFirstYear"> No<br><br>

     <input type="submit" value="Submit">
 </form>

 <script language="Javascript" type="text/javascript">

	function isOperatingSytem(os) {
	// This could be used to pre-check the OS question
	    if (navigator.appVersion.indexOf("Win") != -1) return os == "Windows";
	    if (navigator.appVersion.indexOf("Mac") != -1) return os == "MacOS";
	    if (navigator.appVersion.indexOf("X11") != -1) return os == "Linux";
	    if (navigator.appVersion.indexOf("Linux") != -1) return os == "Linux";
	    return false;
	}

   console.log("Hello World");
     // This script handles form submission and redirection based on answers
     var form = document.forms['pythonsupport-python-Q'];
     form.addEventListener('submit', function(event) {
         console.log("got event");
         event.preventDefault(); // Prevent default form submission

	 // Push answers of questions into this array
	 const questions = new Array();

	 for( let i = 1 ; i <= 4 ; i++ ) {
           console.log("querying q" + i);
	   // From the `form` (defined outside, perhaps it can more elegantly
	   // be fetched from 'event' for clarity.
	   const q = form.elements["question" + i];
	   // grab the value
	   questions.push(q.value);
	   // print-out to the console, for logging purposes
           console.log("q" + i + " = ".concat(questions.slice(-1)));
	}

         // Concatenate the new url
         const redirectUrl = "https://placeholder-url1.com/pathto/website1/" + questions.join("/");
         console.log("after " + redirectUrl);

         if (redirectUrl) {
             window.location.href = redirectUrl; // Redirect if a URL is set
         } else {
             alert("No matching website found based on your answers.");
         }
     });
 </script>

   </body>

..    :maxdepth: 1

..    install-python.rst
..    install-conda.rst
..    install-verify.rst
