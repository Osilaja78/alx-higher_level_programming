#!/usr/bin/python3
"""
Creates an object form a JSON file.
"""
import json


def load_from_json_file(filename):
    """Creates an object form filename"""

    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
