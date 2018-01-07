#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    """

    def test_integer(self):
        """
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_None(self):
        """
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_negatives(self):
        """
        """
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

if __name__ == '__main__':
    unittest.main()
