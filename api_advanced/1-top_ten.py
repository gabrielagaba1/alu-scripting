#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Print up to 10 hot post titles for a valid subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (compatible; ALUStudent/1.0)"}

    try:
        response = requests.get(
            url,
            headers=headers,
            params={"limit": 10},
            allow_redirects=False,
            timeout=15
        )

        if response.status_code == 404 or response.status_code in (301, 302):
            print("None")
            return

        if response.status_code != 200:
            return

        posts = response.json().get("data", {}).get("children", [])

        for post in posts[:10]:
            print(post.get("data", {}).get("title", ""))

    except (requests.RequestException, ValueError, TypeError):
        return
