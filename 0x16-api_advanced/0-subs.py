#!/usr/bin/python3
""" Module for storing the number_of_subscribers """
from requests import get


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers. """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'HolbertonSchool'}

    r = get(url, headers=headers, allow_redirects=False)

    if r.status_code == 200:
        return r.json()['data']['subscribers']
    else:
        return 0
