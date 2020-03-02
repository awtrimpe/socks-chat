import os
from unittest.mock import patch

import pytest

from app import socketio
from app.main.database import get_session


def describe_chat():
    def test_chat():
        import chat
        chat.app = 'mock_create_app'
        with patch.object(socketio, 'run') as socket_mock:
            with patch.object(chat, '__name__', '__main__'):
                with patch.object(chat.sys, 'exit') as mock_exit:
                    chat.init()
                    socket_mock.assert_called_with(
                        chat.app, host='0.0.0.0', port=5000)

    def test_chat_certificate():
        import chat
        chat.app = 'mock_create_app'
        with patch.dict(os.environ, {'site_cert_path': 'a/fake/path/'}):
            with patch.object(socketio, 'run') as socket_mock:
                with patch.object(chat, '__name__', '__main__'):
                    with patch.object(chat.sys, 'exit'):
                        chat.init()
                        socket_mock.assert_called_with(
                            chat.app, host='0.0.0.0', port=5000, keyfile='a/fake/path/privkey.pem', certfile='a/fake/path/cert.pem')
