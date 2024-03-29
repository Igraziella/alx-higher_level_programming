#!/usr/bin/python3
""" Takes in a letter,
- Sends a POST request to http://0.0.0.0:5000/search_user
- with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    value = {"q": letter}

    r = requests.post(url, data=value)

    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print('[{}] {}'.format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
