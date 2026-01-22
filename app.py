from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from supabase import create_client
import os

# -------------------------
# SUPABASE CONFIG
# -------------------------

SUPABASE_URL = "https://cyaxvuwkwptaxbkpwyid.supabase.co"
SUPABASE_KEY = "sb_publishable_wshxDs-Q_gUgYXxVjw7bwA_ycY3kndA"   # paste anon public key here

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# -------------------------
# FLASK CONFIG
# -------------------------

app = Flask(__name__)
app.secret_key = "maintenance-secret-key"   # can be anything


# -------------------------
# HOME → LOGIN PAGE
# -------------------------

@app.route("/")
def home():
    return render_template("login.html")


# -------------------------
# SIGNUP ROUTE
# -------------------------

@app.route("/signup", methods=["POST"])
def signup():

    email = request.form.get("email")
    password = request.form.get("password")

    try:
        res = supabase.auth.sign_up({
            "email": email,
            "password": password
        })

        return jsonify({"status": "success", "message": "Account created. Please check email for confirmation."})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


# -------------------------
# LOGIN ROUTE
# -------------------------

@app.route("/login", methods=["POST"])
def login():

    email = request.form.get("email")
    password = request.form.get("password")

    try:
        res = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        session["user"] = res.user.id
        session["email"] = email

        return redirect("/dashboard")

    except Exception as e:
        return render_template("login.html", error="Login failed: Email not confirmed or wrong credentials")


# -------------------------
# DASHBOARD
# -------------------------

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    return render_template("Index.html")


# -------------------------
# LOGOUT
# -------------------------

@app.route("/logout")
def logout():

    session.clear()
    return redirect("/")


# -------------------------
# TRAIN INFO PAGE
# -------------------------

@app.route("/train")
def train():

    if "user" not in session:
        return redirect("/")

    return render_template("Train_Information.html")


# -------------------------
# JOB CARD PAGE
# -------------------------

@app.route("/jobcard")
def jobcard():

    if "user" not in session:
        return redirect("/")

    return render_template("Raise_Jobcard.html")


# -------------------------
# POWER BLOCK PAGE
# -------------------------

@app.route("/powerblock")
def powerblock():

    if "user" not in session:
        return redirect("/")

    return render_template("Power Block Certificate & Record.html")


# -------------------------
# SERVER START
# -------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


