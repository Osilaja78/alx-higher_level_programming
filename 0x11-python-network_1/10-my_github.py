#!/usr/bin/python3
"""
This script takes my GitHub usernam and password
and returns my user id.
"""


if __name__ == "__main__":
    import sys
    import requests

    username = sys.argv[1]
    password = sys.argv[2]
    url = f"https://api.github.com/user"
    auth = (username, password)

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        user_data = response.json()
        user_id = user_data.get('id')
        if user_id:
            print(user_id)
    except requests.exceptions.RequestException as e:
        print(f"Error encountered: {e}")
