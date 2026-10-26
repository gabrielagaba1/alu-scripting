#!/usr/bin/python3
"""Returns the total number of subscribers for a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return subscriber count, or 0 for an invalid subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/gabrielagaba1)"}
    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False, timeout=10
        )
        if response.status_code != 200:
            return 0
        data = response.json().get("data")
        if not isinstance(data, dict):
            return 0
        return data.get("subscribers", 0)
    except (requests.RequestException, ValueError, TypeError):
        return 0
