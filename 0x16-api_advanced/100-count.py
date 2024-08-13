#!/usr/bin/python3
"""Script that is used to get data from api."""
import operator
import requests


def recurse(subreddit, hot_list=[]):
    """َQueries the reddit api and print title of top ten hot posts"""
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    header = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.get(url=url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json().get('data').get('children')
        length = len(hot_list)
        if length == len(posts):
            return hot_list
        hot_list.append(posts[length].get('data').get('title'))
        return recurse(subreddit, hot_list)
    return None


def count_words(subreddit, word_list, counts={}, titles=[]):
    """َQueries the reddit api and print title of top ten hot posts"""
    if len(word_list) == 0 and len(counts) > 0:
        sorted_counts = dict(sorted(counts.items(), key=operator.itemgetter(1), reverse=True))
        for key, value in sorted_counts.items():
            print(f"{key}: {value}")
    if len(titles) == 0:
        titles = recurse(subreddit)
        if titles is None:
            return
    for title in titles:
        for word in title.lower().split():
            if word == word_list[-1].lower():
                counts[word] = counts.get(word, 0) + 1
    return count_words(subreddit, word_list[:-1], counts, titles)
