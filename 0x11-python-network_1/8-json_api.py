#!/usr/bin/python3
import requests
import sys

"""The Search API"""
if __name__ == "__main__":
    try:
        q = {'q': sys.argv[1]}
    except Exception:
        q = ""
    r = requests.post(
        'http://7737658283c4.19.hbtn-cod.io:5000/search_user', data=q)
    try:
        print("[{}] {}".format(r.json()['id'], r.json()['name']))
    except Exception:
        if r.json() == {}:
            print("No result")
        else:
            print("Not a valid JSON")
