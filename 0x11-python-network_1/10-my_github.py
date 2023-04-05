#!/usr/bin/python3
""" A Python script that takes:
- Your GitHub credentials (username and password),
- and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]

    headers = {"Authorization": "Basic" + (username + " " + password)}

    response = requests.get("https://api.github.com/user", headers=headers)
    print(response.json().get("id"))
