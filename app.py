from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"


@app.get("/define/<word>")
def define(word):
    word = word.strip()

    if " " in word:
        return jsonify({"error": "Only one word allowed"}), 400

    resp = requests.get(API_URL.format(word))

    if resp.status_code != 200:
        return jsonify({"error": "Word not found"}), 404

    data = resp.json()

    meaning = data[0]["meanings"][0]["definitions"][0]

    return jsonify({
        "word": data[0]["word"],
        "part_of_speech": data[0]["meanings"][0]["partOfSpeech"],
        "definition": meaning.get("definition"),
        "example": meaning.get("example"),
    })


if __name__ == "__main__":
    app.run(debug=True)
