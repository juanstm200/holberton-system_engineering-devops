#!/usr/bin/python3
""" Module for storing the recurse function. """
from requests import get


def recurse(subreddit, hot_list=[], page_after=None):
    """ Returns a list with all of the hot articles """
    headers = {'User-Agent': 'HolbertonSchool'}
    if page_after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        r = get(url, headers=headers, allow_redirects=False)
        if r.status_code == 200:
            for child in r.json()['data']['children']:
                hot_list.append(child['data']['title'])
            if r.json()['data']['after'] is not None:
                recurse(subreddit, hot_list, r.json()['data']['after'])
        else:
            return None
    else:
        url = ('https://www.reddit.com/r/{}/hot.json?after={}'
               .format(subreddit,
                       page_after))
        r = get(url, headers=headers, allow_redirects=False)

        if r.status_code == 200:
            for child in r.json()['data']['children']:
                hot_list.append(child['data']['title'])
            if r.json()['data']['after'] is not None:
                recurse(subreddit, hot_list, r.json()['data']['after'])
        else:
            return None

    return hot_list
