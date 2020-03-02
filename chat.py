import os
import sys

from app import create_app, socketio
from app.main.database import create_tables, engine, get_session

create_tables(engine)
app = create_app(get_session)


def main():
    if os.getenv('site_cert_path'):
        socketio.run(app, host='0.0.0.0', port=5000,
                     keyfile=os.getenv('site_cert_path') + 'privkey.pem',
                     certfile=os.getenv('site_cert_path') + 'cert.pem',
                     )
    else:
        socketio.run(app, host='0.0.0.0', port=5000)


def init():
    if __name__ == '__main__':
        sys.exit(main())


init()
