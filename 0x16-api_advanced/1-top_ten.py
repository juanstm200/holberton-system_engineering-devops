#!/usr/bin/python3
""" Module for storing the top_ten function. """
from requests import get


def top_ten(subreddit):
    """ Prints the hottest 10 posts on a given subbreddit. """

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'HolbertonSchool'}

    r = get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        for child in r.json()['data']['children']:
            print(child['data']['title'])
    else:
        print(None)
