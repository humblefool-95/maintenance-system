from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ---------------- HOME / LOGIN ----------------

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    # TEMP SIMPLE LOGIN (for testing)
    if email and password:
        return redirect(url_for("dashboard"))
    else:
        return "Login Failed"


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():
    return render_template("Index.html")


# ---------------- MODULE PAGES ----------------

@app.route("/train")
def train():
    return render_template("Train_Information.html")


@app.route("/powerblock")
def powerblock():
    return render_template("Power Block Certificate & Record.html")


@app.route("/jobcard")
def jobcard():
    return render_template("Raise_Jobcard.html")


@app.route("/records")
def records():
    return render_template("records.html")


# ---------------- RUN LOCAL ----------------

if __name__ == "__main__":
    app.run(debug=True)
