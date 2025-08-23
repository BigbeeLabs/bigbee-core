# bigbee_core/utils/map_navigator.py

# Usage:
#     from bigbee_core.utils.map_navigator import MapNavigator

#     data = {
#         "person": {"given_name": "Jude", "family_name": "Law"},
#         "emails": [{"address": "a@x"}, {"address": "b@x"}],
#     }

#     ctx = MapNavigator(data)

#     # Attribute chain
#     ctx.person.given_name            # -> "Jude"

#     # Dotted path indexing
#     ctx["person.given_name"]         # -> "Jude"

#     # Safe get (returns None or provided default if missing)
#     ctx.get("emails.0.address")      # -> "a@x"
#     ctx.get("person.middle_name", default="")  # -> ""

#     # Ruby-style dig
#     ctx.dig("emails", 1, "address")  # -> "b@x"

from collections.abc import Mapping, Sequence
from typing import Any

class MapNavigator(Mapping):
    __slots__ = ("_data", "_sep")

    def __init__(self, data: Mapping, sep: str = "."):
        if not isinstance(data, Mapping):
            raise TypeError("MapNavigator expects a dict-like mapping")
        object.__setattr__(self, "_data", data)
        object.__setattr__(self, "_sep", sep)

    @staticmethod
    def _is_seq(x):
        return isinstance(x, Sequence) and not isinstance(x, (str, bytes, bytearray))

    @classmethod
    def wrap(cls, obj, sep="."):
        if isinstance(obj, Mapping):
            return cls(obj, sep=sep)
        if cls._is_seq(obj):
            return [cls.wrap(o, sep=sep) for o in obj]
        return obj

    def _index(self, cur: Any, key: Any) -> Any:
        if isinstance(cur, Mapping):
            return cur[key]
        if self._is_seq(cur):
            # allow 0 / "0" etc.
            if isinstance(key, str):
                try:
                    key = int(key)
                except ValueError:
                    raise KeyError(key)
            return cur[key]
        raise KeyError(key)

    def _traverse(self, path: str):
        cur: Any = self._data
        for p in path.split(self._sep):
            cur = self._index(cur, p)
        return cur

    def __getitem__(self, key):
        if isinstance(key, str) and key in self._data:        # exact key
            return self.wrap(self._data[key], self._sep)
        if isinstance(key, str) and self._sep in key:         # dotted path
            return self.wrap(self._traverse(key), self._sep)
        # fall back: direct key (may raise KeyError)
        return self.wrap(self._data[key], self._sep)

    def get(self, path, default=None):
        try:
            if isinstance(path, str) and self._sep in path:
                return self.wrap(self._traverse(path), self._sep)
            return self.wrap(self._data.get(path, default), self._sep) if isinstance(path, str) else default
        except KeyError:
            return default

    def dig(self, *keys, default=None):
        cur: Any = self._data
        for k in keys:
            try:
                cur = self._index(cur, k)
            except Exception:
                return default
        return self.wrap(cur, self._sep)

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError as e:
            raise AttributeError(name) from e

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"MapNavigator({self._data!r})"

    # read-only
    def __setattr__(self, k, v):
        if k.startswith("_"):
            return object.__setattr__(self, k, v)
        raise TypeError("MapNavigator is read-only")

    def to_dict(self):
        return self._data
