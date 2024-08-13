#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list 
    of all hot articles' titles for a given subreddit.
    If no results are found or the subreddit is invalid, returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-reddit-api'}
    response = requests.get(url, headers=headers, params={'after': hot_list[-1] if hot_list else None})

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get('data', {}).get('children', [])
    if not posts:
        return hot_list

    hot_list.extend(post.get('data', {}).get('title') for post in posts)
    after = data.get('data', {}).get('after')

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list)

