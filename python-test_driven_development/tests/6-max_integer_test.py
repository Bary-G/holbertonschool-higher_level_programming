#!/usr/bin/python3
import unittest
from your_module import max_integer  # Replace 'your_module' with the actual module name

class TestMaxInteger(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))  # Assuming function returns None for empty lists

    def test_duplicates(self):
        self.assertEqual(max_integer([1, 2, 2, 3, 3]), 3)

    def test_large_numbers(self):
        self.assertEqual(max_integer([10**6, 10**9, 10**3]), 10**9)

if __name__ == '__main__':
    unittest.main()
