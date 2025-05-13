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

@main.route('/pridat_nalezy')
def pridat_nalezy():
    return render_template('pridat_nalezy.html')



@main.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        files = request.files.getlist("file")

        for file in files:
            file.save(file.filename)
        return render_template("nalez.html" , name=file.filename)
