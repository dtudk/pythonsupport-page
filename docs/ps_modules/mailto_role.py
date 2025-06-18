
from docutils import nodes
import urllib.parse

def escape_backslash(text:str):
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
    
    if "<" not in text and ">" not in text:
        display = text.strip()
        email = text.strip()

        uri = f"mailto:{email}"
        node = nodes.reference(rawtext, display, refuri=uri, **options)
        return [node], []

    else:
        display, params = text.split("<", 1)
        params, _ = params.rsplit(">", 1)
        parsed_input = params.split("|")

        display = display.strip()

        if len(parsed_input) == 1:
            email = parsed_input[0].strip()
            uri = f"mailto:{email}"
            node = nodes.reference(rawtext, display, refuri=uri, **options)
            return [node], []
            
        elif len(parsed_input) == 3:
            email = parsed_input[0].strip()
            subject = parsed_input[1].strip()
            body = parsed_input[2].strip()
            email = email.strip()

            subject = urllib.parse.quote(subject)
            body = urllib.parse.quote(body)

            uri = f"mailto:{email}?subject={subject}&body={body}"
            node = nodes.reference(rawtext, display, refuri=uri, **options)
            return [node], []
            
        else:
            raise ValueError("The :mailto: role takes none, one or three parameters.")