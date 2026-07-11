#!/usr/bin/python3
"""
This module fetches posts from the JSONPlaceholder API using the
`requests` library, then prints or saves the retrieved data.
"""
import csv
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print the response
    status code. If the request succeeded (status code 200), parse
    the JSON body and print the title of every post.
    """
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder. If the request succeeded,
    structure the data into a list of dictionaries (id, title, body)
    and write it to a CSV file named 'posts.csv'.
    """
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()
        posts_data = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"],
            }
            for post in posts
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_data)
