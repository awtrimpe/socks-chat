import os
import sys

from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    if "pytest" in sys.modules:
        app.config['WTF_CSRF_ENABLED'] = False
    app.config['SECRET_KEY'] = os.getenv('secret_key')

    from app.main.routes.routes import bp as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app
