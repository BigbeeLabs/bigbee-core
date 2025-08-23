from markupsafe import Markup

def html(s: str) -> Markup:
    # Mark a trusted HTML fragment as safe for templates.
    return Markup(s)