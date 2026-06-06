from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

print("KEY =", os.getenv("GEMINI_API_KEY"))

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")

    try:
        response = model.generate_content(user_message)

        print("SUCCESS:", response.text)

        return jsonify({
            "reply": response.text
        })

    except Exception as e:
        import traceback

        traceback.print_exc()

        print("FULL ERROR:", repr(e))

        return jsonify({
            "reply": f"Error: {str(e)}"
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
