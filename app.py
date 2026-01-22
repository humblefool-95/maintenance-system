from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ---------------- LOGIN ----------------

@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_action():
    email = request.form.get("email")
    password = request.form.get("password")

    if email and password:
        return redirect(url_for("dashboard"))
    else:
        return "Login failed"


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():
    return render_template("Index.html")


# ---------------- MODULE ROUTES ----------------

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


# ---------------- HEALTH CHECK ----------------

@app.route("/health")
def health():
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
