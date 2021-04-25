from flask import Blueprint, redirect, render_template

from meditations.models import Post

blueprint = Blueprint(
    "meditations",
    __name__,
    template_folder="templates",
    url_prefix="/"
)


@blueprint.route("/")
@blueprint.route("/home")
def landing_page():
    return render_template("index.html")


@blueprint.route("/posts/new", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["post"]
        author = request.form["author"]
        post = Post(title=title, content=content, author=author)
        db.add(post)
        db.commit()
        return redirect("/posts")
    else:
        return render_template("new_post.html")
