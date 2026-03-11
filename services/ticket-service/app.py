from flask import Flask, request, jsonify
from db import create_ticket, get_tickets

app = Flask(__name__)

@app.route("/ticket", methods=["POST"])
def ticket():

    data = request.json
    message = data["message"]

    ticket = create_ticket(message)

    return jsonify(ticket)


@app.route("/tickets")
def tickets():

    return jsonify(get_tickets())


app.run(host="0.0.0.0",port=5000)