from flask import Blueprint
from flask_login import current_user

blueprint = Blueprint(
    "auth",
    __name__,
    template_folder="../templates",
    url_prefix="/auth")


@blueprint.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("posts"))
