#!/usr/bin/python3
import requests

"""Fetches a body response and displays it"""
if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}\n\t- content: {}".format(
        type(r.text), r.text))
