#!/usr/bin/python3
"""Print the titles of the first 10 hot Reddit posts."""
import requests


def top_ten(subreddit):
    """Query Reddit and print up to 10 hot post titles."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-SWE-Student/1.0"}
    try:
        response = requests.get(
            url,
            headers=headers,
            params={"limit": 10},
            allow_redirects=False
        )

        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print(None)
            return

        for post in posts[:10]:
            print(post["data"]["title"])

    except (requests.RequestException, ValueError, KeyError, TypeError):
        print(None)
