#!/usr/bin/python3
""" Module connects to the Star Wars API
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://swapi.co/api/people/'
    search = argv[1]

    full_url = url + '?' + 'search={}'.format(search)

    req = requests.get(full_url)
    data = req.json()

    print("Number of results: {}".format(data['count']))

    people_list = data['results']
    for person in people_list:
        print("{}".format(person['name']))
