from flask import Blueprint, flash, redirect, render_template
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
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login Requested.\n User: {form.username.data}\n"
            f"remember_me={form.remember_me.data}"
        )
        return redirect("/")
    return render_template("login.html", form=form)
