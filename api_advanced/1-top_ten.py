#!/usr/bin/python3
"""Query the Reddit API and print the first 10 hot post titles."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(
        subreddit
    )
    headers = {"User-Agent": "ALUStudent/1.0"}

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
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
