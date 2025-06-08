#!/usr/bin/python3
import pickle
"""
Module:
A file that runs Python functions.
"""


class CustomObject:
    """A CustomObject class."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the object's attributes."""
        print(f"Name: {self.name}, Age: {self.age}, Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the object and saves it to a file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object successfully saved to {filename}.")
        except (OSError, pickle.PickleError) as e:
            print(f"Error saving object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserializes the object from a file with exception handling."""
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            print(f"Object successfully loaded from {filename}.")
            return obj
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist.")
        except EOFError:
            print(f"Error: The file '{filename}' appears to be empty or malformed.")
        except (OSError, pickle.PickleError) as e:
            print(f"Error loading object: {e}")
        return None
