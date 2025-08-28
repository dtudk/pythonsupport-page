
from docutils import nodes
import urllib.parse

def escape_backslash(text: str):
    return text.replace("\n", "\x00n")

def mailto_role(name, rawtext, text: str, lineno, inliner, options={}, content=[]):
    """
    This function implements a mailto role with the following syntaxes:

    1.
        :mailto:`pythonsupport@dtu.dk`
    2.
        :mailto:`mail <pythonsupport@dtu.dk>`
    3.
        :mailto:`mail <pythonsupport@dtu.dk|subject|body>`

    Newlines in subject and body are formatted with \\n
    """

    # Needed since sphinx sends escaped backslashes
    text = text.replace("\x00n", "\n")

    # Split into subject, body
    display_email, *subject_body = text.split("|")

    # Split text into display and email
    display, *email = display_email.strip().split("<")
    display = display.strip()

    assert len(email) <= 1, "Email specification is longer than 1!"
    if len(email) == 0:
        email = display
    else:
        email = email[0].strip().strip(">")

    subject_body = list(map(urllib.parse.quote, subject_body))
    assert len(subject_body) <= 2, "Subject+body specification can maximally be 2 long!"

    if len(subject_body) == 1:
        subject = subject_body[0]
        uri = f"mailto:{email}?subject={subject}"

    elif len(subject_body) == 2:
        subject, body = subject_body
        uri = f"mailto:{email}?subject={subject}&body={body}"

    else:
        uri = f"mailto:{email}"

    node = nodes.reference(rawtext, display, refuri=uri, **options)

    return [node], []
