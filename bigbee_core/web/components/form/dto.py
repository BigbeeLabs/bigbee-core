# bigbee_core/web/components/form/dto.py

from dataclasses import dataclass

@dataclass(frozen=True)
class Dto:
    csrf_token: str  # required
    remote: str
    method: str = "GET"
    action: str = "/"
    buttons: str = "form-dto-buttons"
    form_fields: str = "form-dto-default-form-fields"
    initializers: str = ""

