# bigbee_core/web/components/form/template_data.py
from dataclasses import dataclass

@dataclass(frozen=True)
class FormTemplateData:
    csrf_token: str
    remote: str
    method: str = "GET"
    action: str = "/"
    buttons: str = "dto-buttons"
    form_fields: str = "form-dto-form_fields"
    initializers: str = ""
