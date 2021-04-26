from flask import Blueprint, redirect, render_template, request

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


@blueprint.route("/posts",  methods=["GET", "POST"])
def get_posts():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['post']
        author = request.form['author']
        post = Post(title=title, content=content, author=author)
        db.add(post)
        db.commit()
        return redirect('/posts')
    else:
        posts = Post.query.order_by(Post.date).all()
        return render_template('posts.html', posts=posts)


@blueprint.route("/posts/edit/<int:id>", methods=["GET", "POST"])
def update_post(id):
    post = Post.query.get_or_404(id)
    if request.method == "POST":
        post.title = request.form["title"]
        post.author = request.form["author"]
        post.content = request.form["post"]
        db.commit()
        return redirect("/posts")
    else:
        return render_template("edit.html", post=post)
