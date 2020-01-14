#!/usr/bin/python3
import requests
import sys

"""This script sends an email"""
if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    r = requests.post(url, email)
    print(r.text)
