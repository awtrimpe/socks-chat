import json
import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.main.database.tables import Base

db = json.loads(os.getenv('database', '{}'))
engine = create_engine(
    f'mysql+mysqldb://{db["username"]}:{db["password"]}@{db["server"]}:3306/{db["database"]}')
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))
Session = sessionmaker(bind=engine)
Base.query = db_session.query_property()


@contextmanager
def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except BaseException:
        session.rollback()
        raise
    finally:
        session.close()


def create_tables(engine):
    Base.metadata.create_all(engine)
