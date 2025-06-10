#!/usr/bin/python3
import requests
import csv
import http.server
import socketserver
"""
Module:
A Python script that runs functions.
"""


PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints only the titles.
    """
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        json_data = response.json()
        # Print only the titles of the first few posts
        for post in json_data[:7]:  # Limiting to first 7 posts
            print(post["title"])
    else:
        print("Failed to fetch posts")


def fetch_and_save_posts():
    """
    Fetches and saves all post from JSONPlaceholder.
    """
    json_data = fetch_and_print_posts()
    if json_data:
        structured_data = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in json_data]
        with open("posts.csv", mode="w", newline="", encoding="UTF8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_data)
        print("Data saved to posts.csv")
