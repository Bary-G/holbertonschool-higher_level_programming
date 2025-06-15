#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
"""
Module:
A Python script that protects access to a data, by using an API.
"""

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['SECRET_KEY'] = 'your_secret_key'

users = {
    "alice": {"password": generate_password_hash("securepassword123"), "role": "admin"},
    "bob": {"password": generate_password_hash("mypassword456"), "role": "user"},
    "bud": {"password": generate_password_hash("mypassword654"), "role": "user"}
}

@auth.verify_password
def verify_password(username, password):
    """
    Verify the password.
    """
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Show a message from a protected route if authenticated.
    """
    return jsonify({"message": "Basic Auth: Access Granted"})

@app.route('/jwt-protected')
def jwt_protected():
    """
    Show a message from a protected route if authenticated.
    """
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Unauthorized"}), 401
    
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return jsonify({"message": "JWT Auth: Access Granted"})
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

@app.route('/login', methods=['POST'])
def login():
    """
    Requests authentication.
    """
    auth_data = request.json
    username = auth_data.get("username")
    password = auth_data.get("password")
    
    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 400
    
    if username in users and check_password_hash(users[username]["password"], password):
        token = jwt.encode({'username': username, 'role': users[username]["role"], 
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
                            app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({"token": token})
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/admin-only')
def admin_only():
    """
    Show a message from a protected route if authenticated.
    """
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Unauthorized"}), 401
    
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        if data['role'] != 'admin':
            return jsonify({"error": "Admin access required"}), 403
        return jsonify({"message": "Admin Access: Granted"})
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
