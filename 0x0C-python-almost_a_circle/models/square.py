#!/usr/bin/python3
"""
A class square.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class inheriting from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter method"""

        return self.width

    @size.setter
    def size(self, value):
        """size setter method"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute

            1st argument should be the id attribute
            2nd argument should be the size attribute
            3th argument should be the x attribute
            4th argument should be the y attribute
        """

        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""

        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns a string containing id, x, y and size"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
