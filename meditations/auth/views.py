from flask import Blueprint, render_template
from flask_login import current_user, login_user

from meditations.auth.forms import LoginForm
from meditations.auth.models import User

blueprint = Blueprint(
    "auth",
    __name__,
    template_folder="../templates",
    url_prefix="/auth")


@blueprint.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html", form=LoginForm())
