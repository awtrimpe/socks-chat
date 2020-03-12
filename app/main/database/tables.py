from flask import g
from flask_login import UserMixin
from sqlalchemy import (Boolean, Column, ForeignKey, Integer, String,
                        UniqueConstraint)
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import check_password_hash, generate_password_hash

from app import login_manager

Base = declarative_base()


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(int(user_id))
    except SQLAlchemyError as e:
        print(f'SQLAlchemyError {e}')
        return None
    except Exception as e:
        print(f'Load failed {e}')
        return None


class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(16), nullable=False)
    password = Column(String(200), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    def set_password(self, password):
        '''Create hashed password.'''
        self.password = generate_password_hash(
            password, method='pbkdf2:sha256', salt_length=8)

    def check_password(self, password):
        '''Check hashed password.'''
        return check_password_hash(self.password, password)

    def serialize_all(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Permission(Base):
    __tablename__ = 'permissions'
    id = Column(Integer, primary_key=True)
    name = Column(String(16), unique=True, nullable=False)

    def serialize_all(self):
        return {
            'id': self.id,
            'name': self.name
        }


class UserPermission(Base):
    __tablename__ = 'user_permissions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    permission_id = Column(Integer, ForeignKey(
        'permissions.id'), nullable=False)

    UniqueConstraint(user_id, permission_id, name='user_perm')

    def serialize_all(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'permission_id': self.permission_id
        }


class AdminControl(Base):
    __tablename__ = 'admin_control'
    id = Column(Integer, primary_key=True)
    name = Column(String(16), unique=True, nullable=False)
    value = Column(Boolean, nullable=False, unique=False, default=True)

    def serialize_all(self):
        return {
            'id': self.id,
            'name': self.name,
            'value': self.value
        }

    def switch(self):
        self.value = not self.value
