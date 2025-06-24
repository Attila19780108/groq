from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
GROQ_API_KEY = "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"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")

    if not user_msg:
        return jsonify({"error": "Nincs üzenet megadva."}), 400

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/llama-4-scout-17b-16e-instruct",
                "messages": [{"role": "user", "content": user_msg}]
            }
        )
        answer = response.json()["choices"][0]["message"]["content"]
        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
