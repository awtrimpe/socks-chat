from unittest.mock import patch

from flask import current_app, url_for
from flask_login import login_user

from app.main.admin import get_admin_control_by_name
from app.main.database.tables import User
from app.main.roles import set_user_permission
from app.main.users import register_user
from tests.conftest import test_with_authenticated_user


def describe_index():
    def test_home_page(client):
        resp = client.get('/')
        assert resp.status_code == 200
        assert b'<title>Socks Chat | Home</title>' in resp.data
        with client.session_transaction() as session:
            assert session.get('name', '') == ''

    def test_home_logged_in(client, session):
        with session() as session:
            new_user = register_user(
                session, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
            session.add(new_user)
            session.commit()

            data = {'username': 'anheuserbusch',
                    'password': 'DillyDilly', 'room': 'AFakeRoom'}
            resp = client.post('/', data=data, follow_redirects=True)
            assert resp.status_code == 200
            assert b'<title>Socks Chat | Chat</title>' in resp.data
            assert b'AFakeRoom' in resp.data
            with client.session_transaction() as session:
                assert session.get('name', '') == 'Bud Light'
                assert session.get('room', '') == 'AFakeRoom'

    def test_home_not_logged_in(client):
        data = {'name': 'TestUser', 'room': 'AFakeRoom'}
        resp = client.post('/', data=data, follow_redirects=True)
        assert resp.status_code == 200
        assert b'<title>Socks Chat | Home</title>' in resp.data
        with client.session_transaction() as session:
            assert session.get('name', '') == ''
            assert session.get('room', '') == ''

    # def test_user_already_logged_in(client, session):
    #     with app.app_context():
    #         with app.test_request_context():
    #             with session() as session:
    #                 new_user = register_user(
    #                     session, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
    #                 session.add(new_user)
    #                 session.commit()
    #                 login_user(new_user)
    #                 resp = client.get('/', follow_redirects=True)
    #                 assert b'<title>Socks Chat | Chat</title>' in resp.data

    def test_user_not_valid(client, session):
        data = {'username': 'oneone',
                'password': 'badpass', 'room': 'AFakeRoom'}
        resp = client.post('/', data=data, follow_redirects=True)
        assert resp.status_code == 200
        assert b'<title>Socks Chat | Home</title>' in resp.data
        assert b'The username or password provided was incorrect' in resp.data


def describe_about():
    def test_about_page(client):
        resp = client.get('/about')
        assert b'<title>Socks Chat | About</title>' in resp.data


def describe_admin():
    def test_admin_page(client, session):
        with session() as session:
            new_user = register_user(
                session, 'sabmiller', 'ColdAsTheRockies', 'Coors', 'Light')
            session.add(new_user)
            session.commit()
            perm = set_user_permission(session, 'admin', new_user.id)
            session.add(perm)
            session.commit()

            test_with_authenticated_user(session)

            resp = client.get('/admin')
            assert b'<title>Socks Chat | Admin</title>' in resp.data
            assert b'''<span class="horizontal">
            new_users''' in resp.data
            assert b'''sabmiller''' in resp.data
            assert b'''Coors Light''' in resp.data
            assert b'''<span class="horizontal">\n            new_users''' in resp.data

    def test_user_not_admin(client):
        resp = client.get('/admin')
        assert b'Access denied' in resp.data
        assert resp.status_code == 401


def describe_chat():
    def test_signed_in_chat(client):
        with client.session_transaction() as session:
            session['name'] = 'Test User2'
            session['room'] = 'AFakeRoom2'
        resp = client.get('/chat', follow_redirects=True)
        assert b'<title>Socks Chat | Chat</title>' in resp.data

    def test_not_signed_in_chat(client):
        resp = client.get('/chat', follow_redirects=True)
        assert b'<title>Socks Chat | Home</title>' in resp.data


def describe_logout():
    def test_logout(client):
        resp = client.get('/logout', follow_redirects=True)
        assert b'<title>Socks Chat | Home</title>' in resp.data
        assert b'You have been successfully logged out' in resp.data


def describe_register():
    def test_register_page(client):
        resp = client.get('/register')
        assert b'<h2>Create Account</h2>' in resp.data

    def test_register_user(client, session):
        data = {'username': 'sabmiller', 'password': 'ColdAsTheRockies',
                'password_conf': 'ColdAsTheRockies', 'first_name': 'Coors', 'last_name': 'Light'}
        resp = client.post('/register', data=data, follow_redirects=True)
        assert resp.status_code == 200
        assert b'<title>Socks Chat | Home</title>' in resp.data
        with session() as session:
            user = session.query(User).filter_by(username='sabmiller').first()
            assert user.first_name == 'Coors'

    def test_invalid_user_input(client):
        data = {'username': 'sabmiller', 'password': 'ColdAsTheRockies',
                'first_name': 'Coors', 'last_name': 'Light'}
        resp = client.post('/register', data=data, follow_redirects=True)
        assert b'Not all required fields provided' in resp.data

    def test_non_matching_passwords(client):
        data = {'username': 'sabmiller', 'password': 'ColdAsTheRockies',
                'password_conf': 'ReachForTheCold', 'first_name': 'Coors', 'last_name': 'Light'}
        resp = client.post('/register', data=data, follow_redirects=True)
        assert b'Passwords did not match' in resp.data

    def test_user_already_registered(client, session):
        with session() as session:
            new_user = register_user(
                session, 'sabmiller', 'ColdAsTheRockies', 'Coors', 'Light')
            session.add(new_user)
            session.commit()
            perm = set_user_permission(session, 'admin', new_user.id)
            session.add(perm)
            session.commit()
            data = {'username': 'sabmiller', 'password': 'ColdAsTheRockies',
                    'password_conf': 'ColdAsTheRockies', 'first_name': 'Coors', 'last_name': 'Light'}
            resp = client.post('/register', data=data, follow_redirects=True)
            assert b'Username already used' in resp.data

    # def test_invalid_user_added(client):
    #     import app.main.users as user_register
    #     data = {'username': 'sabmiller', 'password': 'ColdAsTheRockies',
    #             'password_conf': 'ColdAsTheRockies', 'first_name': 'Coors', 'last_name': 'Light'}
    #     with patch.object(user_register, "register_user", 'simple_string'):
    #         resp = client.post('/register', data=data, follow_redirects=True)
    #         assert b'<title>Socks Chat | Register</title>' in resp.data
    #         assert b'<p class="warning" id="msg">Not all required fields provided</p>' in resp.data

    def test_new_registration_off(client, session):
        with session() as session:
            get_admin_control_by_name(session, 'new_users').switch()
            session.commit()
            resp = client.get('/register')
            assert b'New user registration has been disabled at this time' in resp.data
