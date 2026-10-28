#!/usr/bin/python3
"""Queries the Reddit API and prints the first 10 hot post titles."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts in a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-SWE-Student/1.0"}
    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            params={"limit": 10}
        )
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {}).get("children", [])
        if not data:
            print(None)
            return

        for post in data[:10]:
            print(post.get("data", {}).get("title"))
    except (requests.RequestException, ValueError, AttributeError):
        print(None)
