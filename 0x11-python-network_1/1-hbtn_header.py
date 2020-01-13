#!/usr/bin/python3
import urllib.request
import sys
"""This script displays the value of X-Request-Id header variable"""
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print("{}".format(response.info()['X-Request-Id']))
