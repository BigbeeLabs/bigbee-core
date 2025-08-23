# web/components/form/submit_button/dto.py
from dataclasses import dataclass
@dataclass(frozen=True)
class Dto:
    label: str = "Submit"
    class_: str = "btn"
    name: str | None = None      # e.g., "action"
    value: str | None = None     # e.g., "sign_in"
    form: str | None = None      # optional external form id
    disabled: bool = False
    formmethod: str | None = None        # overrides form method
    formaction: str | None = None        # overrides form action
    formenctype: str | None = None
    formnovalidate: bool = False
    formtarget: str | None = None
