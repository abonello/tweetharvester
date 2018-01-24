#!/usr/bin/env python2
import json
import tweepy
from keys_and_secrets import get_auth, twitter_api
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter

# Twitter API authentication keys
api = twitter_api()
auth = get_auth()

count = 150
#query = 'Brexit'
query = 'Ireland'


# Get all tweets for the search query
# list comprehension using the api.search object based on the query value
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]