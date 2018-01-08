#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests the function max_integer for correct output
    """

    def test_integer(self):
        """Tests all positive numbers
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_None(self):
        """Tests what happens when None is passed
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_negatives(self):
        """Tests a list of negative numbers
        """
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_zero(self):
        """Tests a list size of 0
        """
        self.assertEqual(max_integer([]), None)

    def test_not_integer(self):
        """Tests when list contains something that's not an integer
        """
        with self.assertRaises(TypeError):
            max_integer([1, 2, "Penguin"])

    def test_positive_and_negative(self):
        """Test a list with positive and negative numbers
        """
        self.assertEqual(max_integer([1, 6, 100, 4, 0, -1, 10]), 100)

    def test_not_a_list(self):
        """Test a non-list item
        """
        with self.assertRaises(TypeError):
            max_integer("not a list")

    def test_with_dict(self):
        """Test with a dict
        """
        with self.assertRaises(TypeError):
            max_integer({5, 5, 5, 5})

if __name__ == '__main__':
    unittest.main()
