import json
import os
from contextlib import contextmanager

import pytest
from flask import template_rendered
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main.database import create_tables
from app.main.database.tables import Base
from chat import create_app

###########################
# Test Database Credentials
###########################

db = json.loads(os.getenv('test_database', '{}'))
port = int(os.getenv('port', '3306'))
engine = create_engine(
    f'mysql+mysqldb://{db["username"]}:{db["password"]}@{db["server"]}:{port}/{db["database"]}')
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
            session.commit()
        except BaseException:
            session.rollback()
            raise
        finally:
            session.close()
    yield get_session
    transaction.rollback()
    session.close()


@pytest.fixture(scope='function')
def client(session):
    from app import create_app
    app = create_app(session)
    with app.app_context():
        yield app.test_client()


def pytest_sessionfinish(session, exitstatus):
    Base.metadata.drop_all(bind=engine)
