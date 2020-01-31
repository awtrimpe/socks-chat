import pytest
from flask import current_app, g, request, url_for

from app.main.database.tables import User
from app.main.users.registration import register_user


def describe_register():
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
