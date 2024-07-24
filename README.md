Chatbot Project
This project implements a simple chatbot using Python and a standalone frontend.

Project Structure
chatbot_project/
│
├── chatbot/
│   ├── app.py
│   ├── chat.py
│   ├── data.pth
│   ├── intents.json
│   ├── model.py
│   ├── nltk_utils.py
│   ├── train.py
│   ├── .vscode/settings.json
│   ├── __pycache__/
│   ├── report/
│   └── standalone-frontend/
│
├── static/
│   ├── app.js
│   ├── style.css
│   └── images/chatbox-icon.svg
Files and Directories
app.py: Main application script.
chat.py: Contains the chatbot logic.
data.pth: Model data file.
intents.json: Training data for the chatbot.
model.py: Defines the neural network model.
nltk_utils.py: Utility functions for NLP processing.
train.py: Script to train the model.
.vscode/settings.json: Visual Studio Code settings.
pycache/: Directory for cached Python files.
report/: Contains various documents and images related to the project.
standalone-frontend/: Contains frontend assets for the standalone chatbot.


Here are the libraries that need to be installed based on the imports found in your Python files:

Flask - for creating the web application.
flask_cors - for handling Cross-Origin Resource Sharing (CORS) in Flask.
pyttsx3 - for text-to-speech conversion.
torch (PyTorch) - for building and training the neural network model.
nltk - for natural language processing utilities.

Frontend
The standalone frontend is located in the standalone-frontend directory. It includes HTML, CSS, and JavaScript files for the chatbot interface.
