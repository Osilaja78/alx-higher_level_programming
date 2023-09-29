#!/usr/bin/python3
"""
This script sends a request to a URL and displays the
value of the X-Request-Id in the response header.
"""


if __name__ == "__main__":
    import sys
    import requests

    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
