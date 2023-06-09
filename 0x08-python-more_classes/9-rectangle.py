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
            raise TypeError("width must be an integer")
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
            raise TypeError("height must be an integer")
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compares and returns the biggest triangle """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance with width == height == size """

        return cls(size, size)
