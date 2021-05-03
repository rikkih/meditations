from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    Response,
    url_for
)

from meditations.extensions import db
from meditations.posts.models import Post

blueprint = Blueprint("posts", __name__, template_folder="../templates")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["post"]
        author = request.form["author"]
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("posts.home"))
    else:
        posts = Post.query.order_by(Post.timestamp).all()
        return render_template("posts.html", posts=posts)


@blueprint.route("/posts/new", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["post"]
        author = request.form["author"]
        post = Post(title=title, content=content, author=author)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("posts.home"))
    else:
        return render_template("new_post.html")


@blueprint.route("/posts/edit/<int:id>", methods=["GET", "POST"])
def update(id: int):
    post = Post.query.get_or_404(id)
    if request.method == "POST":
        post.title = request.form["title"]
        post.author = request.form["author"]
        post.content = request.form["post"]
        db.session.commit()
        return redirect(url_for("posts.home"))
    else:
        return render_template("edit.html", post=post)


@blueprint.route("/posts/delete/<int:id>")
def delete(id: int) -> Response:
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("posts.home"))
