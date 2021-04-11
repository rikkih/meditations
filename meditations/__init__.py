import logging
import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev"
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError as e:
        logging.warning(f"Instance Path Initialization Error: {e}")

    @app.route("/home")
    def home():
        return "Meditations & Perspection"

    return app

