from flask import request
from flask import session as f_session
from flask_login import current_user, login_user

from app.main.events import joined, left, text, typing
from app.main.users import register_user
from chat import app

# TODO: Use test socketio client


def describe_joined():
    def test_joined_user(session):
        with app.app_context():
            with app.test_request_context():
                with session() as session_s:
                    new_user = register_user(
                        session_s, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
                    session_s.add(new_user)
                    session_s.commit()
                    login_user(new_user)
                    request.sid = 10
                    request.namespace = 'Namespace'
                    f_session['name'] = 'Alex'
                    joined('A user joined')
                    import pdb
                    pdb.set_trace()
                    assert True


def describe_text():
    def test_user_message(session):
        with app.app_context():
            with app.test_request_context():
                with session() as session_s:
                    new_user = register_user(
                        session_s, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
                    session_s.add(new_user)
                    session_s.commit()
                    login_user(new_user)
                    request.sid = 10
                    request.namespace = 'Namespace'
                    f_session['name'] = 'Alex'
                    text({'msg': 'A user joined'})


def describe_left():
    def test_user_left(session):
        with app.app_context():
            with app.test_request_context():
                with session() as session_s:
                    new_user = register_user(
                        session_s, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
                    session_s.add(new_user)
                    session_s.commit()
                    login_user(new_user)
                    request.sid = 10
                    request.namespace = 'Namespace'
                    f_session['name'] = 'Alex'
                    left('A user joined')


def describe_typing():
    def test_user_typing(session):
        with app.app_context():
            with app.test_request_context():
                with session() as session_s:
                    new_user = register_user(
                        session_s, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
                    session_s.add(new_user)
                    session_s.commit()
                    login_user(new_user)
                    request.sid = 10
                    request.namespace = 'Namespace'
                    f_session['name'] = 'Alex'
                    typing('A user joined')
