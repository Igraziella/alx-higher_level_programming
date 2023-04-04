#!/usr/bin/python3
""" A script that takes in a URL,
- sends a POST request to the URL passed,
- takes email as a parameter, and
- displays the body of the response
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        html = response.read().decode("utf-8")
        print(html)
