from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"


@app.get("/")
def home():
    return render_template('index.html')

@app.post("/define")
def define():
    word = request.form.get("word","").strip()

    if " " in word:
        return jsonify({"error": "Only one word allowed"}), 400

    resp = requests.get(API_URL.format(word))

    if resp.status_code != 200:
        return jsonify({"error": "Word not found"}), 404

    data = resp.json()

    meaning = data[0]["meanings"][0]["definitions"][0]

    return render_template('index.html', meaning = meaning)
    


if __name__ == "__main__":
    app.run(debug=True)
