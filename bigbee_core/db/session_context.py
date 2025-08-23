# bigbee_core/db/session_context.py

from contextvars import ContextVar

_session_var: ContextVar = ContextVar("db_session")

def set_session(session):
    _session_var.set(session)

def clear_session():
    _session_var.set(None)

def get_session():
    session = _session_var.get(None)
    if session is None:
        raise RuntimeError("No session set in context")
    return session