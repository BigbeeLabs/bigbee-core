# bigbee_core/session/bridge.py

_session_getter = None

def register_session(session_getter):
    global _session_getter
    _session_getter = session_getter

def get_session():
    if _session_getter is None:
        raise RuntimeError("Session getter not registered")
    return _session_getter()