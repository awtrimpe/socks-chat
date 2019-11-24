import json
import os
from contextlib import contextmanager

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main.database import create_tables
from app.main.database.tables import Base
from chat import create_app

###########################
# Test Database Credentials
###########################

db = json.loads(os.getenv('test_database', '{}'))
engine = create_engine(
    f'mysql+mysqldb://{db["username"]}:{db["password"]}@{db["server"]}:3306/{db["database"]}')
Session = sessionmaker()


@pytest.fixture(scope='module')
def connection():
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture(scope='function')
def session(connection):
    create_tables(engine)
    transaction = connection.begin()
    session = Session(bind=connection)

    @contextmanager
    def get_session() -> Session:
        try:
            yield session
        except BaseException:
            session.rollback()
            raise
        finally:
            session.close()
    yield get_session
    transaction.rollback()


@pytest.fixture(scope='function')
def client(session):
    from app import create_app
    yield create_app(session).test_client()


def pytest_sessionfinish(session, exitstatus):
    Base.metadata.drop_all(bind=engine)
