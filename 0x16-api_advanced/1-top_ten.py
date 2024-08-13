#!/usr/bin/python3
"""Script that is used to get data from api."""
import requests


def top_ten(subreddit):
    """َQueries the reddit api and print title of top ten hot posts"""
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    header = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.get(url=url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json().get('data').get('children')
        i = 0
        for post in posts:
            i += 1
            print(post.get('data').get('title'))
            if i == 10:
                break
    else:
        print(None)
