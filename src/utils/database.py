from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from config.settings import settings
import logging

logger = logging.getLogger(__name__)

engine = create_engine(
    settings.DATABASE_URL,
    pool_size=10,
    max_overflow=5,
    pool_pre_ping=True,  # Connection health check before each use
    pool_recycle=1800,   # Recycle connections every 30 mins
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_session():
    """Context manager for safe session handling."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except OperationalError as e:
        session.rollback()
        logger.error(f"DB Operational Error: {e}")
        raise
    except Exception as e:
        session.rollback()
        logger.error(f"DB Session Error: {e}")
        raise
    finally:
        session.close()
