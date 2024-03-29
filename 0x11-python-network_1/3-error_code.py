#!/usr/bin/python3
""" A script thattakes in a URL,
- sends a request to the URL, and
- displays the body of the response (decoded in utf-8).
"""
import sys
from urllib import error, request


if __name__ == "__main__":

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
