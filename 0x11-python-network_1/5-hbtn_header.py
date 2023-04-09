#!/usr/bin/python3
""" Script that:
- Takes in a URL, sends a request to the URL and
- Displays the value of the variable X-Request-Id in the response header
"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]

    response = requests.get(url)
    print((response.headers).get('X-Request-Id'))
