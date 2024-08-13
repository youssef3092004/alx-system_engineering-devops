#!/usr/bin/python3
"""
Number of subscribers for a given subreddit.
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'my-reddit-app/0.1'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)

    if response.status_code != 200:
        return 0

    try:
        results = response.json()
        return results.get('data', {}).get('subscribers', 0)
    except ValueError:
        return 0
if __name__ == "__main__":
    subreddit = input("Enter the subreddit: ")
    subscribers = number_of_subscribers(subreddit)
    print("Number of subscribers:", subscribers)
