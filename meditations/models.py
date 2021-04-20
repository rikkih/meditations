from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Post(db.model):
    """Blog Post Model for a users posts. This is initially linked to a
    string, but a backref to a user will be added later.
    """
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(32), nullable=False, default="MissingNo")
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return self.title
