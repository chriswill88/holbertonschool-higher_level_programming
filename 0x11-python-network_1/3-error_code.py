#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys
"""This script displays error code"""

if __name__ == "__main__":
    url = sys.argv[1]

    # fecode body in utf-8
    try:
        with urllib.request.urlopen(url) as response:
            for i in response:
                print(i.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(e.code)
