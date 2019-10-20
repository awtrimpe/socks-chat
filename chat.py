import os

from app import create_app, socketio

app = create_app(debug=True)

if __name__ == '__main__':
    if os.getenv('site_cert_path'):
        socketio.run(app, host='0.0.0.0', port=5000,
                     keyfile=os.getenv('site_cert_path')+'privkey.pem',
                     certfile=os.getenv('site_cert_path')+'cert.pem',
                     )
    else:
        socketio.run(app, host='0.0.0.0', port=5000)
