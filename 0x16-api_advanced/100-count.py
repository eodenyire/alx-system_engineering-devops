#!/usr/bin/python3
import requests
from collections import Counter
import re

def count_words(subreddit, word_list):
    """
    Recursively queries the Reddit API, parses titles of all
    hot articles, and prints a sorted count of given keywords.
    """
    def fetch_titles(subreddit, after=None):
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {'User-Agent': 'my-reddit-api'}
        params = {'after': after} if after else {}
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            return None, None

        data = response.json()
        posts = data.get('data', {}).get('children', [])
        titles = [post.get('data', {}).get('title', '') for post in posts]
        after = data.get('data', {}).get('after')

        return titles, after

    def recurse(subreddit, word_list, after=None):
        titles, after = fetch_titles(subreddit, after)
        if titles is None:
            return

        words = [word.lower() for title in titles for word in re.findall(r'\b\w+\b', title.lower())]
        word_counts = Counter(words)
        word_list_lower = [word.lower() for word in word_list]

        counts = {word: word_counts[word] for word in word_list_lower if word in word_counts}
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

        for word, count in sorted_counts:
            print(f"{word}: {count}")

        if after:
            recurse(subreddit, word_list, after)

    recurse(subreddit, word_list)

