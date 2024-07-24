from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response
import pyttsx3

app = Flask(__name__)
CORS(app)


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    result = message
    def speechtx(x):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 150)
        engine.say(x)
        engine.runAndWait()
    speechtx(response)
    return jsonify(message)
    

if __name__=="__main__":
    app.run(debug=True)