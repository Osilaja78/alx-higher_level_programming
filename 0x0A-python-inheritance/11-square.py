#!/usr/bin/python3
"""
A class Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class square inheriting Rectangle.
    """

    def __init__(self, size):
        """Initializes a new Square object"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of the square"""

        return self.__size ** 2

    def __str__(self):
        """ Returns a string representation of the square """

        return "[Square] {}/{}".format(self.__size, self.__size)
