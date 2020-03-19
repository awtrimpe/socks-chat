import pytest
from flask import request, url_for

from app.main.database.tables import User
from app.main.roles import change_user_permission, set_user_permission
from app.main.users import (delete_user, get_all_users,
                            get_all_users_with_permissions, get_user,
                            get_user_with_permissions, is_admin, register_user)
from tests.conftest import test_with_authenticated_user


def describe_register_user():
    def test_register_unique(session):
        with session() as session:
            resp = register_user(session,
                                 'cmorgan', 'LiveLikeTheCaptain', 'Captain', 'Morgan')
            assert type(resp) == User

    def test_register_already_exists(session):
        with session() as session:
            with pytest.raises(Exception) as exc:
                new_user = register_user(
                    session, 'cmorgan', 'LiveLikeTheCaptain', 'Captain', 'Morgan')
                session.add(new_user)
                session.commit()
                register_user(session, 'cmorgan',
                              'LiveLikeTheCaptain', 'Captain', 'Morgan')
        assert str(exc.value) == 'Username already used'

    def test_password_hashed(session):
        with session() as session:
            new_user = register_user(
                session, 'cmorgan', 'LiveLikeTheCaptain', 'Captain', 'Morgan')
            session.add(new_user)
            session.commit()
            user = session.query(User).filter_by(username='cmorgan').first()
            assert user.first_name == 'Captain'
            assert user.last_name == 'Morgan'
            assert user.username == 'cmorgan'
            assert user.password != 'LiveLikeTheCaptain'


def describe_get_user():
    def test_valid_user(session):
        with session() as session:
            new_user = register_user(
                session, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
            session.add(new_user)
            session.commit()
            user = get_user(session, 'anheuserbusch', 'DillyDilly')
            assert type(user) == User
            assert user.first_name == 'Bud'
            assert user.last_name == 'Light'
            assert user.username == 'anheuserbusch'

    def test_invalid_user(session):
        with session() as session:
            with pytest.raises(Exception) as exc:
                user = get_user(session, 'notreal', 'password')
        assert str(exc.value) == 'The username or password provided was incorrect'


def describe_get_all_users():
    def test_get_all_users(session):
        with session() as session:
            new_user_1 = register_user(
                session, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
            session.add(new_user_1)
            session.commit()
            new_user_2 = register_user(
                session, 'especial1925', 'ABInBev', 'Grupo', 'Modelo')
            session.add(new_user_2)
            session.commit()

            users = get_all_users(session)
            assert type(users) == list
            assert len(users) == 2
            assert new_user_1 in users and new_user_2 in users


def describe_get_user_with_permissions():
    def test_get_user_with_permissions(session, client):
        with session() as session:
            new_user_1 = register_user(
                session, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
            session.add(new_user_1)
            session.commit()
            perm_1 = set_user_permission(session, 'admin', new_user_1.id)
            session.add(perm_1)
            session.commit()
            new_user_2 = register_user(
                session, 'especial1925', 'ABInBev', 'Grupo', 'Modelo')
            session.add(new_user_2)
            session.commit()
            perm_2 = set_user_permission(session, 'user', new_user_2.id)
            session.add(perm_2)
            session.commit()
            user = get_user_with_permissions(session, new_user_1.id)
            assert new_user_1 in user
            assert perm_1 in user
            assert user.User.first_name == 'Bud'
            assert user.Permission.name == 'admin'


def describe_get_all_users_with_permissions():
    def test_get_all_users_with_permissions(session, client):
        with session() as session:
            new_user_1 = register_user(
                session, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
            session.add(new_user_1)
            session.commit()
            perm_1 = set_user_permission(session, 'admin', new_user_1.id)
            session.add(perm_1)
            session.commit()
            new_user_2 = register_user(
                session, 'especial1925', 'ABInBev', 'Grupo', 'Modelo')
            session.add(new_user_2)
            session.commit()
            perm_2 = set_user_permission(session, 'user', new_user_2.id)
            session.add(perm_2)
            session.commit()
            users = get_all_users_with_permissions(session)
            assert new_user_1 in users[0] or new_user_1 in users[1]
            assert new_user_2 in users[0] or new_user_2 in users[1]
            assert perm_1 in users[0] or perm_1 in users[1]
            assert perm_2 in users[0] or perm_2 in users[1]
            assert len(users) == 2


def describe_is_admin():
    def test_is_admin(session, client):
        with session() as session:
            new_user_1 = register_user(
                session, 'especial1925', 'ABInBev', 'Grupo', 'Modelo')
            session.add(new_user_1)
            session.commit()
            # First user must always be admin even though we are asking for user
            perm_1 = set_user_permission(session, 'user', new_user_1.id)
            session.add(perm_1)
            session.commit()

            test_with_authenticated_user(session)

            admin = is_admin(session, new_user_1)
            assert admin

            new_user_2 = register_user(
                session, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
            session.add(new_user_2)
            session.commit()
            perm_2 = set_user_permission(session, 'admin', new_user_2.id)
            session.add(perm_2)
            session.commit()

            # Now that there is a second user, change first user to 'user'
            change_user_permission(session, new_user_1.id)
            session.commit()

            admin = is_admin(session, new_user_1)
            assert not admin


def describe_delete_user():
    def test_delete_user(session):
        with session() as session:
            new_user = register_user(
                session, 'sabmiller', 'ColdAsTheRockies', 'Coors', 'Light')
            session.add(new_user)
            session.commit()

            assert len(session.query(User).all()) == 1
            assert delete_user(session, new_user.id)
            assert len(session.query(User).all()) == 0
            # Bad session provided
            assert not delete_user(session.query, 1)
