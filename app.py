import os
from flask import Flask
app = Flask(__name__)

messages = []


def add_message(username, message):
    messages.append("{0}: {1}".format(username, message))


@app.route('/')
def index():
    """ main page with instructions """
    return "To send a message use /username/message"


@app.route('/<username>')
def user(username):
    """ Display username in app in the chat page"""
    return "Welcome, {0} ".format(username, messages)


@app.route('/<username>/<message>')
def send_message(username, message):
    """ Create a new message and redirect back to the chat page"""
    return "{0}: {1}".format(username, message)


app.run(debug=True)
