import os
from datetime import datetime
from flask import Flask, redirect
app = Flask(__name__)

messages = []


def add_messages(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username, message))


def get_all_messages():
    """Get all messages and add them to the messages list each on a new line."""
    return "<br>".join(messages)


@app.route('/')
def index():
    """ main page with instructions """
    return "To send a message use /username/message"


@app.route('/<username>')
def user(username):
    """ Display username in app in the chat page"""
    return "<h1>Welcome, {0}</h1> {1}". format(username, get_all_messages())


@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)


app.run(debug=True)
