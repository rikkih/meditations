from flask import current_app, g

from .extensions import db


def get_db():
    """Helper to get a connection from the database pool.

    TODO: Use a flask.before_application_context function and handle the
    database connection here. Return the connection to the pool at the end of
    the request.
    """
    pass
