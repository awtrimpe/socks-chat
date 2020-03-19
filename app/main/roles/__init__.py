from sqlalchemy.orm.session import Session

from app.main.database.tables import Permission, User, UserPermission
from app.main.users import get_user_with_permissions


def set_user_permission(session: Session, permission: str, user_id: int) -> UserPermission:
    '''
    Creates a user's permission entry to be set in the database

    Args:
        session (Session): The database session used to query for existing controls
        user_id (int): The ID of the new user that needs permissions set

    Returns:
        An instance of UserPermission for the database
    '''
    # If first user to register, make them admin
    if len(session.query(User).all()) <= 1:
        role = session.query(Permission).filter_by(name='admin').first()
    else:
        role = session.query(Permission).filter_by(name=permission).first()
    return UserPermission(permission_id=role.id, user_id=user_id)


def change_user_permission(session: Session, user_id: int) -> UserPermission:
    '''
    Switches a user's permission entry to the opposite of the current setting

    Args:
        session (Session): The database session used to query for existing controls
        user_id (int): The ID of the new user that needs permissions switched

    Returns:
        An instance of UserPermission for the database
    '''
    user_info = get_user_with_permissions(session, user_id)
    user_perm = session.query(UserPermission).filter_by(
        user_id=user_id).first()

    role = session.query(Permission).filter_by(name='admin').first()

    # Make sure this isn't the last admin, otherwise there will be no admins
    admins = session.query(UserPermission).filter_by(
        permission_id=role.id).all()
    if len(admins) <= 1 and admins[0].user_id == int(user_id):
        raise Exception('Cannot remove last admin')

    if user_info.Permission.name == 'admin':
        role = session.query(Permission).filter_by(name='user').first()

    user_perm.permission_id = role.id

    return user_perm
