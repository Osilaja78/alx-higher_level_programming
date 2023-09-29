#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests

    res = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {res.text.__class__}")
    print(f"\t- content: {res.text}")
