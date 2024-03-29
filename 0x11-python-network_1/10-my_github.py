#!/usr/bin/python3
""" A Python script that takes:
- Your GitHub credentials (username and password),
- and uses the GitHub API to display your id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":

    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    response = requests.get(url, auth=auth)
    print(response.json().get('id'))
