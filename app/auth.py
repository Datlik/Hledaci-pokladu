from flask import Blueprint, render_template, request, redirect, url_for, session, flash

auth = Blueprint("auth", __name__)

users = {
    "admin":"admin",
    "jakub":"jakub"
}

@auth.route("/Přihlášení", methods=["POST", "GET"])
def prihlaseni():
    error = None
    #jestliže je POST získá hodnoty z formuláře
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        #kontrola zadání hesla a jména v případě zadání mezery
        if username.strip()=="" or password.strip()=="":
            flash("Jméno nebo heslo není zadáno")
            return redirect(url_for("auth.prihlaseni"))
        
        #uložení jména do session
        if  username in users and users[username] == password:
            session["username"] = username
            flash("Jste úspěšně přihlášen")
            return redirect(url_for("auth.profil"))
        else:
            error = "Neznámé uživatelské jméno nebo heslo."
            return render_template("prihlaseni.html", error=error)
    else:
        #jestliže je uživatel v session je přihlášený 
        if "username" in session:
            flash("Už jste přihlášený")  
        else:
            return render_template("prihlaseni.html")
