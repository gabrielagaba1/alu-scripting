#!/usr/bin/python3
"""Query the Reddit API and print the first 10 hot post titles."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
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

        data = response.json()
        children = data.get("data", {}).get("children", [])

        for post in children[:10]:
            title = post.get("data", {}).get("title")
            if title is not None:
                print(title)

    except (requests.RequestException, ValueError, TypeError):
        print("None")
