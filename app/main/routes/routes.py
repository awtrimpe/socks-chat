from flask import (Blueprint, Markup, redirect, render_template, request,
                   session, url_for)

from app.main.forms import LoginForm
from app.main.helpers import svg_contents

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
