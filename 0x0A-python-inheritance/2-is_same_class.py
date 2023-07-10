#!/usr/bin/python3
"""
Checks if the instance of an object
is same as passed.
"""


def is_same_class(obj, a_class):
    """
    Takes obj and a_class as arguments.

    Checks if the instance of obj is same
    as a_class.
    """

    return (type(obj) is a_class)
