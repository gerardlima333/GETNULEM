# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    from .app import app_bp
    app.register_blueprint(app_bp)

    return app
