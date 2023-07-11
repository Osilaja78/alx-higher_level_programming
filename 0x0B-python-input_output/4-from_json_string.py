#!/usr/bin/python3
"""
Converts an object from JSON string
to Object.
"""
import json


def from_json_string(my_str):
    """Returns object form JSON string my_str"""

    return json.loads(my_str)
