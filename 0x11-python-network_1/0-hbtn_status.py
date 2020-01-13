#!/usr/bin/python3
import urllib.request

"""This script fetches a body response from a website"""
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response

        content = html.read()
        print("Body response:\n\t- type: {}".format(type(content)))

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response
        content = html.read()
        print("\t- content: {}".format(content))

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response
        for line in html:
            rline = line.decode('utf-8')
        print("\t- utf8 content: {}".format(rline))


