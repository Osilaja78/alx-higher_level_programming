#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found.
"""


if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as r:
        header = r.headers.get('X-Request-Id')
        print(header)
