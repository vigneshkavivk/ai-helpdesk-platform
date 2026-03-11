from flask import Flask, request, jsonify
from model import predict_intent

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json
    message = data["message"]

    intent = predict_intent(message)

    return jsonify({"intent":intent})


@app.route("/health")
def health():
    return "ok"


app.run(host="0.0.0.0",port=5000)