#!/usr/bin/python3
"""
A a function that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """Recieves an object as argument and returns
    a list o available attributes and methods of
    the object"""

    return (dir(obj))
