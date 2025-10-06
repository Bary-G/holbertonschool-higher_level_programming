#!/usr/bin/env python3
"""
Module : A Python file that runs functions.
pickle : A module used to convert data
"""
import pickle


class CustomObject:
    """A class that represents a custom object with propreties"""
    def __init__(self, name, age, is_student):
        """Class initialization"""
        if not isinstance(name, str):
            return None
        if not isinstance(age, int):
            return None
        if not isinstance(is_student, bool):
            return None
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display CustomObject class attributes"""
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize CustomObject class attributes"""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize CustomObject class attributes"""
        with open(filename, 'rb') as file:
            return pickle.load(file)
        
