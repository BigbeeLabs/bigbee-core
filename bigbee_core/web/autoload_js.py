# bigbee_core/web/autoload_js.py
from pathlib import Path

def autoload_js(root_dir: Path, url_prefix: str, pattern: str = "*.js") -> list[str]:

    #===========================================================================
    #  Return URLs for all JS files under root_dir, matching pattern,
    #  with ?v=mtime cache-busting. Caller must ensure root_dir is mounted
    #  in FastAPI at url_prefix.
    #===========================================================================

    if not root_dir.exists():
        return []

    urls: list[str] = []
    for path in sorted(root_dir.rglob(pattern)):
        rel = path.relative_to(root_dir).as_posix()
        v = int(path.stat().st_mtime)  # cache-busting by file mtime
        urls.append(f"{url_prefix.rstrip('/')}/{rel}?v={v}")

    return urls
