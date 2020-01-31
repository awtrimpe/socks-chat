from flask import app

from app import create_app


def describe_app():
    def test_app(session):
        assert create_app(session)
