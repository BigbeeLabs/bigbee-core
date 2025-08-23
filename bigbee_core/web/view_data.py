from collections.abc import Mapping, Sequence

class ViewData(Mapping):
    def __init__(self, data, sep="."):
        if not isinstance(data, Mapping):
            raise TypeError("View expects a dict-like mapping")
        self._data = data
        self._sep = sep

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

    def _traverse(self, path: str):
        cur = self._data
        parts = path.split(self._sep)
        for p in parts:
            if isinstance(cur, Mapping) and p in cur:
                cur = cur[p]
            elif self._is_seq(cur) and p.isdigit():
                cur = cur[int(p)]
            else:
                raise KeyError(path)
        return cur

    def __getitem__(self, key):
        if key in self._data:                           # exact key
            return self.wrap(self._data[key], self._sep)
        if isinstance(key, str) and self._sep in key:   # dotted path
            return self.wrap(self._traverse(key), self._sep)
        raise KeyError(key)

    def get(self, path, default=None):
        try:
            return self._traverse(path) if isinstance(path, str) else self._data.get(path, default)
        except KeyError:
            return default

    def __getattr__(self, name):                        # attribute access
        try:
            return self[name]
        except KeyError as e:
            raise AttributeError(name) from e

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def to_dict(self):
        return self._data
