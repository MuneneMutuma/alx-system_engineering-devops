#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
returns 0 if invalid subreddit is given
"""
import requests


def number_of_subscribers(subreddit):
    """gets number of subscibers in a subreddit"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'alx/api'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return (0)

    ans = response.json().get('data').get('subscribers')
    
    if not ans:
        return (0)

    return ans
