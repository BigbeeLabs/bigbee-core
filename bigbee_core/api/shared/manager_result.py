# bigbee_core/api/shared/manager_result.py
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from .enums.status_codes import StatusCode

@dataclass(frozen=True, slots=True)
class ManagerResult:
    data: Any = None
    error: Optional[str] = None
    status_code: int = StatusCode.OK

    # add structured fields
    errors: Optional[Dict[str, List[str]]] = None
    details: Optional[str] = None
    meta: Dict[str, Any] = field(default_factory=dict)

    def is_ok(self) -> bool:
        return self.error is None

    @property
    def errors_dict(self) -> Optional[Dict[str, List[str]]]:
        return dict(self.errors) if self.errors is not None else None

    @classmethod
    def ok(cls, data=None, status_code: int = StatusCode.OK, **extras):
        return cls(data=data, error=None, status_code=status_code, **extras)

    @classmethod
    def fail(cls, error: str, status_code: int = StatusCode.INTERNAL_ERROR, **extras):
        return cls(data=None, error=error, status_code=status_code, **extras)

    @classmethod
    def no_content(cls):
        return cls(data=None, error=None, status_code=StatusCode.NO_CONTENT)
