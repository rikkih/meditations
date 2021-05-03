import os
from uuid import uuid4


class Config:
    """Default Config for running the application locally."""
    SECRET_KEY = os.getenv("SECRET_KEY") or str(uuid4())
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
