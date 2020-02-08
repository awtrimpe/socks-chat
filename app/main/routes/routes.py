from flask import (Blueprint, Markup, flash, g, redirect, render_template,
                   request, session, url_for)
from flask_login import current_user, login_user, logout_user

from app.main.database.tables import User
from app.main.forms import LoginForm, RegisterForm
from app.main.helpers import svg_contents
from app.main.users import get_user, register_user

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    '''Login form to enter a room.'''
    if current_user.is_authenticated:
        return redirect(url_for('.chat'))
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
            return render_template('index.html', msg=err, form=form, svg=Markup(svg_contents('./app/static/socks.svg')))
    elif request.method == 'GET':
        form.username.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form, svg=Markup(svg_contents('./app/static/socks.svg')))


@bp.route('/chat')
def chat():
    '''Chat room. The user's name and room must be stored in the session.'''
    username = session.get('username', '')
    name = session.get('name')
    room = session.get('room', '')
    if name == '' or room == '':
        flash('You must be logged in to access the chatroom')
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room, svg=Markup(svg_contents('./app/static/socks.svg')), send_logo=Markup(svg_contents('./app/static/send.svg')))


@bp.route('/about')
def about():
    return render_template('about.html', svg=Markup(svg_contents('./app/static/socks.svg')), github=Markup(svg_contents('./app/static/github.svg')))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
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
                return render_template('register.html', form=form, msg='Passwords did not match', svg=Markup(svg_contents('./app/static/socks.svg')))
            try:
                new_user = register_user(
                    g.session, username, password, first_name, last_name)
                # add the new user to the database
                g.session.add(new_user)
                g.session.commit()
            except Exception as err:
                return render_template('register.html', form=form, msg=err, svg=Markup(svg_contents('./app/static/socks.svg')))
        else:
            return render_template('register.html', form=form, msg='Not all required fields provided', svg=Markup(svg_contents('./app/static/socks.svg')))
    return redirect(url_for('.index', msg='Registration successful'))


@bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    session.clear()
    flash('You have been successfully logged out')
    return redirect(url_for('.index'))
