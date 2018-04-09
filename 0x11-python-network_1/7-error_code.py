#!/usr/bin/python3
""" Module that handles errors if they occur during a URL request
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    if req.status_code < 400:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
