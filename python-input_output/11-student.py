#!/usr/bin/python3
"""
Module:
A file that runs Python functions.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.
        
        If attrs is a list of strings, only attributes listed in attrs will be retrieved.
        Otherwise, all attributes will be retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance using a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
