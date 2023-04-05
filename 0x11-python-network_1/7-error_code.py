#!/usr/bin/python3
""" A script that:
- Takes in a URL, sends a request to the URL
- Displays the body of the response.
- Prints Error code if the HTTP code is greater or equal to 400.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:{}".format(response.status_code))
    else:
        print(response.text)
