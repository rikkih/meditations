from flask import Blueprint, redirect, render_template, request, Response

from meditations.extensions import db
from meditations.posts.models import Post

blueprint = Blueprint(
    "posts",
    __name__,
    template_folder="../templates"
)


@blueprint.route("/", methods=["GET", "POST"])
@blueprint.route("/posts",  methods=["GET", "POST"])
def get_posts():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["post"]
        author = request.form["author"]
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        return redirect("/posts")
    else:
        posts = Post.query.order_by(Post.timestamp).all()
        return render_template("posts.html", posts=posts)


@blueprint.route("/posts/new", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["post"]
        author = request.form["author"]
        post = Post(title=title, content=content, author=author)
        db.session.add(post)
        db.session.commit()
        return redirect("/posts")
    else:
        return render_template("new_post.html")


@blueprint.route("/posts/edit/<int:id>", methods=["GET", "POST"])
def update_post(id: int):
    post = Post.query.get_or_404(id)
    if request.method == "POST":
        post.title = request.form["title"]
        post.author = request.form["author"]
        post.content = request.form["post"]
        db.session.commit()
        return redirect("/posts")
    else:
        return render_template("edit.html", post=post)


@blueprint.route("/posts/delete/<int:id>")
def delete_post(id: int) -> Response:
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect("/posts")
