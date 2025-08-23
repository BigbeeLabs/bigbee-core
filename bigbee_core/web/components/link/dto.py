# bigbee_core/web/components/link/dto.py

from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Dto:
    href: str
    label: str
    remote: str
    id: Optional[str] = None
    classes: Optional[str] = None
    target: Optional[str] = None
    rel: Optional[str] = None
    download: Optional[str] = None
    aria_label: Optional[str] = None
    initializers: Optional[str] = None  # NEW: space-separated initializer names