#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

"""This script sends an email"""
if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')

    # fecode body in utf-8
    with urllib.request.urlopen(url, data) as response:
        for i in response:
            print(i.decode('utf-8'))
