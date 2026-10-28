#!/usr/bin/python3
"""Recursively count keywords in hot Reddit post titles."""
import re
import requests


def count_words(subreddit, word_list, counts=None, after=None,
                word_multiplicity=None):
    """Print sorted keyword counts from all available hot posts."""
    if counts is None:
        counts = {}
        word_multiplicity = {}
        for word in word_list:
            word = word.lower()
            counts[word] = 0
            word_multiplicity[word] = word_multiplicity.get(word, 0) + 1

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
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title", "").lower()
            words = re.findall(r"[a-z0-9_]+", title)
            for word in words:
                if word in counts:
                    counts[word] += word_multiplicity[word]

        next_after = data.get("after")

        if next_after is not None and posts:
            return count_words(
                subreddit, word_list, counts, next_after,
                word_multiplicity
            )

        for word, count in sorted(
            counts.items(), key=lambda item: (-item[1], item[0])
        ):
            if count > 0:
                print("{}: {}".format(word, count))

    except (requests.RequestException, ValueError, TypeError, AttributeError):
        return
