#!/usr/bin/python3
"""
Module:
A script that contains abstract classes.
"""

class VerboseList(list):
    """
    A class that notifies Python list class changes.
    """

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        print(f"Extended the list with [{x}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        
    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list")
        return item