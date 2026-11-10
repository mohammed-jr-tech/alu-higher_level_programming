#!/usr/bin/python3
"""
Defines a class Student with filtered JSON representation.
"""


class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes in attrs are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
