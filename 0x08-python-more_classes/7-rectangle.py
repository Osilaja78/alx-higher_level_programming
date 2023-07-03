#!/usr/bin/python3
"""
A rectangle class
"""


class Rectangle:
    """
    Class that defines a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initializes a new instance of the Rectangle class. """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """ __width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ __width setter method """
        if not isinstance(value, int):
            raise ValueError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ __height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ __height setter method """
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Calculates and returns the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ Returns a string representation of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle_str += "{}".format(self.print_symbol)
                if j == (self.__width - 1) and i != (self.__height - 1):
                    rectangle_str += '\n'
        return rectangle_str

    def __repr__(self):
        """ Allows the use of eval() """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(cls):
        """ Prints a string when a rectangle is deleted """
        cls.number_of_instances -= 1
        print("Bye rectangle...")
