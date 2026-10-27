#!/usr/bin/python3
"""Print the first ten hot posts from a subreddit."""

import json
import urllib.error
import urllib.request


class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Prevent HTTP redirects."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def top_ten(subreddit):
    """Print titles of the ten hottest posts in a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(
        urllib.request.quote(subreddit, safe="")
    )
    request = urllib.request.Request(
        url, headers={"User-Agent": "alu-api-project/1.0"}
    )
    opener = urllib.request.build_opener(NoRedirectHandler)

    try:
        with opener.open(request, timeout=15) as response:
            data = json.loads(response.read().decode("utf-8"))
        posts = data.get("data", {}).get("children", [])
        for post in posts[:10]:
            title = post.get("data", {}).get("title")
            if title is not None:
                print(title)
    except (urllib.error.HTTPError, urllib.error.URLError, ValueError):
        print("None")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
