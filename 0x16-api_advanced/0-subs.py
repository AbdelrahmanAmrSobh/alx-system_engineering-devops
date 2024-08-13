#!/usr/bin/python3
"""
Script that is used to get data from api
and display this data
"""
import requests


def number_of_subscribers(subreddit):
    """َQueries the reddit api and returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; \
              Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}
    response = requests.request(url=url, headers=header,
                                allow_redirects=False, method='GET')
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
