from flask import Flask, Blueprint, render_template, url_for

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("index.html")
