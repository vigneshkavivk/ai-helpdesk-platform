from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# mock database
users = {
    "admin": "password123",
    "devops": "cloud123"
}

@app.route("/")
def home():
    if "user" in session:
        return f"<h2>Welcome {session['user']} 👋</h2><a href='/logout'>Logout</a>"
    return redirect(url_for("login_page"))

# UI login page
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        session["user"] = username
        return jsonify({"status":"success","user":username})

    return jsonify({"status":"failed"}),401

# API login endpoint
@app.route("/api/login", methods=["POST"])
def login():

    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        session["user"] = username
        return jsonify({"status": "success", "user": username})

    return jsonify({"status": "failed"}), 401

# logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login_page"))

# health check for Kubernetes
@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
