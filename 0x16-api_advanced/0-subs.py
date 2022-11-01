#!/usr/bin/python3
"""Get number of subscribers in subreddit"""
import requests


def number_of_subscribers(subreddit):
    """gets number of subscibers in a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'alx/api'}

    response = requests.get(url, headers=headers)
    if response.status_code == '404':
        return (0)

    return (response.json().get('data').get('subscribers'))
