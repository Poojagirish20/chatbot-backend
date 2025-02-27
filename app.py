from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Set your OpenAI API key (replace "your-api-key" with your actual key)
openai.api_key = "your-api-key"

# Function to generate a response using OpenAI API
def get_chatbot_response(question):
    prompt = f"Answer the following question based on Segment, mParticle, Lytics, or Zeotap documentation:\n\n{question}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=300
    )
    
    return response["choices"][0]["message"]["content"].strip()

# API Endpoint to handle user questions
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_question = data.get("question")
    
    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    answer = get_chatbot_response(user_question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
