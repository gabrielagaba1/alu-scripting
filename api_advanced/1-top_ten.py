#!/usr/bin/python3
"""Retrieve and print the ten hottest posts from a subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the first ten hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (compatible; ALUStudent/1.0)"}

    try:
        response = requests.get(
            url,
            headers=headers,
            params={"limit": 10},
            allow_redirects=False,
            timeout=20
        )

        if response.status_code != 200:
            print("None")
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts[:10]:
            title = post.get("data", {}).get("title")
            if title is not None:
                print(title)

    except (requests.RequestException, ValueError):
        print("None")


if __name__ == "__main__":
    pass
