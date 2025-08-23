# bigbee_core/db/engine.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

ENV = os.getenv("ENV")  # Don't default to 'dev' here
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL not set — set it in environment before importing bigbee_core.db.engine")

engine = create_engine(DATABASE_URL)
SessionFactory = sessionmaker(bind=engine)