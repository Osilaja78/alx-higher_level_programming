#!/usr/bin/python3
"""
A class rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle object"""

        #super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """ __width getter """
        return self.width

    @width.setter
    def width(self, value):
        """ __width setter method """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value

    @property
    def height(self):
        """ __height getter """
        return self.height

    @height.setter
    def height(self, value):
        """__height setter method"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.height = height

    @property
    def x(self):
        """__x getter method"""
        return self.x

    @x.setter
    def x(self, value):
        """__x setter method"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.x = value

    @property
    def y(self):
        """__y getter method"""
        return self.y

    @y.setter
    def y(self, value):
        """__y setter method"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.y = value
