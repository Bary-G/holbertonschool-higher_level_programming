#!/usr/bin/python3
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
"""
Module:
A Python script that protects access to a data, by using an API.
"""


app = Flask(__name__)
auth = HTTPBasicAuth()


users = {
    "alice": generate_password_hash("securepassword123"),
    "bob": generate_password_hash("mypassword456"),
    "bud": generate_password_hash("mypassword654"),
}

@auth.verify_password
def verify_password(username, password):
    """
    Verify the password.
    """
    if username in users and check_password_hash(users[username], password):
        return username
    return None

@app.route('/protected')
@auth.login_required
def protected():
    """
    Show a message from a protected route if authenticated.
    """
    return jsonify({"message": f"Hello, {auth.current_user()}! You have accessed a protected route."})

@app.route('/')
def public():
    """
    Show a message from a public route without authentication.
    """
    return jsonify({"message": "This is a public route. No authentication required."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
