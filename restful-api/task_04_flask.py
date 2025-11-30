#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/status')
def status():
    return 'OK'

@app.route('/users/john')
def john():
    data = {
        "username": "john", 
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return data

@app.route('/details/<int:item_id>')
def details(item_id):
    if 0 <= item_id < len(data):
        return render_template('place.html', item=data[item_id])
    return "Item not found", 404

@app.route('/add_review.html')
def add_review():
    return render_template('add_review.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)