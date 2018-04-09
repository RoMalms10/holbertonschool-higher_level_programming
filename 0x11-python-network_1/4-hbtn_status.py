#!/usr/bin/python3
""" Module that fetches from a URL using requests
"""
import requests


if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
