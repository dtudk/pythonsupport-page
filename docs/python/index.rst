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
        <input type="radio" id="question2-yes" name="question2" value="Yes"> Yes<br>
        <input type="radio" id="question2-no" name="question2" value="No"> No<br><br>

        <label for="question3">Type of installation</label><br>
        <input type="radio" id="question3-automated" name="question3" value="Automated" checked="checked" > Automated<br>
        <input type="radio" id="question3-package-managed" name="question3" value="Package Managed"> Package Managed<br>
        <input type="radio" id="question3-fully-manual" name="question3" value="Fully manual"> Fully manual<br><br>

        <label for="question4">Are you a first year student</label><br>
        <input type="radio" id="question4-yes" name="question4" value="Yes" checked="checked"> Yes<br>
        <input type="radio" id="question4-no" name="question4" value="No"> No<br><br>

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

            if (question1 === "Windows") {
                if (question2 === "Yes") {
                    if (question3 === "Automated") {
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url1.com";
                        } else {
                            redirectUrl = "https://placeholder-url2.com";
                        }
                    } else if (question3 === "Package Managed") {
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url3.com";
                        } else {
                            redirectUrl = "https://placeholder-url4.com";
                        }
                    } else { // Fully manual
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url5.com";
                        } else {
                            redirectUrl = "https://placeholder-url6.com";
                        }
                    }
                } else { // No Conda installed
                    if (question3 === "Automated") {
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url7.com";
                        } else {
                            redirectUrl = "https://placeholder-url8.com";
                        }
                    } else if (question3 === "Package Managed") {
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url9.com";
                        } else {
                            redirectUrl = "https://placeholder-url10.com";
                        }
                    } else { // Fully manual
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url11.com";
                        } else {
                            redirectUrl = "https://placeholder-url12.com";
                        }
                    }
                }
            } else if (question1 === "MacOS") {
                if (question2 === "Yes") {
                    if (question3 === "Automated") {
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url13.com";
                        } else {
                            redirectUrl = "https://placeholder-url14.com";
                        }
                    } else if (question3 === "Package Managed") {
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url15.com";
                        } else {
                            redirectUrl = "https://placeholder-url16.com";
                        }
                    } else { // Fully manual
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url17.com";
                        } else {
                            redirectUrl = "https://placeholder-url18.com";
                        }
                    }
                } else { // No Conda installed
                    if (question3 === "Automated") {
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url19.com";
                        } else {
                            redirectUrl = "https://placeholder-url20.com";
                        }
                    } else if (question3 === "Package Managed") {
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url21.com";
                        } else {
                            redirectUrl = "https://placeholder-url22.com";
                        }
                    } else { // Fully manual
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url23.com";
                        } else {
                            redirectUrl = "https://placeholder-url24.com";
                        }
                    }
                }
            } else if (question1 === "Linux") {
                if (question2 === "Yes") {
                    if (question3 === "Automated") {
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url25.com";
                        } else {
                            redirectUrl = "https://placeholder-url26.com";
                        }
                    } else if (question3 === "Package Managed") {
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url27.com";
                        } else {
                            redirectUrl = "https://placeholder-url28.com";
                        }
                    } else { // Fully manual
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url29.com";
                        } else {
                            redirectUrl = "https://placeholder-url30.com";
                        }
                    }
                } else { // No Conda installed
                    if (question3 === "Automated") {
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url31.com";
                        } else {
                            redirectUrl = "https://placeholder-url32.com";
                        }
                    } else if (question3 === "Package Managed") {
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url33.com";
                        } else {
                            redirectUrl = "https://placeholder-url34.com";
                        }
                    } else { // Fully manual
                        if (question4 === "Yes") {
                            redirectUrl = "https://placeholder-url35.com";
                        } else {
                            redirectUrl = "https://placeholder-url36.com";
                        }
                    }
                }
            }

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
