from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/Onas")
def onas():
    return render_template("onas.html")


@main.route("/Kontakty")
def kontakty():
    return render_template("kontakty.html")


@main.route("/Nálezy")
def nalezy():
    return render_template("nalezy.html")

@main.route("/Přidat nálezy")
def pridat_nalezy():
    return render_template("pridat_nalezy.html")
