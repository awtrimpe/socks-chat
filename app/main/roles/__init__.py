from sqlalchemy.orm.session import Session

from app.main.database.tables import Permission, UserPermission


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
    if user_id == 1:
        role = session.query(Permission).filter_by(name='admin').first()
    else:
        role = session.query(Permission).filter_by(name=permission).first()
    return UserPermission(role.id, user_id)
