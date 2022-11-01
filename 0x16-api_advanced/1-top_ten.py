#!/usr/bin/python3
"""
module queries and prints titles of top ten hot posts in subreddit
Invalid subreddits may return a redirect to search results.
Ensure that you are not following redirects.
"""
import requests


def top_ten(subreddit):
    """Gets the top ten subreddits"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'alx/top-ten'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return
    else:
        for i in range(10):
            data = response.json().get('data').get('children')[i].get('data')
            print(data.get('title'))
