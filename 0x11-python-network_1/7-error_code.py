#!/usr/bin/python3
"""
This script sends a request to a URL and
displays the body of the response.
"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    try:
        res = requests.get(url)
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.HTTPError as err:
        print(f"Error code: {err.response.status_code}")
