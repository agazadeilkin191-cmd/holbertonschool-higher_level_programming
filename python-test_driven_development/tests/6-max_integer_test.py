#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
import sys
import os

# Bu hissə faylın yuxarı qovluqdakı modulu tapması üçün lazımdır
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test suite for max_integer function."""

    def test_ordered_list(self):
        """Test with a list of ordered integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with a list of unordered integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test with a list containing negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a list containing both positive and negative integers."""
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test with a list containing only one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_max_at_beginning(self):
        """Test with the max integer at the beginning."""
        self.assertEqual(max_integer([10, 2, 3]), 10)

    def test_identical_elements(self):
        """Test with a list of identical elements."""
        self.assertEqual(max_integer([7, 7, 7]), 7)

if __name__ == '__main__':
    unittest.main()
