#!/usr/bin/python3
import requests
import sys

"""The Searching the API"""
if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]

    r = requests.post(
        'http://0.0.0.0:5000/search_user', data={'q': q}
        )
    try:
        if r.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.json['id'], r.json['name']))
    except Exception:
        print("Not a valid JSON")
