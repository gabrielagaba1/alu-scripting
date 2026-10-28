#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:alu-scripting:v1.0 (by /u/your_username)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )

        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])

        for post in posts[:10]:
            print(post.get("data", {}).get("title"))

    except (requests.RequestException, ValueError):
        print(None)


if __name__ == "__main__":
    pass
