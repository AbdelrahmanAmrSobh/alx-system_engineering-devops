#!/usr/bin/python3
"""
Script that is used to get data from api
and display this data
"""
import requests


def number_of_subscribers(subreddit):
    """َQueries the reddit api and returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.request(url=url, headers=header,
                                allow_redirects=False, method='GET')
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
