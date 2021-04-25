import logging
import os

from flask import Flask, render_template

from meditations.config import Config
from meditations.models import db
from meditations import views


def create_app() -> Flask:
    """Application Factory for the Flask.application instance."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(views.blueprint)

    with app.app_context():
        db.create_all()

    try:
        os.makedirs(app.instance_path)
    except OSError as e:
        logging.warning(f"Instance Path Initialization Error: {e}")

    return app
