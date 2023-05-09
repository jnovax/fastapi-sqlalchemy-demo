from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Film(Base):
    __tablename__ = "films"

    title = Column(String, primary_key=True)
    director = Column(String)
    year = Column(String)


db_connection = "postgresql+psycopg://demo:demo@localhost:5432/demo"
engine = create_engine(db_connection, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

def get_db():
    return Session()

from contextlib import contextmanager

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
