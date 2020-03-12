import json
import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.main.database.tables import AdminControl, Base, Permission

db = json.loads(os.getenv('database', '{}'))
engine = create_engine(
    f'mysql+mysqldb://{db["username"]}:{db["password"]}@{db["server"]}:3306/{db["database"]}',
    pool_recycle=3600, pool_pre_ping=True)


@contextmanager
def get_session():
    db_session = scoped_session(sessionmaker(
        autocommit=False, autoflush=False, bind=engine))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.query = db_session.query_property()

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


def create_database_defaults(get_session):
    with get_session() as session:
        create_admin_control(session)
        create_roles(session)


def create_admin_control(session):
    if not(len(session.query(AdminControl).all()) > 0):
        controls = [{'name': 'new_users', 'value': True}]
        for control in controls:
            ctrl = AdminControl(name=control['name'], value=control['value'])
            session.add(ctrl)
            session.commit()


def create_roles(session):
    if not(len(session.query(Permission).all()) > 0):
        permissions = ['admin', 'user']
        for permission in permissions:
            perm = Permission(name=permission)
            session.add(perm)
            session.commit()
