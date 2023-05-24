from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

@app.route("/answer", methods=["POST"])
def answer():
    data = request.get_json()
    question = data.get("question")
    context = data.get("context")
    result = qa_pipeline({"question": question, "context": context})
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)