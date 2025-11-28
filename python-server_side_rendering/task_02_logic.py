#!/usr/bin/env python3
"""
Module: Create a basic Flask app that serves a web page using a Jinja template.
"""
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return render_template('items.html', items=data["items"])

if __name__ == '__main__':
    app.run(debug=True, port=5000)