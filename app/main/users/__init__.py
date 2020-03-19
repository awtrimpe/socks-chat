from typing import List

from flask import Blueprint, redirect, render_template, request, url_for
from sqlalchemy.orm.session import Session
from werkzeug.local import LocalProxy

from app.main.database import get_session
from app.main.database.tables import Permission, User, UserPermission


def register_user(session: Session, username: str, password: str, first_name: str, last_name: str) -> User:
    '''
    Creates a new account and stores it in the database

    Args:
        session (Session): The database session used to query for existing users
        username (str): The username to be set
        password (str): The provided password for the user
        first_name (str): The user's first name
        last_name (str): The user's last name

    Returns:
        A User object to be set in the database
    '''
    if session.query(User).filter_by(username=username).first():
        raise Exception('Username already used')

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(username=username, password=password,
                    first_name=first_name, last_name=last_name)
    new_user.set_password(new_user.password)

    return new_user


def get_user(session: Session, username: str, password: str) -> User:
    '''
    Gets user and checks password provided from the database

    Args:
        session (Session): The database session used to query for existing users
        username (str): The username in the database
        password (str): The provided password for the user

    Returns:
        A User object from the database
    '''
    user = session.query(User).filter_by(username=username).first()
    if user and user.check_password(password=password):
        return user
    else:
        raise Exception('The username or password provided was incorrect')


def get_all_users(session: Session) -> List[User]:
    '''
    Gets all users from the database

    Args:
        session (Session): The database session used to query for existing users

    Returns:
        A list of User objects from the database
    '''
    return session.query(User).all()


def get_user_with_permissions(session: Session, user_id: int):
    '''
    Gets all users from the database with the assigned permissions

    Args:
        session (Session): The database session used to query for existing users

    Returns:
        A list of User objects from the database with their associated permissions
    '''
    return session.query(User, UserPermission, Permission).filter(User.id == user_id).filter(User.id == UserPermission.user_id).filter(UserPermission.permission_id == Permission.id).first()


def get_all_users_with_permissions(session: Session) -> List:
    '''
    Gets all users from the database with the assigned permissions

    Args:
        session (Session): The database session used to query for existing users

    Returns:
        A list of User objects from the database with their associated permissions
    '''
    return session.query(User, UserPermission, Permission).filter(User.id == UserPermission.user_id).filter(UserPermission.permission_id == Permission.id).all()


def is_admin(session: Session, current_user: LocalProxy) -> bool:
    '''
    Gets all users from the database with the assigned permissions

    Args:
        session (Session): The database session used to query for existing users
        current_user (LocalProxy): The current user managed by Flask Login

    Returns:
        A boolean on if the user is an admin or not
    '''
    if current_user.is_authenticated and get_user_with_permissions(session, current_user.id).Permission.name == 'admin':
        return True
    else:
        return False


def delete_user(session: Session, user_id: int) -> bool:
    '''
    Deletes a user and their relevant permissions from the database

    Args:
        session (Session): The database session used to query for existing users
        user_id (int): The ID of the user to be removed

    Returns:
        A boolean on if the deletion was successful or not
    '''
    try:
        session.query(UserPermission).filter_by(user_id=user_id).delete()
        session.query(User).filter_by(id=user_id).delete()
        return True
    except:
        return False
