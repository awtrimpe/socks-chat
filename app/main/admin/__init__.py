from typing import List

from sqlalchemy.orm.session import Session

from app.main.database.tables import AdminControl


def get_admin_controls(session: Session) -> List[AdminControl]:
    '''
    Gets all admin controls from the database

    Args:
        session (Session): The database session used to query for existing controls

    Returns:
        A list of AdminControl objects from the database
    '''
    return session.query(AdminControl).all()


def get_admin_control_by_name(session: Session, control_name: str) -> AdminControl:
    '''
    Gets a single admin control from the database

    Args:
        session (Session): The database session used to query for existing controls
        control_name (str): The name of the control desired

    Returns:
        An instance of Admin Control from the database
    '''
    return session.query(AdminControl).filter_by(name=control_name).first()


def get_admin_control_by_id(session: Session, control_id: int) -> bool:
    '''
    Gets a single admin control from the database

    Args:
        session (Session): The database session used to query for existing controls
        control_name (str): The name of the control desired

    Returns:
        An instance of Admin Control from the database
    '''
    return session.query(AdminControl).filter_by(id=control_id).first()
