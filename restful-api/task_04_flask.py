#!/usr/bin/python3
from flask import Flask, jsonify, request
"""
Module:
A Python script that executes functions.
"""

app = Flask(__name__)


users = {
    "jane":
        {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john":
        {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route('/')
def home():
    """Returns a welcome message."""
    return "Welcome to the Flask API"


@app.route('/data')
def get_usernames():
    """Returns a list of all stored usernames."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Returns the full object corresponding to the provided username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Parses incoming JSON data and adds a new user."""
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Invalid data"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "User already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
