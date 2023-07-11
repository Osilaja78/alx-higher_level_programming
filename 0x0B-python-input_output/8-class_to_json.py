#!/usr/bin/python3
"""
Returns a dictionary representation of an object.
"""


def class_to_json(obj):
    return vars(obj)
