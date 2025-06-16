#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    """Fetch posts and print status code and titles"""
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        response.raise_for_status()

        posts = response.json()
        for post in posts:
            print(post.get("title"))

    except requests.RequestException:
        print("Fetch fail")


def fetch_and_save_posts():
    """Fetch posts and save selected fields into a CSV"""
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url)
		if response.status_code != 200:
			print("Fetch fail")
			return

        posts = response.json()
        data = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]

        with open("posts.csv", "w", newline='', encoding='utf-8') as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    except requests.RequestException:
        print("Fetch fail")
