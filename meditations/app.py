from meditations import create_app
from meditations.config import Config
from meditations.models import db, migrate, Post, User

app = create_app(Config)


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Post": Post,
        "User": User
    }
