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
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
        self.iternum = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iterable):
            raise StopIteration
        item = self.iterable[self.index]
        self.index = self.index + 1
        self.iternum = self.iternum + 1
        print(f"Iteration [{self.iternum}]: Current item is {item}")
        return item
