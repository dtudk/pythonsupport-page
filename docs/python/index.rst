.. _installation-index:

Installing Python
================================

.. raw:: html

   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>Questionnaire</title>
   </head>
   <body>
       <h1>Website Questionnaire</h1>
       <form action="" method="post">
           <label for="question1">Which OS (Operating system) are you using?</label><br>
           <input type="radio" id="question1" name="question1" value="Windows"> Windows<br>
           <input type="radio" id="question1" name="question1" value="MacOS"> MacOS<br>
           <input type="radio" id="question1" name="question1" value="Linux"> Linux<br><br>

           <label for="question2">Do you already have Conda installed?</label><br>
           <input type="radio" id="question2" name="question2" value="Yes"> Yes<br>
           <input type="radio" id="question2" name="question2" value="No"> No<br><br>

           <label for="question3">Type of installation</label><br>
           <input type="radio" id="question3" name="question3" value="Automated" checked="checked" > Automated<br>
           <input type="radio" id="question3" name="question3" value="Package Managed"> Package Managed<br>
           <input type="radio" id="question3" name="question3" value="Fully manual"> Fully manual<br><br>

           <label for="question4">Are you a first year student</label><br>
           <input type="radio" id="question4" name="question4" value="Yes" checked="checked"> Yes<br>
           <input type="radio" id="question4" name="question4" value="No"> No<br><br>

           <input type="submit" value="Submit">
       </form>

       <script>
           // This script handles form submission and redirection based on answers
           const form = document.querySelector('form');
           form.addEventListener('submit', function(event) {
               event.preventDefault(); // Prevent default form submission

               const question1 = document.querySelector('input[name="question1"]:checked').value;
               const question2 = document.querySelector('input[name="question2"]:checked').value;
               const question3 = document.querySelector('input[name="question3"]:checked').value;
               const question4 = document.querySelector('input[name="question4"]:checked').value;

               let redirectUrl;

               if (question1 === "shopping") {
                   if (question2 === "simple") {
                       redirectUrl = "https://www.amazon.com"; // Replace with a simple shopping site
                   } else {
                       redirectUrl = "https://www.etsy.com"; // Replace with a complex shopping site
                   }
               } else if (question1 === "news") {
                   if (question3 === "english") {
                       redirectUrl = "https://www.bbc.com/news"; // Replace with English news site
                   } else {
                       redirectUrl = "https://www.google.com/search?q=news" // Generic news search
                   }
               } else if (question1 === "social") {
                   if (question2 === "simple") {
                       redirectUrl = "https://twitter.com"; // Replace with a simple social media site
                   } else {
                       redirectUrl = "https://www.facebook.com"; // Replace with a complex social media site
                   }
               }

               if (redirectUrl) {
                   window.location.href = redirectUrl; // Redirect if a url is set
               } else {
                   alert("No matching website found based on your answers.");
               }
           });
       </script>
   </body>
   </html>






..    :maxdepth: 1

..    install-python.rst
..    install-conda.rst
..    install-verify.rst
