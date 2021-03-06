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
        'http://0.0.0.0:5000/search_user', data={'q': q}
        )
    try:
        info = r.json()
        if info == {}:
            print("No result")
        else:
            print("[{}] {}".format(info.get('id'), info.get('name')))
    except Exception:
        print("Not a valid JSON")
