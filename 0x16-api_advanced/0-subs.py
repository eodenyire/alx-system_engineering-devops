#!/usr/bin/python3
"""
0-subs.py

This module contains the function number_of_subscribers 
which queries the Reddit API to retrieve the number of 
subscribers for a given subreddit.

Functions:
- number_of_subscribers(subreddit): Returns the number 
of subscribers for a given subreddit. If the subreddit 
is invalid, returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
