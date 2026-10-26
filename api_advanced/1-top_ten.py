#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "python:alu_scripting_api_advanced:v1.0 (by /u/gabrielagaba1)"
    }

    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False, timeout=10
        )
        if response.status_code != 200:
            print("None")
            return

        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print("None")
            return

        for post in posts[:10]:
            print(post.get("data", {}).get("title", ""))
    except (requests.RequestException, ValueError, TypeError):
        print("None")
