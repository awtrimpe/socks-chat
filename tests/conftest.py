import json
import os
from contextlib import contextmanager

import pytest
from flask import template_rendered
from flask_login import LoginManager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main.database import create_database_defaults, create_tables
from app.main.database.tables import Base, User

###########################
# Test Database Credentials
###########################

db = json.loads(os.getenv('test_database', '{}'))
port = int(os.getenv('port', '3306'))
engine = create_engine(
    f'mysql+mysqldb://{db["username"]}:{db["password"]}@{db["server"]}:{port}/{db["database"]}')
Session = sessionmaker()
login_manager = LoginManager()


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
    create_database_defaults(session)
    login_manager.init_app(app)
    with app.app_context():
        yield app.test_client()


@pytest.fixture(autouse=True)
def reset_login_manager():
    @login_manager.request_loader
    def load_user_from_request(request):
        return None


def pytest_sessionfinish(session, exitstatus):
    if os.getenv('drop_tables', 'True') == 'True':
        Base.metadata.drop_all(bind=engine)


def test_with_authenticated_user(session):
    '''
    Overrides the default login_manager.request_loader and essentially sets the
    current_user to the first user in the database
    '''
    @login_manager.request_loader
    def load_user_from_request(request):
        return session.query(User).first()
