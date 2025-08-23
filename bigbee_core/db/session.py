# bigbee_core/db/session.py

from bigbee_core.db.engine import SessionFactory

def get_db_session():
    return SessionFactory()