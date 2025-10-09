#!/usr/bin/python3
"""
Module : A Python file that runs functions.
http : A library used for web functions.
server : A module used for basic web server.
csv : A module used to convert data.
"""
import http.server
import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)


def fetch_and_print_posts():
    """
    Parse the fetched data into a JSON object.
    """
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        posts = response.json()
        for post in posts:
            print(post["title"])
    except Exception:
        print(f"Status Code: {response.status_code}")
    

def fetch_and_save_posts():
    """
    Structure the data into a list of dictionaries, where each dictionary
    represents a post with keys and values for id, title, and body
    """
    try:
        response = requests.get(url)
        posts = response.json()
        filtered_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]
        with open("posts.csv", "w", encoding="utf-8", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(filtered_posts)
    except Exception:
        print("An exception occured")
