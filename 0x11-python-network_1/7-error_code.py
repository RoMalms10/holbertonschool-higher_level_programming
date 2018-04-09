#!/usr/bin/python3
""" Module that handles errors if they occur during a URL request
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        req = requests.get(url)
        print(req.text)
    except requests.exception.RequestException as e:
        print(e)
