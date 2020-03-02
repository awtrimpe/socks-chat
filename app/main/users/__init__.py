from flask import Blueprint, redirect, render_template, request, url_for

from app.main.database import get_session
from app.main.database.tables import User


def register_user(session, username, password, first_name, last_name):
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


def get_user(session, username, password):
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
