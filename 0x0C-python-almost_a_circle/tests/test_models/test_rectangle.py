#!/usr/bin/python3
""" My module for testing the Rectangle class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Tests the rectangle class
    """

    def test_id(self):
        """ Tests the id of the rectangle
        """

        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(1, 1)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
