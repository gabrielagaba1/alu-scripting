#!/usr/bin/python3
"""Tests the number_of_subscribers function."""
import sys
from importlib.machinery import SourceFileLoader

number_of_subscribers = SourceFileLoader(
    "subs", "api_advanced/0-subs.py"
).load_module().number_of_subscribers

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
