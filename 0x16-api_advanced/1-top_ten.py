#!/usr/bin/python3
""" This script queries the Reddit API and prints the titles of
    Reddit threads of the given subreddit. Only the top 10 are
    listed """
import requests


def top_ten(subreddit):
    try:
        hot = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.
                           format(subreddit), allow_redirects=False,
                           headers={'User-Agent': 'custom'})
        for topic in hot.json().get('data').get('children'):
            print(topic.get('data').get('title'))
    except:
        print('None')
