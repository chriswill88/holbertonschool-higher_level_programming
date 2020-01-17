#!/usr/bin/python3
import requests
import sys

"""The Searching the API"""
if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    r = requests.post(
        'http://473998d62070.19.hbtn-cod.io:5000/search_user', data={'q': q}
        )
    try:
        if r.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
    except Exception:
        print("Not a valid JSON")
