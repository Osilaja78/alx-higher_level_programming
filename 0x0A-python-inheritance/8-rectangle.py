#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
A class Rectangle.
"""


class Rectangle(BaseGeometry):
    """
    A class rectangle inheriting BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the Rectangle class.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
