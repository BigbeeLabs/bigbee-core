# bigbee_core/services/shared/service_result.py
from dataclasses import dataclass, field, replace
from typing import Any, Dict, List, Optional, TypeVar, Generic, Mapping
from types import MappingProxyType

T = TypeVar("T")

def _readonly_meta(meta: Optional[Dict[str, Any]]) -> Mapping[str, Any]:
    return MappingProxyType({} if meta is None else dict(meta))

@dataclass(frozen=True, slots=True)
class ServiceResult(Generic[T]):
    success: bool
    value: Optional[T] = None
    error: Optional[str] = None

    status_code: Optional[int] = None
    errors: Optional[Mapping[str, List[str]]] = None   # read-only mapping
    details: Optional[str] = None
    meta: Mapping[str, Any] = field(default_factory=lambda: MappingProxyType({}))

    # Convenience: JSON-safe view of errors (unwrap mappingproxy)
    @property
    def errors_dict(self) -> Optional[Dict[str, List[str]]]:
        return dict(self.errors) if self.errors is not None else None

    # Convenience aliases
    @property
    def failed(self) -> bool:
        return not self.success

    @property
    def failure(self) -> bool:
        return not self.success

    # ---------- factories ----------
    @classmethod
    def ok(
        cls,
        value: Optional[T] = None,
        *,
        status_code: Optional[int] = None,
        details: Optional[str] = None,
        meta: Optional[Dict[str, Any]] = None,
    ) -> "ServiceResult[T]":
        return cls(
            success=True,
            value=value,
            status_code=status_code,
            details=details,
            meta=_readonly_meta(meta),
        )

    @classmethod
    def fail(
        cls,
        error: str,
        *,
        status_code: Optional[int] = None,
        errors: Optional[Dict[str, List[str]]] = None,
        details: Optional[str] = None,
        meta: Optional[Dict[str, Any]] = None,
    ) -> "ServiceResult[None]":
        return cls(
            success=False,
            error=error,
            status_code=status_code,
            errors=MappingProxyType(errors or {}),
            details=details,
            meta=_readonly_meta(meta),
        )

    # Immutable "update"
    def evolve(self, **changes) -> "ServiceResult[T]":
        return replace(self, **changes)
