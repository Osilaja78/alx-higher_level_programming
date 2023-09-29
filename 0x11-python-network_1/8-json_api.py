#!/usr/bin/python3
"""
This script sends a POST request with a letter
as a parameter.
"""


if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        try:
            result = response.json()
            if result:
                print(f"[{result['id']}] {result['name']}")
            else:
                print("No result")
        except ValueError:
            print("No valid JSON")
    except requests.exceptions.HTTPError as err:
        print("No result")
