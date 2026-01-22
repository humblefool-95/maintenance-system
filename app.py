from flask import Flask, render_template
import os

# -----------------------------
# FLASK APP INITIALIZATION
# -----------------------------

app = Flask(__name__)

# -----------------------------
# ROUTES (HTML PAGE SERVING)
# -----------------------------

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("index.html")


@app.route("/train")
def train_info():
    return render_template("Train_Information.html")


@app.route("/jobcard")
def job_card():
    return render_template("Raise_Jobcard.html")


@app.route("/powerblock")
def power_block():
    return render_template("Power Block Certificate & Record.html")


@app.route("/records")
def records():
    return render_template("records.html")


# -----------------------------
# HEALTH CHECK (OPTIONAL)
# -----------------------------

@app.route("/health")
def health():
    return {"status": "running"}


# -----------------------------
# MAIN SERVER START
# -----------------------------

if __name__ == "__main__":

    # Render automatically assigns PORT
    port = int(os.environ.get("PORT", 5000))

    print("====================================")
    print(" Maintenance System Server Started ")
    print("====================================")
    print(f" Running on port: {port}")
    print("====================================")

    app.run(
        host="0.0.0.0",
        port=port
    )
