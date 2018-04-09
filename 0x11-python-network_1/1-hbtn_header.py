#!/usr/bin/python3
""" Module that sends a request to a passed URL and displays
    the value of X-Request-Id
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        page = response.info()
    page = dict(page)
    print(page['X-Request-Id'])
