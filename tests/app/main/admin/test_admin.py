from app.main.admin import (get_admin_control_by_id, get_admin_control_by_name,
                            get_admin_controls)
from app.main.database.tables import AdminControl


def describe_get_admin_controls():
    def test_get_admin_controls(session, client):
        with session() as session:
            controls = get_admin_controls(session)
            assert type(controls) == list
            assert len(controls) == 1


def describe_get_admin_control_by_name():
    def test_get_admin_control_by_name(session, client):
        with session() as session:
            control = get_admin_control_by_name(session, 'new_users')
            assert type(control) == AdminControl
            assert control.name == 'new_users'


def describe_get_admin_control_by_id():
    def test_get_admin_control_by_id(session, client):
        with session() as session:
            ctrl = AdminControl(name='new_ctrl', value=False)
            session.add(ctrl)
            session.commit()
            control = get_admin_control_by_id(session, ctrl.id)
            assert type(control) == AdminControl
            assert control.name == ctrl.name
            assert control.value == ctrl.value
