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
    <h1></h1>
    <form id="questionnaireForm">

        <label for="question1">Are you a first year student</label><br>
        <input type="radio" name="studentYear" value="Yes" checked="checked"> Yes<br>
        <input type="radio" name="studentYear" value="No"> No<br><br>    

        <label for="question2">Do you already have Conda installed?</label><br>
        <input type="radio" name="conda" value="Yes"> Yes<br>
        <input type="radio" name="conda" value="No" checked="checked"> No<br><br>    

        <label for="question3">Which OS (Operating system) are you using?</label><br>
        <input type="radio" name="os" value="Windows"> Windows<br>
        <input type="radio" name="os" value="MacOS"> MacOS<br>
        <input type="radio" name="os" value="Linux"> Linux<br><br>

        <label for="question4">Type of installation</label><br>
        <input type="radio" name="installationType" value="Automated" checked="checked"> Automated<br>
        <input type="radio" name="installationType" value="Package Managed"> Package Managed<br>
        <input type="radio" name="installationType" value="Fully Manual"> Fully manual<br><br>



        <input type="submit" value="Submit">
    </form>

    <script>
    document.getElementById('questionnaireForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting via the browser

        var os = document.querySelector('input[name="os"]:checked').value;
        var conda = document.querySelector('input[name="conda"]:checked').value;
        var installationType = document.querySelector('input[name="installationType"]:checked').value;
        var studentYear = document.querySelector('input[name="studentYear"]:checked').value;

        var destinationFile = "index.html"; // Default redirection file

        // Define redirection logic
    if (os === "Windows" && installationType === "Automated") {
        destinationFile = "windows/automated.html";
    } else if (os === "Windows" && installationType === "Package Managed") {
        destinationFile = "windows/package-managed.html";
    } else if (os === "Windows" && installationType === "Fully Manual") {
        destinationFile = "windows/fully-manual.html";
    } else if (os === "MacOS" && installationType === "Automated") {
        destinationFile = "macos/automated.html";
    } else if (os === "MacOS" && installationType === "Package Managed") {
        destinationFile = "macos/package-managed.html";
    } else if (os === "MacOS" && installationType === "Fully Manual") {
        destinationFile = "macos/fully-manual.html";
    } else if (os === "Linux" && installationType === "Automated") {
        destinationFile = "linux/automated.html";
    } else if (os === "Linux" && installationType === "Package Managed") {
        destinationFile = "linux/package-managed.html";
    } else if (os === "Linux" && installationType === "Fully Manual") {
        destinationFile = "linux/fully-manual.html";
    }


        // Add more conditions as needed

        // Redirect to the appropriate .rst file
        window.location.href = destinationFile;
    });
    </script>

    </body>
    </html>

