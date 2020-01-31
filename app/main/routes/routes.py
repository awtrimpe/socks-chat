from flask import (Blueprint, Markup, g, redirect, render_template, request,
                   session, url_for)
from flask_login import login_required

from app.main.forms import LoginForm, RegisterForm
from app.main.helpers import svg_contents
from app.main.users.registration import register_user

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    '''Login form to enter a room.'''
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form, svg=Markup(svg_contents('./app/static/socks.svg')))


@bp.route('/chat')
# @login_required
def chat():
    '''Chat room. The user's name and room must be stored in the session.'''
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
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
