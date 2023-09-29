#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the body of the response.
"""


if __name__ == "__main__":
    import sys
    from urllib.request import urlopen
    from urllib.error import HTTPError

    try:
        with urlopen(sys.argv[1]) as r:
            content = r.read().decode('utf-8')
            print(content)
    except HTTPError as e:
        print(f"Error code: {e.code}")
