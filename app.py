from flask import Flask, render_template, request, redirect, url_for, flash
from auth import register_user, check_login

app = Flask(__name__)
#Questa riga imposta una chiave segreta usata da Flask per proteggere i dati di sessione e firmare i messaggi flash (in modo che non possano essere manipolati dal client)
app.secret_key = "chiavesegreta"  

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if register_user(username, password):
            flash("Registrazione avvenuta con successo!", "success")
            return redirect(url_for("login"))
        else:
            flash("Utente già registrato", "danger")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if check_login(username, password):
            flash(f"Benvenuto, {username}!", "success")
        else:
            flash("Credenziali errate", "danger")
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
