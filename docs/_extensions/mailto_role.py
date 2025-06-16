
from docutils import nodes
import urllib.parse
import re

# Matches a string with a prefix and a custom tag in angle brackets, extracting:
# - the leading text (non-greedy),
# - the main tag name before the first pipe '|',
# - and optionally, one or more parameters separated by '|'.
# Example matches: "Text<tag>", "Prefix<name|param1|param2>"
pattern = re.compile(r"(.*?)<([^>|]+)(?:\|([^>|]+))(?:\|([^>|]+))*>")

def mailto_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    
    parsed_input = pattern.match(text).groups()
    
    if len(parsed_input) == 1:
        display = parsed_input[0]
        email_part = parsed_input[0]

    if len(parsed_input) == 2:
        display = parsed_input[0]
        email_part = parsed_input[1]

    elif len(parsed_input) == 4:
        display = parsed_input[0]
        email_part = parsed_input[1]
        subject = parsed_input[2]
        body = parsed_input[3]
    
    else:
        raise ValueError("Mailto takes none or one or three options.")

    email = email_part.strip()
    subject = urllib.parse.quote(subject.strip())
    body = urllib.parse.quote(body.strip())
    uri = f"mailto:{email}?subject={subject}&body={body}"

    node = nodes.reference(display, email, refuri=uri, **options)
    return [node], []