#!/usr/bin/python3
""" Module that interacts with Github API to display 10 commits
    to a repository
"""
import requests
from sys import argv


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)

    resp = requests.get(url)
    commit_list = resp.json()
    for index in range(0, 10):
        sha = commit_list[index].get('sha')
        author_name = commit_list[index].get('commit').get('author').get('name')
        print(author_name)
        print("{}: {}".format(sha, author_name))
