#!/usr/bin/python3
import requests
import sys

"""Fetches a url and displays the variable X-Request"""
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
