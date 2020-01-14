#!/usr/bin/python3
import requests
import sys

"""The Search API"""
username = sys.argv[1]
password = sys.argv[2]
r = requests.get('https://api.github.com/user', auth=(username, password))
try:
    print(r.json()['id'])
except Exception:
    print('None')
