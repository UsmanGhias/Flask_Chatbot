# Flask Chatbot

This repository contains the source code for a simple chatbot API built with Flask. The chatbot utilizes a Support Vector Machine (SVM) classifier trained on TF-IDF vectorized text data to predict user intents and generate appropriate responses.

## Overview

The Flask Chatbot API offers a simple interface for interacting with the chatbot. Users can send messages to the API, which then predicts the intent of the message and generates a response accordingly. The chatbot is designed to provide support and assistance related to mental health topics.

## Features

- **Predict Intent**: Given a user message, the chatbot predicts the intent of the message.
- **Generate Response**: Based on the predicted intent, the chatbot generates an appropriate response.
- **Simple API Interface**: The API is easy to integrate into web applications or other systems for seamless interaction.

## Installation

To run the Flask Chatbot API locally, follow these steps:

1. Clone this repository:

```bash
git clone https://github.com/UsmanGhias/flask_chatbot.git
```

2. Navigate to the project directory:

```bash
cd flask_chatbot
```

3. Install dependencies using pip:

```bash
pip install -r requirements.txt
```

4. Run the Flask application:

```bash
python app.py
```

## Usage

Once the Flask application is running, you can interact with the chatbot API by sending HTTP POST requests to the `/predict` endpoint. Include a JSON object with a `message` field containing the user message to receive a response from the chatbot.

Example usage with cURL:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello"}' http://localhost:5000/predict
```

## Deployment

To deploy the Flask Chatbot API to a production environment, follow these general steps:

1. Choose a hosting provider such as Heroku, AWS, or Google Cloud Platform.
2. Set up a server instance and ensure it meets the system requirements.
3. Clone the repository onto the server.
4. Install dependencies using pip.
5. Configure environment variables for any sensitive information.
6. Run the Flask application using a production-grade WSGI server like Gunicorn.

## Contributing

Contributions to the Flask Chatbot project are welcome! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure they adhere to the project's coding standards.
4. Test your changes thoroughly.
5. Commit your changes with clear and descriptive commit messages.
6. Push your changes to your fork.
7. Create a pull request against the `main` branch of the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to [OpenAI](https://openai.com) for providing the GPT-based language model used for generating responses in the chatbot.

