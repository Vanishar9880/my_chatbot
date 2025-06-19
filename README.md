# Vanisha's ChatGPT WebSocket Chatbot

This project is a real-time AI chatbot built using Python, Flask, and WebSockets (Socket.IO). It uses OpenAI’s GPT-3.5 language model to generate intelligent and context-aware responses. The chatbot runs on a Flask server and communicates with the front end over WebSockets to provide instant, low-latency messaging.

## Features

- Built using Flask and Flask-SocketIO
- Real-time communication using WebSockets
- Integration with OpenAI GPT-3.5 for responses
- Modern and simple front-end with HTML, CSS, and JavaScript
- Landing page and chat UI included
- Environment variables used for API key (kept secure)

## Project Structure

my_chatbot/
│
├── server.py # Flask + WebSocket server
├── chatbot.py # GPT-3.5 interaction logic
├── requirements.txt # List of required libraries
├── .env # Stores the OpenAI API key (excluded from GitHub)
├── .gitignore # Specifies files to ignore
├── README.md # Project description and setup guide
└── templates/
├── welcome.html # Landing page
└── index.html # Main chat interface



## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/Vanishar9880/my_chatbot.git
   cd my_chatbot

2.Install dependencies:

pip install -r requirements.txt

3.Create a .env file in the root folder and add your OpenAI key:

OPENAI_API_KEY=your-key-here

4.Run the chatbot:

python server.py
Then open your browser and go to http://localhost:5000

##Notes
This project is for learning and demonstration purposes.

API keys are managed through a .env file and excluded from Git using .gitignore.

Built By
Vanisha Rathore
2nd Year ECE, NSUT
WebSocket | Flask | GPT-3.5 | HTML/CSS