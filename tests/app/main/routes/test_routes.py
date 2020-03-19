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

    def test_user_already_logged_in(client, session):
        with session() as session:
            new_user = register_user(
                session, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
            session.add(new_user)
            session.commit()
            perm = set_user_permission(session, 'user', new_user.id)
            session.add(perm)
            session.commit()

            test_with_authenticated_user(session)

            with client.session_transaction() as f_session:
                f_session['username'] = 'anheuserbusch'
                f_session['name'] = 'Bud Light'
                f_session['room'] = 'ABInBev'

            resp = client.get('/', follow_redirects=True)
            assert b'<title>Socks Chat | Chat</title>' in resp.data

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
    # GET
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

    # PATCH
    def test_patch_control(client, session):
        from app.main.admin import get_admin_control_by_name
        with session() as session:
            control_id = get_admin_control_by_name(session, 'new_users').id
            new_user = register_user(
                session, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
            session.add(new_user)
            session.commit()
            perm = set_user_permission(session, 'admin', new_user.id)
            session.add(perm)
            session.commit()

            test_with_authenticated_user(session)

        resp = client.patch('/admin', json={'control': control_id})
        assert resp.status_code == 200
        assert resp.json == {
            'msg': f'Control ID: {control_id} successfull changed'}

    def test_patch_control_exception(client, session):
        from app.main.admin import get_admin_control_by_name
        with session() as session:
            control_id = get_admin_control_by_name(session, 'new_users').id
            new_user = register_user(
                session, 'especial1925', 'ABInBev', 'Grupo', 'Modelo')
            session.add(new_user)
            session.commit()
            perm = set_user_permission(session, 'user', new_user.id)
            session.add(perm)
            session.commit()

            test_with_authenticated_user(session)

        with patch('app.main.routes.routes.get_admin_control_by_id', side_effect=Exception('admin_switch_err')):
            resp = client.patch(
                '/admin', json={'control': control_id}, follow_redirects=True)
            assert resp.status_code == 500
            assert resp.json == {
                'msg': 'Something went wrong changing the control'}

    def test_patch_user(client, session):
        with session() as session:
            new_user = register_user(
                session, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
            session.add(new_user)
            session.commit()
            perm = set_user_permission(session, 'admin', new_user.id)
            session.add(perm)
            session.commit()
            new_user = register_user(
                session, 'especial1925', 'ABInBev', 'Grupo', 'Modelo')
            session.add(new_user)
            session.commit()
            perm = set_user_permission(session, 'user', new_user.id)
            session.add(perm)
            session.commit()

            test_with_authenticated_user(session)

            user_id = new_user.id
        resp = client.patch('/admin', json={'user': user_id})
        assert resp.status_code == 200
        assert resp.json == {
            'msg': f'User permissions changed for ID {user_id}'}

    def test_patch_user_exception(client, session):
        with session() as session:
            new_user = register_user(
                session, 'especial1925', 'ABInBev', 'Grupo', 'Modelo')
            session.add(new_user)
            session.commit()
            perm = set_user_permission(session, 'user', new_user.id)
            session.add(perm)
            session.commit()

            test_with_authenticated_user(session)

            user_id = new_user.id

        with patch('app.main.routes.routes.change_user_permission', side_effect=Exception('user_permission_err')):
            resp = client.patch(
                '/admin', json={'user': user_id}, follow_redirects=True)
            assert resp.status_code == 500
            assert resp.json == {'msg': 'user_permission_err'}

    def test_patch_user_base_exception(client, session):
        with session() as session:
            new_user = register_user(
                session, 'especial1925', 'ABInBev', 'Grupo', 'Modelo')
            session.add(new_user)
            session.commit()
            perm = set_user_permission(session, 'user', new_user.id)
            session.add(perm)
            session.commit()

            test_with_authenticated_user(session)

            user_id = new_user.id

        with patch('app.main.routes.routes.change_user_permission', side_effect=BaseException('user_permission_err')):
            resp = client.patch(
                '/admin', json={'user': user_id}, follow_redirects=True)
            assert resp.status_code == 500
            assert resp.json == {
                'msg': 'Something went wrong changing the user permission'}

    def test_patch_user_bad_json(client, session):
        with session() as session:
            new_user = register_user(
                session, 'especial1925', 'ABInBev', 'Grupo', 'Modelo')
            session.add(new_user)
            session.commit()
            perm = set_user_permission(session, 'user', new_user.id)
            session.add(perm)
            session.commit()

            test_with_authenticated_user(session)

            user_id = new_user.id

        with patch('app.main.routes.routes.change_user_permission', side_effect=BaseException('user_permission_err')):
            resp = client.patch(
                '/admin', json={'bad_key': user_id}, follow_redirects=True)
            assert resp.status_code == 400
            assert resp.json == {'msg': 'A known value was not supplied'}

    # DELETE
    def test_delete_user(client, session):
        with session() as session:
            new_user = register_user(
                session, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
            session.add(new_user)
            session.commit()
            perm = set_user_permission(session, 'admin', new_user.id)
            session.add(perm)
            session.commit()
            new_user = register_user(
                session, 'especial1925', 'ABInBev', 'Grupo', 'Modelo')
            session.add(new_user)
            session.commit()
            perm = set_user_permission(session, 'user', new_user.id)
            session.add(perm)
            session.commit()

            test_with_authenticated_user(session)

            delete_id = new_user.id
            resp = client.delete('/admin', json={'user': delete_id})
            assert resp.status_code == 200
            assert resp.json == {
                'msg': f'User with ID {delete_id} successfully deleted'}

    def test_delete_user_bad_json(client, session):
        with session() as session:
            new_user = register_user(
                session, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
            session.add(new_user)
            session.commit()
            perm = set_user_permission(session, 'admin', new_user.id)
            session.add(perm)
            session.commit()

            test_with_authenticated_user(session)

            resp = client.delete('/admin', json={'bad_key': new_user.id})
            assert resp.status_code == 400
            assert resp.json == {'msg': 'A known value was not supplied'}


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

    def test_exception_on_register(client):
        data = {'username': 'sabmiller', 'password': 'ColdAsTheRockies',
                'password_conf': 'ColdAsTheRockies', 'first_name': 'Coors', 'last_name': 'Light'}
        with patch('app.main.routes.routes.register_user', side_effect=Exception('mocked error')):
            resp = client.post('/register', data=data, follow_redirects=True)
            assert b'<title>Socks Chat | Register</title>' in resp.data
            assert b'<p class="warning" id="msg">mocked error</p>' in resp.data

    def test_base_exception_on_register(client):
        data = {'username': 'sabmiller', 'password': 'ColdAsTheRockies',
                'password_conf': 'ColdAsTheRockies', 'first_name': 'Coors', 'last_name': 'Light'}
        with patch('app.main.routes.routes.register_user', side_effect=BaseException('base exception')):
            resp = client.post('/register', data=data, follow_redirects=True)
            assert b'<title>Socks Chat | Register</title>' in resp.data
            assert b'<p class="warning" id="msg">Unexpected error: &lt;class &#39;BaseException&#39;&gt;</p>' in resp.data

    def test_invalid_user(client):
        data = {'username': 'SigloXX', 'password': 'CerveceríaCuauhtémoc',
                'password_conf': 'CerveceríaCuauhtémoc', 'first_name': 'Dos', 'last_name': 'Equis'}
        with patch('app.main.routes.routes.register_user', side_effect='a_string_instead_of_a_user'):
            resp = client.post('/register', data=data, follow_redirects=True)
            assert b'<title>Socks Chat | Register</title>' in resp.data
            assert b'<p class="warning" id="msg">Error adding new user</p>' in resp.data

    def test_exception_on_permissions(client):
        data = {'username': 'SigloXX', 'password': 'CerveceríaCuauhtémoc',
                'password_conf': 'CerveceríaCuauhtémoc', 'first_name': 'Dos', 'last_name': 'Equis'}
        with patch('app.main.routes.routes.set_user_permission', side_effect='a_string_instead_of_a_permission'):
            resp = client.post('/register', data=data, follow_redirects=True)
            assert b'<title>Socks Chat | Register</title>' in resp.data
            assert b'<p class="warning" id="msg">Error setting user permissions</p>' in resp.data

    def test_new_registration_off(client, session):
        with session() as session:
            get_admin_control_by_name(session, 'new_users').switch()
            session.commit()
            resp = client.get('/register')
            assert b'New user registration has been disabled at this time' in resp.data
