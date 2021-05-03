import logging
import os

from flask import Flask, render_template

from meditations import auth, posts
from meditations.config import Config
from meditations.extensions import db, login_manager, migrate


def create_app(config: Config) -> Flask:
    """Application Factory for the Flask instance."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)

    with app.app_context():
        db.create_all()

    try:
        os.makedirs(app.instance_path)
    except OSError as e:
        logging.warning(f"Instance Path Initialization Error: {e}")

    return app


def register_blueprints(app: Flask) -> None:
    """Registers blueprint configuration for application routes."""
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(posts.views.blueprint)


def register_extensions(app: Flask) -> None:
    """Handles the registering of the Flask extension packages"""
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
