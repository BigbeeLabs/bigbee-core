# bigbee_core/web/components/text_input/dto.py
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Dto:
    id: str
    name: str
    label: str
    value: Optional[str] = ""
    input_type: str = "text"          # ← add
    placeholder: Optional[str] = None
    required: bool = False
    disabled: bool = False
    readonly: bool = False
    autocomplete: Optional[str] = None
    inputmode: Optional[str] = None
    pattern: Optional[str] = None
    maxlength: Optional[int] = None
    minlength: Optional[int] = None
    help_text: Optional[str] = None
    error_text: Optional[str] = None
    group_classes: Optional[str] = None
    input_classes: Optional[str] = None
    label_classes: Optional[str] = None
    initializers: Optional[str] = None
