# ALU Scripting

This repository contains scripting exercises completed as part of the African Leadership University curriculum.

## API Advanced

The `api_advanced` directory contains Python scripts that interact with APIs.

### Task 0: How many subs?

File: `api_advanced/0-subs.py`

The `number_of_subscribers(subreddit)` function queries Reddit's subreddit information endpoint and returns the total number of subscribers.

- Prototype: `number_of_subscribers(subreddit)`
- Returns the total subscriber count for a valid subreddit.
- Returns `0` if the subreddit is invalid or the request fails.
- Uses the Python `requests` library.
- Sets a custom User-Agent.
- Disables HTTP redirects.

### Running the example

From the repository root:

    python3 api_advanced/0-main.py programming

### Requirements

- Python 3
- Python Requests library
