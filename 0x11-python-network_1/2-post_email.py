#!/usr/bin/python3
"""
This script sends a POST request to a URL with email
as parameter and displays body of the response
"""


if __name__ == "__main__":
    import sys
    from urllib.parse import urlencode
    from urllib.request import urlopen

    data = urlencode({'email': sys.argv[2]}).encode('utf-8')

    try:
        with urllib.request.urlopen(sys.argv[1], data=data) as r:
            content = r.read().decode('utf-8')
            print(content)
    except urllib.error.URLError as e:
        print(f"{e}")
