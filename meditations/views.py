from flask import Blueprint, render_template

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