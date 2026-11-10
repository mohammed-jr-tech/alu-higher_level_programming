#!/usr/bin/python3
"""
Defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    A class that inherits from list with a method to print sorted elements.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        print(sorted(self))
