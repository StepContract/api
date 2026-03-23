from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=settings.ECHO)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

Base = declarative_base()


def get_db():
    try:
        yield db
    except:
        db.rollback()
    finally:
        db.close()
