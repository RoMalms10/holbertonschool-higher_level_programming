#!/usr/bin/python3
""" Module that handles JSON when doing a POST
    request to a URL
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if argv[1]:
        q = argv[1]
    else:
        q=""

    values = {'q': q}

    req = requests.post(url, data=values)
    print(req)
    req = req.json
    print(req)
