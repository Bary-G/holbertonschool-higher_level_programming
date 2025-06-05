#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
Module:
A script that contains abstract classes.
"""

class CountedIterator(ABC):
    """
    A class that extends the built-in iterator.
    """

    @abstractmethod
    def __init__(self, iter, iternum=0):
        """
        Print append notify.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        """
        Print extend notify.
        """
        print(f"Extended the list with [{x}] items.")

    def remove(self, item):
        """
        Print remove notify.
        """
        print(f"Removed [{item}] from the list.")
        
    def pop(self, index=-1):
        """
        Print pop notify.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list")
        return item
