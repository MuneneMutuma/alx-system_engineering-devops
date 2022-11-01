#!/usr/bin/python3
"""
module queries and prints titles of top ten hot posts in subreddit
Invalid subreddits may return a redirect to search results.
Ensure that you are not following redirects.
"""
import requests


def top_ten(subreddit):
    """Gets the top ten subreddits"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'alx/top-ten'}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=params)

    if response.status_code != 200:
        print("None")
        return
    else:
        data = response.json().get('data').get('children')
        for post in data:
            title = post.get('data').get('title')
            if title:
                print(title)
