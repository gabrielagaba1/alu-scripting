#!/usr/bin/python3
"""Recursively retrieves all hot Reddit post titles."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot post titles for a subreddit."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-SWE-Student/1.0"}
    params = {"limit": 100}

    if after is not None:
        params["after"] = after

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code != 200:
            return None if not hot_list else hot_list

        data = response.json().get("data", {})
        posts = data.get("children", [])

        for post in posts:
            hot_list.append(post["data"]["title"])

        next_after = data.get("after")

        if next_after is None or not posts:
            return hot_list if hot_list else None

        return recurse(subreddit, hot_list, next_after)

    except (requests.RequestException, ValueError, KeyError, TypeError):
        return None if not hot_list else hot_list
