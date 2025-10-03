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

    def to_json(self):
        """
        Return the dictionary description with simple data structure 
        for JSON serialization of an object
        """
        return self.__dict__
