#!/usr/bin/python3
""" A script that:
- Takes in a URL and an email address
- Sends a POST request to the passed URL with the email as a parameter
- Displays the body of the response.
"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    email = sys.argv[2]

    value = {'email'}
    response = requests.post(url, data=value)
    print(response.text)
