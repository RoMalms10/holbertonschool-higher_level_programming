#!/usr/bin/python3
""" My module for testing Square
"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Tests the square class
    """

    def test_id(self):
        """ Tests the id of the rectangle
        """

        Base._Base__nb_objects = 0
        s1 = Square(10, 2)
        s2 = Square(1, 1)
        s3 = Square(10, 0, 0, 12)

        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 12)

    def test_size(self):
        """ Test correct size being set
        """
        
        s1 = Square(10, 2)
        s2 = Square(666, 333)

        self.assertEqual(s1.size, 10)
        self.assertEqual(s2.size, 666)

    def test_no_arguments(self):
        """ Test when no arguements passed
        """

        with self.assertRaises(TypeError):
            s1 = Square()

    def test_with_size_and_x(self):
        """ Test when size and x are passed
        """

        s1 = Square(10, 3)
        
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 3)

    def test_with_size_x_and_y(self):
        """ Test when size, x and y are passed
        """

        s1 = Square(10, 3, 2)

        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 2)

    def test_with_all_arguments(self):
        """ Test when size, x, y and id are passed
        """

        s1 = Square(10, 3, 2, 50)

        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 50)
