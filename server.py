# server.py

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from chatbot import get_chatbot_reply

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/chat")
def chat():
    return render_template("index.html")

@socketio.on("user_message")
def handle_user_message(message):
    print(f"User: {message}")
    reply = get_chatbot_reply(message)
    emit("bot_reply", reply)

if __name__ == "__main__":
    socketio.run(app, debug=True)
