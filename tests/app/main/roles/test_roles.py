import pytest

from app.main.database.tables import Permission, UserPermission
from app.main.roles import change_user_permission, set_user_permission
from app.main.users import register_user


def describe_set_user_permission():
    def test_set_user_permission(session, client):
        with session() as session:
            user = register_user(
                session, 'diageo', 'St._Jamess_Gate_Dublin', 'Arthur', 'Guinness')
            session.add(user)
            session.commit()
            perm = set_user_permission(session, 'admin', user.id)
            session.add(perm)
            session.commit()

            admin_perm = session.query(
                Permission).filter_by(name='admin').first()
            user_perm = session.query(UserPermission).filter_by(
                user_id=user.id).first()

            assert user_perm.permission_id == admin_perm.id

    def test_set_user_permission_first_user(session, client):
        with session() as session:
            user = register_user(
                session, 'diageo', 'St._Jamess_Gate_Dublin', 'Arthur', 'Guinness')
            session.add(user)
            session.commit()
            # First user must be the admin
            perm = set_user_permission(session, 'user', user.id)
            session.add(perm)
            session.commit()

            admin_perm = session.query(
                Permission).filter_by(name='admin').first()
            user_perm = session.query(UserPermission).filter_by(
                user_id=user.id).first()

            assert user_perm.permission_id == admin_perm.id

    def test_set_user_permission_multiple_users(session, client):
        with session() as session:
            user = register_user(
                session, 'diageo', 'St._Jamess_Gate_Dublin', 'Arthur', 'Guinness')
            session.add(user)
            session.commit()
            perm = set_user_permission(session, 'admin', user.id)
            session.add(perm)
            session.commit()

            admin_perm = session.query(
                Permission).filter_by(name='admin').first()
            user_perm = session.query(UserPermission).filter_by(
                user_id=user.id).first()

            assert admin_perm.id == user_perm.permission_id

            new_user_2 = register_user(
                session, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
            session.add(new_user_2)
            session.commit()
            perm_2 = set_user_permission(session, 'user', new_user_2.id)
            session.add(perm_2)
            session.commit()

            user_permission = session.query(
                Permission).filter_by(name='user').first()
            user2_perm = session.query(UserPermission).filter_by(
                user_id=new_user_2.id).first()

            assert user_permission.id == user2_perm.permission_id


def describe_change_user_permission():
    def test_change_second_user(session, client):
        with session() as session:
            new_user_1 = register_user(
                session, 'sabmiller', 'ColdAsTheRockies', 'Coors', 'Light')
            session.add(new_user_1)
            session.commit()
            perm = set_user_permission(session, 'admin', new_user_1.id)
            session.add(perm)
            session.commit()
            new_user_2 = register_user(
                session, 'anheuserbusch', 'DillyDilly', 'Bud', 'Light')
            session.add(new_user_2)
            session.commit()
            perm_2 = set_user_permission(session, 'user', new_user_2.id)
            session.add(perm_2)
            session.commit()

            user_permission = session.query(
                Permission).filter_by(name='user').first()
            admin_permission = session.query(
                Permission).filter_by(name='admin').first()
            user_perm_2 = session.query(UserPermission).filter_by(
                user_id=new_user_2.id).first()
            assert user_perm_2.permission_id == user_permission.id

            change_user_permission(session, new_user_2.id)
            session.commit()
            assert user_perm_2.permission_id == admin_permission.id
            change_user_permission(session, new_user_2.id)
            session.commit()
            assert user_perm_2.permission_id == user_permission.id

    def test_change_only_admin(session, client):
        with session() as session:
            user = register_user(
                session, 'diageo', 'St._Jamess_Gate_Dublin', 'Arthur', 'Guinness')
            session.add(user)
            session.commit()
            perm = set_user_permission(session, 'admin', user.id)
            session.add(perm)
            session.commit()

            with pytest.raises(Exception) as exc:
                change_user_permission(session, user.id)
            assert str(exc.value) == 'Cannot remove last admin'
