#!/usr/bin/python3
import requests
import sys

"""Starwars search"""
if __name__ == "__main__":
    search = {'search': sys.argv[1]}
    r = requests.get('https://swapi.co/api/people', search)
    page = r.json()
    stringies, count = page['results'], page['count']
    # print(type(r.json()))
    # for x, y in r.json().items():
    #     print("dict -> \n{}\n[{}]\n", x, y)
    # a bunch of info can be found in the json version of the request
    print("Number of results: {}".format(count))
    for line in stringies:
        print(line['name'])
