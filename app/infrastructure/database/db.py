from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session
from app.infrastructure.database.database_manager import DatabaseManager

Base = declarative_base()


def get_db():
    db: Session = DatabaseManager().create_session()
    try:
        yield db
    finally:
        db.close()
