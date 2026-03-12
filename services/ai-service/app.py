from flask import Flask, request, jsonify, render_template
from model import predict_intent

app = Flask(__name__)

# UI page
@app.route("/")
def home():
    return render_template("index.html")

# AI API
@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()
    message = data.get("message")

    intent = predict_intent(message)

    return jsonify({"intent": intent})

# health check (for Kubernetes)
@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)