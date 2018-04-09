#!/usr/bin/python3
""" Module that takes in a URL and displays a certain value
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    print(req.headers['x-request-id'])
