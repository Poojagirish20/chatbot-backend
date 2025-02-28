from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Corrected Route
@app.route("/")
def home():
    return "Flask server is running!"

@app.route("/chatbot", methods=["POST"])
def chatbot():
    return jsonify({"message": "Chatbot response placeholder"})

if __name__ == "__main__":
    app.run(debug=True)
