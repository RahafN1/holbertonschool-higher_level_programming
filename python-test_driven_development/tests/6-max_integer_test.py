#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_default_arg(self):
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_reverse_ordered_list(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 5, -10, 3]), 5)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([4, 4, 2, 4]), 4)

    def test_all_same(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)


if __name__ == '__main__':
    unittest.main()
