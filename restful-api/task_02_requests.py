#!/usr/bin/python3
"""
Module : A Python file that runs functions.
http : A library used for web functions.
server : A module used for basic web server.
json : A module used to convert data.
"""
import http.server
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)


def fetch_and_print_posts():
    """
    Parse the fetched data into a JSON object.
    """
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(response.json())
    

def fetch_and_save_posts():
    """
    Structure the data into a list of dictionaries, where each dictionary
    represents a post with keys and values for id, title, and body
    """
    response = requests.get(url)
    posts = response.json()
    structured_posts = [
        {"id": post["id"], "title": post["title"], "body": post["body"]}
        for post in posts[:5]
    ]
    with open("posts.csv", "w", encoding="utf-8") as f:
        json.dump(structured_posts, f, indent=4, ensure_ascii=False)
