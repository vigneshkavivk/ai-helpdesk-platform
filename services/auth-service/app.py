from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "admin":"password123"
}

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]

    if username in users and users[username] == password:
        return jsonify({"status":"success"})
    else:
        return jsonify({"status":"failed"}),401


@app.route("/health")
def health():
    return "ok"


app.run(host="0.0.0.0",port=5000)