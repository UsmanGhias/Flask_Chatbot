from flask import Flask, request, jsonify
import joblib
import random
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

# Globals to hold the model and vectorizer
vectorizer = None
model = None
responses = {}

def load_model_and_responses():
    global vectorizer, model, responses
    # Load the trained model and vectorizer
    vectorizer = joblib.load('vectorizer.pkl')
    model = joblib.load('model.pkl')

    # Load responses dictionary
    # It's assumed you have a structured way to load these responses that align with your intents
    # Example: Load responses from a JSON file or a Python dictionary here
    import json
    with open('intents.json', 'r') as f:
        data = json.load(f)
        for item in data['intents']:
            responses[item['tag']] = item['responses']

@app.route('/')
def home():
    return "Welcome to the Mental Health Chatbot API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    message = data['message']
    message_vec = vectorizer.transform([message])
    intent = model.predict(message_vec)[0]
    
    # Fetch a suitable response for the predicted intent
    if intent in responses:
        response = random.choice(responses[intent])
    else:
        response = "I'm not sure how to respond to that."

    return jsonify({"intent": intent, "response": response})

if __name__ == "__main__":
    load_model_and_responses()
    app.run(debug=True)

