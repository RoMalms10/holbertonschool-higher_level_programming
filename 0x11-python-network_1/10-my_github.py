#!/usr/bin/python3
""" Module that interacts with the Github API
    to display the id of someone that is passed
    as an argument to the script
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    uname = argv[1]
    passwd = argv[2]

    data = requests.get(url, auth=(uname, passwd))
    if data.status_code == requests.codes.ok:
        new_dict = data.json()
        print(new_dict['id'])
    else:
        print("None")
