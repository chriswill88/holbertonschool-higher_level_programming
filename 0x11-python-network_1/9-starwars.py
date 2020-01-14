#!/usr/bin/python3
import requests
import sys

"""Starwars search"""
if __name__ == "__main__":
    search = {'search': sys.argv[1]}

    r = requests.get('https://swapi.co/api/people', search)
    # print(r.json()['results'])
    stringies = r.json()['results']
    print("Number of results: {}".format(len(stringies)))
    for i in stringies:
        print(i['name'])
        # for x in i:
        #     print(x['name'])
