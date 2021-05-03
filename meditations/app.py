from meditations import auth, create_app, db, posts
from meditations.config import Config

app = create_app(Config)


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Post": posts.models.Post,
        "User": auth.models.User
    }
