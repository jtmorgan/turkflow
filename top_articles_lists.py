#! /usr/bin/env python

import boto3
import getpass
import glob
import json
from operator import itemgetter, getitem
import os
from pprint import pprint
import requests
from random import choice, sample, seed, shuffle
from urllib import parse
import time

def api_call(url):
    try:
        call = requests.get(url)
        response = call.json()
    except:
        response = None
    return response

if __name__ == '__main__':
    #https://en.wikipedia.org/api/rest_v1/feed/trending/edits
    endpoint = 'https://en.wikipedia.org/api/rest_v1/feed/trending/edits'
    print(endpoint)
    response = api_call(endpoint)
    print(response)

    if response:
        trending = {}
        for a in response['pages']:
            title = a['normalizedtitle']
            trending[title] = {}
            trending[title]['rank'] = a['trendiness']
            if 'description' in a.keys():
                trending[title]['description'] = a['description']
            else:
                trending[title]['description'] = ''
            if 'originalimage' in a.keys():
                trending[title]['image url'] = parse.unquote(a['originalimage']['source'])
            else:
                trending[title]['image url'] = ''
    else:
        print("Error retrieving data from API")

    print(trending)