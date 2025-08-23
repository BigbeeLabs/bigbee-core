# bigbee_core/api/shared/presenter_result.py
from dataclasses import dataclass, field
from typing import Any, Mapping, Optional, Union, Dict

Body = Union[str, Mapping[str, Any]]

@dataclass(frozen=True, slots=True)
class PresenterResult:
    ok: bool                      # True => success (HTML), False => error (JSON)
    status: int                   # HTTP status code
    body: Body                    # HTML string or JSON-like mapping
    headers: Mapping[str, str] = field(default_factory=dict)  # optional hints

    def is_ok(self) -> bool:
        return self.ok

    @property
    def is_html(self) -> bool:
        return isinstance(self.body, str)

    @property
    def is_json(self) -> bool:
        return not self.is_html

    @property
    def body_html(self) -> Optional[str]:
        return self.body if isinstance(self.body, str) else None

    @property
    def body_json(self) -> Optional[Dict[str, Any]]:
        return dict(self.body) if isinstance(self.body, Mapping) else None

    @classmethod
    def success(cls, body: str, status: int = 200, headers: Optional[Mapping[str, str]] = None) -> "PresenterResult":
        return cls(ok=True, status=status, body=body, headers=dict(headers or {}))

    @classmethod
    def failure(cls, body: Mapping[str, Any], status: int = 422, headers: Optional[Mapping[str, str]] = None) -> "PresenterResult":
        return cls(ok=False, status=status, body=body, headers=dict(headers or {}))
