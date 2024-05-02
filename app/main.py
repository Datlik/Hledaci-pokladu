from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/E-shop")
def e_shop():
    return render_template("e-shop.html")


@main.route("/Kontakty")
def kontakty():
    return render_template("kontakty.html")
