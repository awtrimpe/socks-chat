from flask import app

from app import create_app


def describe_app():
    def test_app():
        assert create_app()
