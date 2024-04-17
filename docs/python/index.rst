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
        <input type="radio" id="question1-windows" name="question1" value="Windows"> Windows<br>
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

    <script>

      console.log("Hello World");
        // This script handles form submission and redirection based on answers
        const form = document.querySelector('form');
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            const question1 = document.querySelector('input[name="question1"]:checked').value;
            const question2 = document.querySelector('input[name="question2"]:checked').value;
            const question3 = document.querySelector('input[name="question3"]:checked').value;
            const question4 = document.querySelector('input[name="question4"]:checked').value;

            let redirectUrl;

            redirectUrl = "https://placeholder-url1.com/pathto/website1/" + question1 + "/" + question2 + "/" + question3 + "/" + question4 + "/";

            if (redirectUrl) {
                window.location.href = redirectUrl; // Redirect if a URL is set
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
