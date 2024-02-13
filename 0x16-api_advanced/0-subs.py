#!/usr/bin/python3
"""
A module to interact with the Reddit API and retrieve the number of subscribers
for a given subreddit.
"""


import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given
    subreddit. If an invalid subreddit is given, returns 0.

    Args:
    subreddit (str): The subreddit to query.

    Returns:
    int: The number of subscribers or 0 if the subreddit is invalid.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'MyApp/1.0.0 (http://myapp.example.com)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data', {}).get('subscribers', 0)
    else:
        return 0
