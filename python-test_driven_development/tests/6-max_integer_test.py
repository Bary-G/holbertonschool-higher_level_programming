#!/usr/bin/python3
import unittest
"""
Module: A Python script file with functions.
unittest: for testing environnement.
"""

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Unittests for the function
    """
    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-10, 0, 5, 3]), 5)

    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_duplicates(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_at_start(self):
        self.assertEqual(max_integer([99, 1, 2, 3]), 99)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 100]), 100)

    def test_all_equal(self):
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

    def test_nested_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, [2], 3])

    def test_dict_input(self):
        with self.assertRaises(TypeError):
            max_integer({"a": 1, "b": 2})

if __name__ == "__main__":
    unittest.main()
