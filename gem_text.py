from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/generate/", methods=["POST"])
def generate():
    data = request.get_json()
    theme = data.get("theme", "").strip()

    if not theme:
        return jsonify({"error": "Theme is required"}), 400

    prompt = f"Write a fun, short 4-paragraph children's story about: {theme}"
    try:
        response = model.generate_content(prompt)
        return jsonify({"story": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
