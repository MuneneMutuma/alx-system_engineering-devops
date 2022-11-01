#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the titles of all
hot articles for a given subreddit. If no results are found for the given
subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Does a recursive quer on subreddit, following pagination links"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {"User-Agent": "alx/recurs"}
    params = {"after": after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    length = response.json().get('data').get('dist')
    for i in range(length):
        data = response.json().get('data').get('children')[i].get('data')
        hot_list.append(data.get('title'))

    after = response.json().get('data').get('after')
    if after is not None:
        return recurse(subreddit, hot_list=hot_list, after=after)

    return hot_list
