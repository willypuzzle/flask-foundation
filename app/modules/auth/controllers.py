from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

# Import module forms
from app.modules.auth.forms import LoginForm
# Import module models (i.e. User)
from app.modules.auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod = Blueprint('auth', __name__, url_prefix='/auth')


@mod.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user)

        flash("Logged in successfully.", "success")
        return redirect(request.args.get("next") or url_for("home.home"))

    return render_template("auth/login.html", form=form)


@mod.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "success")

    return redirect(url_for("home.home"))


@mod.route("/restricted")
@login_required
def restricted():
    return "You can only see this if you are logged in!", 200
