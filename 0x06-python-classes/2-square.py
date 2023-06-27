#!/usr/bin/python3
"""
a class Square that defines a square by:
Private instance attribute: size
"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes the class data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
