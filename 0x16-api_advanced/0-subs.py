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
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.adv:v1.0.0 (by /u/fg_okeke)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
