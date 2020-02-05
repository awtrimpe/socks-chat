from flask import url_for

from app.main.users import register_user


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


def describe_chat():
    def test_signed_in_chat(client):
        with client.session_transaction() as session:
            session['name'] = 'TestUser2'
            session['room'] = 'AFakeRoom2'
        resp = client.get('/chat', follow_redirects=True)
        assert b'<title>Socks Chat | Chat</title>' in resp.data

    def test_not_signed_in_chat(client):
        resp = client.get('/chat', follow_redirects=True)
        assert b'<title>Socks Chat | Home</title>' in resp.data


def describe_about():
    def test_about_page(client):
        resp = client.get('/about')
        assert b'<title>Socks Chat | About</title>' in resp.data
