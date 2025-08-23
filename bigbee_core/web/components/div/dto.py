# bigbee_core/web/components/div/dto.py
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Dto:
    content: str = ""                 # inner HTML/text
    id: Optional[str] = None
    classes: Optional[str] = None
    role: Optional[str] = None
    aria_label: Optional[str] = None
    initializers: Optional[str] = None  # space-separated