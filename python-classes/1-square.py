#!/usr/bin/python3
"""Defines a class Square with a private size."""


class Square:
    """A square defined by its private size."""

    def __init__(self, size):
        """Initializes a new square.

        Args:
            size: the size of the square.
        """
        self.__size = size
