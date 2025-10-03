#!/usr/bin/python3
"""
Module : A Python file that runs functions.
"""


class Student:
    """
    A class that represent a student
    """
    def __init__(self, first_name, last_name, age):
        """Class instantiation"""
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        if age <= 0:
            raise TypeError("age must be more than 0")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Return the dictionary description with simple data structure 
        for JSON serialization of an object
        """
        return self.__dict__
