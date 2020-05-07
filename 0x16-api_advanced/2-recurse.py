#!/usr/bin/python3
""" This script queries the Reddit API for a list of hot articles
    of the given subreddit and returns the count. Written using
    recursion because Holberton demanded it """
import requests


def recurse(subreddit, hot_list=[], next_topic=''):
    try:
        hot = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'.
                           format(subreddit, next_topic),
                           allow_redirects=False,
                           headers={'User-Agent': 'custom'})
        if next_topic is None:
            return hot_list
        for topic in hot.json().get('data').get('children'):
            hot_list += [topic.get('data').get('title')]
        next_topic = hot.json().get('data').get('after')
        recurse(subreddit, hot_list, next_topic)
        return hot_list
    except:
        return None
