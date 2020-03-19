import json
import sys

from flask import (Blueprint, Markup, flash, g, jsonify, redirect,
                   render_template, request, session, url_for)
from flask_login import current_user, login_user, logout_user

from app.main.admin import (get_admin_control_by_id, get_admin_control_by_name,
                            get_admin_controls)
from app.main.database.tables import User
from app.main.forms import LoginForm, RegisterForm
from app.main.helpers import svg_contents
from app.main.roles import change_user_permission, set_user_permission
from app.main.users import (delete_user, get_all_users_with_permissions,
                            get_user, is_admin, register_user)

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    '''Login form to enter a room.'''
    if current_user.is_authenticated:
        return redirect(url_for('.chat'))
    admin = is_admin(g.session, current_user)
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        try:
            user = get_user(g.session, username, password)
            login_user(user)
            session['username'] = username
            session['name'] = f'{user.first_name} {user.last_name}'
            session['room'] = form.room.data
            return redirect(url_for('.chat'))
        except Exception as err:
            return render_template('index.html',
                                   msg=str(err),
                                   form=form,
                                   admin=admin,
                                   svg=Markup(svg_contents('./app/static/socks.svg')))
    elif request.method == 'GET':
        form.username.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form, admin=admin, svg=Markup(svg_contents('./app/static/socks.svg')))


@bp.route('/about')
def about():
    admin = is_admin(g.session, current_user)
    return render_template('about.html',
                           svg=Markup(svg_contents('./app/static/socks.svg')),
                           admin=admin,
                           github=Markup(svg_contents('./app/static/github.svg')))


@bp.route('/admin', methods=['GET', 'PATCH', 'DELETE'])
def admin():
    admin = is_admin(g.session, current_user)
    if admin:
        if request.method == 'GET':
            users = get_all_users_with_permissions(g.session)
            controls = get_admin_controls(g.session)
            return render_template('admin.html',
                                   svg=Markup(svg_contents(
                                       './app/static/socks.svg')),
                                   trash=Markup(svg_contents(
                                       './app/static/trash.svg')),
                                   admin=admin,
                                   users=users,
                                   controls=controls)
        elif request.method == 'PATCH':
            if request.json.get('control'):
                try:
                    control_id = request.json.get('control')
                    get_admin_control_by_id(g.session, control_id).switch()
                    g.session.commit()
                    return jsonify({'msg': f'Control ID: {control_id} successfull changed'}), 200
                except:
                    return jsonify({'msg': 'Something went wrong changing the control'}), 500
            elif request.json.get('user'):
                try:
                    user_id = request.json.get('user')
                    change_user_permission(g.session, user_id)
                    g.session.commit()
                    return jsonify({'msg': f'User permissions changed for ID {user_id}'}), 200
                except Exception as err:
                    return jsonify({'msg': str(err)}), 500
            else:
                return jsonify({'msg': 'A known value was not supplied'}), 200

        elif request.method == 'DELETE':
            if request.json.get('user'):
                user_id = request.json.get('user')
                delete_user(g.session, user_id)
                g.session.commit()
                return jsonify({'msg': f'User with ID {user_id} successfully deleted'}), 200
            else:
                return jsonify({'msg': 'A known value was not supplied'}), 200
        else:
            return 'Unknown request received', 400
    else:
        return 'Access denied', 401


@bp.route('/chat')
def chat():
    '''Chat room. The user's name and room must be stored in the session.'''
    admin = is_admin(g.session, current_user)
    username = session.get('username', '')
    name = session.get('name')
    room = session.get('room', '')
    if name == '' or room == '':
        flash('You must be logged in to access the chatroom')
        return redirect(url_for('.index'))
    return render_template('chat.html',
                           name=name,
                           room=room,
                           admin=admin,
                           svg=Markup(svg_contents('./app/static/socks.svg')),
                           send_logo=Markup(svg_contents('./app/static/send.svg')))


@bp.route('/logout', methods=['GET'])
def logout():
    admin = is_admin(g.session, current_user)
    logout_user()
    session.clear()
    flash('You have been successfully logged out')
    return redirect(url_for('.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    admin = is_admin(g.session, current_user)
    form = RegisterForm()
    # Check if 'new_users' is turned on or off
    if not get_admin_control_by_name(g.session, 'new_users').value:
        return render_template('register.html',
                               form=form,
                               admin=admin,
                               msg='New user registration has been disabled at this time',
                               svg=Markup(svg_contents('./app/static/socks.svg')))
    if request.method == 'GET':
        return render_template('register.html', form=form, svg=Markup(svg_contents('./app/static/socks.svg')))
    elif request.method == 'POST':
        if form.validate_on_submit():
            username = request.form.get('username')
            password = request.form.get('password')
            password_conf = request.form.get('password_conf')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            if password != password_conf:
                return render_template('register.html',
                                       form=form,
                                       admin=admin,
                                       msg='Passwords did not match',
                                       svg=Markup(svg_contents('./app/static/socks.svg')))
            try:
                new_user = register_user(
                    g.session, username, password, first_name, last_name)
                try:
                    # add the new user to the database
                    g.session.add(new_user)
                    g.session.commit()
                except:
                    g.session.rollback()
                    raise Exception('Error adding new user')
                # Set user's role as 'user'
                user_permission = set_user_permission(
                    g.session, 'user', new_user.id)
                try:
                    # add the new user's related permission to the database
                    g.session.add(user_permission)
                    g.session.commit()
                except:
                    g.session.rollback()
                    raise Exception('Error setting user permissions')
            except Exception as err:
                return render_template('register.html',
                                       form=form,
                                       admin=admin,
                                       msg=str(err),
                                       svg=Markup(svg_contents('./app/static/socks.svg')))
            except:
                return render_template('register.html',
                                       form=form,
                                       admin=admin,
                                       msg=f'Unexpected error: {sys.exc_info()[0]}',
                                       svg=Markup(svg_contents('./app/static/socks.svg')))
        else:
            return render_template('register.html',
                                   form=form,
                                   admin=admin,
                                   msg='Not all required fields provided',
                                   svg=Markup(svg_contents('./app/static/socks.svg')))
    flash('Registration successful')
    return redirect(url_for('.index'))
