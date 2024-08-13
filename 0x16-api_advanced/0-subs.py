#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of 
    subscribers for a given subreddit.
    If an invalid subreddit is given, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my-reddit-api'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0
    
    data = response.json()
    return data.get('data', {}).get('subscribers', 0)

