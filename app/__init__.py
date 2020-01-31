import os
import sys

from flask import Flask, g
from flask_login import LoginManager
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app(get_session, debug=False):
    '''Create an application.'''
    app = Flask(__name__)
    # login_manager = LoginManager()
    # login_manager.init_app(app)
    app.debug = debug

    @app.before_request
    def inject_session():
        with get_session() as session:
            g.session = session

    if 'pytest' in sys.modules:
        app.config['WTF_CSRF_ENABLED'] = False
    app.config['SECRET_KEY'] = os.getenv('secret_key')

    from app.main.routes.routes import bp as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app
