#!/usr/bin/python3
"""
This script solves a GitHub challenge.
"""


if __name__ == "__main__":
    import sys
    import requests

    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    commits = requests.get(url).json()

    try:
        for i in range(10):
            sha = commits[i].get("sha")
            name = commits[i].get("commit").get("author").get("name")
            print(f"{sha}: {name}")
    except IndexError:
        pass
