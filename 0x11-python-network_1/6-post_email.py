#!/usr/bin/python3
""" Module that takes in a URL and email address and sends a POST request
    to the URL with the email as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    values = {'email': email}
    
    req = requests.post(url, data=values)
    print(req.text)
