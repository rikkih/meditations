from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class Post(db.Model):
    """Blog Post Model for a users posts."""
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(32), nullable=False, default="MissingNo")
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Post {self.title}>"


class User(db.Model):
    """User Model for a user profile. A user will initially be able to create
    a Post on the blog page.
    """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.name}>"
