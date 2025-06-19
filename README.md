💬 Vanisha's ChatGPT WebSocket Bot
A real-time AI chatbot built using Flask, Flask-SocketIO, and OpenAI's GPT-3.5-turbo. This bot communicates over WebSockets for low-latency messaging and provides a responsive front-end powered by HTML, CSS, and Socket.IO.

🚀 Features
🧠 ChatGPT-3.5 integration (via OpenAI API)

🌐 Real-time messaging with WebSockets (Socket.IO)

💻 Modern HTML/CSS front-end UI

👋 Landing page with "Start Chat" button

🔒 API key hidden using .env file

✅ Clean structure & beginner-friendly code

📂 Folder Structure
bash
Copy code
chatgpt-websocket-bot/
│
├── server.py              # Flask + WebSocket server
├── chatbot.py             # OpenAI GPT logic
├── .env                   # Stores API key (NOT pushed)
├── .gitignore             # Prevents .env and pycache from uploading
├── requirements.txt       # All required Python libraries
├── README.md              # This file
└── templates/
    ├── welcome.html       # Landing page
    └── index.html         # Chatbot UI