#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of
    the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-reddit-api'}
    response = requests.get(url, headers=headers, params={'limit': 10})

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])
    for post in posts:
        print(post.get('data', {}).get('title'))

