from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/notify", methods=["POST"])
def notify():

    data = request.json
    message = data["message"]

    print("Notification:",message)

    return jsonify({"status":"sent"})


app.run(host="0.0.0.0",port=5000)