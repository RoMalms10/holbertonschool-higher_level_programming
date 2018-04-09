#!/usr/bin/python3
""" Module for sending a POST request
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    
    with urllib.request.urlopen(req) as response:
        page = response.read()
    print(page.decode('utf-8'))
