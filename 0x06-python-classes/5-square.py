#!/usr/bin/python3
"""
A class Square that defines a square by:
Private instance attribute: size
"""


class Square:
    """
    Square class defines a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.

        If the size is 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
