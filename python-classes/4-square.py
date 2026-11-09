#!/usr/bin/python3
"""Defines a class Square with a private size, a getter and a setter."""


class Square:
    """A square defined by its private size."""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size: the size of the square (an integer >= 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2
