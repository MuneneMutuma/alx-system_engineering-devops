#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the titles of all
hot articles for a given subreddit. If no results are found for the given
subreddit, the function should return None.
"""
import requests


def count_words(subreddit, word_list, after=None, count_dict={}):
    """Does a recursive quer on subreddit, following pagination links"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {"User-Agent": "alx/recurs"}
    params = {"after": after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    length = response.json().get('data').get('dist')
    for i in range(length):
        data = response.json().get('data').get('children')[i].get('data')
        for word in word_list:
            word = word.lower()
            title_words = data.get('title').lower().split(' ')
            for title in title_words:
                if title == word:
                    count_dict[word] = count_dict.get(word, 0) + 1

    after = response.json().get('data').get('after')
    if after is not None:
        return count_words(subreddit, word_list, after, count_dict)
    return sorted(count_dict)
