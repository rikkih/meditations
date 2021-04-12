import datetime

from db import db


class Post(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    posted_by = db.Column(db.String(32), nullable=False, default="MissingNo")
    posted_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
