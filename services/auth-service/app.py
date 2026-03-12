from flask import Flask, request, jsonify, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

# mock database
users = {
    "admin": "password123",
    "devops": "cloud123"
}

# Home page
@app.route("/")
def home():
    if "user" in session:
        return f"<h2>Welcome {session['user']} 👋</h2><a href='/logout'>Logout</a>"
    return redirect(url_for("login_page"))

# Login UI page
@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

# API login endpoint
@app.route("/api/login", methods=["POST"])
def api_login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        session["user"] = username
        return jsonify({"status":"success","user":username})

    return jsonify({"status":"failed"}),401


# logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


# health check
@app.route("/health")
def health():
    return jsonify({"status":"ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)