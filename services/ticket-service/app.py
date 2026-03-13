from flask import Flask, request, jsonify, render_template
from db import create_ticket, get_tickets

app = Flask(__name__)

# UI Dashboard
@app.route("/")
def home():
    return render_template("index.html")


# Create ticket API
@app.route("/ticket", methods=["POST"])
def ticket():

    data = request.get_json()

    user = data.get("user")
    message = data.get("message")
    intent = data.get("intent")

    ticket = create_ticket(user, message, intent)

    return jsonify(ticket)


# Get all tickets API
@app.route("/tickets")
def tickets():

    data = get_tickets()

    return jsonify(data)


# Health check for Kubernetes
@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)