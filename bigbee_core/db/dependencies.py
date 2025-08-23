# bigbee_core/db/dependencies.py

from bigbee_core.db.session_context import set_session, clear_session, get_session
from sqlalchemy.orm import Session
from contextlib import contextmanager
from typing import Generator
from bigbee_core.db.engine import SessionFactory  # <- centralized engine/session

@contextmanager
def db_context(session: Session) -> Generator[Session, None, None]:
    set_session(session)
    try:
        yield session
    finally:
        clear_session()

def get_db():
    db = SessionFactory()
    with db_context(db) as session:
        yield session
        db.close()