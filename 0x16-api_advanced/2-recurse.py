#!/usr/bin/python3
"""Script that is used to get data from api."""
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
