import logging
import os

from flask import Flask, render_template

from meditations.config import Config
from meditations.models import db, Post


def create_app() -> Flask:
    """Application Factory for the Flask.application instance."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    db.init_app(app)

    try:
        os.makedirs(app.instance_path)
    except OSError as e:
        logging.warning(f"Instance Path Initialization Error: {e}")

    @app.route("/home")
    def home():
        return render_template("index.html")

    return app
