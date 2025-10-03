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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the dictionary description with simple data structure 
        for JSON serialization of an object.
        If attrs is a list of strings, only attribute names contained in
        this list must be retrieved, otherwise, all attributes must be retrieved
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
