from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import json

auth = Blueprint("auth", __name__)


@auth.route("/Přihlášení", methods=["POST", "GET"])
def prihlaseni():
    error = None
    #jestliže je POST získá hodnoty z formuláře
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        with open("app/static/data/users.json", "r") as file:
            users = json.load(file)
            
        #kontrola zadání hesla a jména v případě zadání mezery
        if username.strip()=="" or password.strip()=="":
            flash("Jméno nebo heslo není zadáno")
            return redirect(url_for("auth.prihlaseni"))
        
        #uložení jména do session
        for user in users:
            if user["username"] == username and user["password"] == password:
                session["username"] = username
                flash("Byl jste úspěšně přihlášen")
                return redirect(url_for("auth.profil"))
        error = "Neznámé uživatelské jméno nebo heslo."
        return render_template("prihlaseni.html", error=error)
    else:
        #jestliže je uživatel v session je přihlášený 
        if "username" in session:
            flash("Už jste přihlášený")  
            return redirect(url_for("auth.profil"))
        else:
            return render_template("prihlaseni.html")


@auth.route("/registrace", methods=["GET", "POST"])
def registrace():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        with open("app/static/data/users.json", "r") as file:
            users = json.load(file)
    
        for user in users:
            if user["username"] == username:
                flash("Uživatelské jméno již existuje.")
                return render_template("registrace.html")
        
        new_user = {"username": username, "password": password}

        with open("app/static/data/users.json", "w") as file:
            users.append(new_user)
            json.dump(users, file, indent=4)

        flash("Registrace proběhla úspěšně. Nyní se můžete přihlásit.")
        return redirect(url_for("auth.prihlaseni"))
        
    return render_template("registrace.html")


@auth.route("/Profil")
def profil():
    #kontrola jestli je uživatel v session
    if "username" in session:
        username = session["username"]
        return render_template("profil.html", username=username)
    else:
        flash("Nejste přihlášený")
        return redirect(url_for("auth.prihlaseni"))


@auth.route("/Odhlášení")
def odhlaseni():
    #pokud je uživatel přihlášen, získá se  jeho uživatelské jméno
    if "username" in session:
        username = session["username"]
        flash(f"Byl jste úspěšně odhlášen {username}")
    #odstranění uživatele ze session
    session.pop("username", None)
    return redirect(url_for("auth.prihlaseni"))

@auth.route("/smazani")
def smazani():
    #načtení uživatelů ze souborů users.json
    with open("app/static/data/users.json", "r") as file:
        users = json.load(file)

    #pokud je aktuální uživatel v users.json vymaže ho
    for user in users:
        if session["username"] == user["username"]:
            users.remove(user)
            break

    with open("app/static/data/users.json", "w", encoding="utf-8") as file:
        json.dump(users, file)

    session.pop("username")
    return redirect(url_for("main.index"))

@auth.route("/send_message", methods=["POST"])
def send_message():
    sender = session["username"]
    recipient = request.form.get("recipient")
    content = request.form.get("message")

    if not recipient or not content:
        flash("Příjemce a zpráva musí být vyplněny")
        return redirect(url_for("auth.profil"))

    # Načtěte uživatele a přidejte zprávu do jejich zpráv
    with open("app/static/data/users.json", "r") as file:
        users = json.load(file)

    for user in users:
        if user["username"] == recipient:
            if "messages" not in user:
                user["messages"] = []
            user["messages"].append({"sender": sender, "content": content})
            break

    with open("app/static/data/users.json", "w") as file:
        json.dump(users, file, indent=4)

    flash("Zpráva byla odeslána")
    return redirect(url_for("auth.profil"))
