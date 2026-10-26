# API Advanced

## 0. How many subs?

The `0-subs.py` module defines `number_of_subscribers(subreddit)`.

This function sends a request to Reddit's subreddit information endpoint and returns the total number of subscribers. It returns `0` when the subreddit is invalid or the request fails.

The function uses the Requests library, supplies a custom User-Agent, and disables redirects.

### Prototype

    def number_of_subscribers(subreddit)

### Example

Run the main script from the repository root:

    python3 api_advanced/0-main.py programming

### Requirements

- Python 3
- Requests library
