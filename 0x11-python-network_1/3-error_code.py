#!/usr/bin/python3
""" Module that takes in a URL and sends a request
"""
import urllib.response
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read())
    except urllib.error.HTTPError as e:
        print("Error Code: {}".format(e.code))
