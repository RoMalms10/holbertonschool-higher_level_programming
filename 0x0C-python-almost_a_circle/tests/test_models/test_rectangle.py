#!/usr/bin/python3
""" My module for testing the Rectangle class
"""
import unittest
import io
import sys
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

    def test_width(self):
        """ Test correct width being set
        """
        
        r1 = Rectangle(10, 2)
        r2 = Rectangle(666, 333)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.width, 666)

    def test_height(self):
        """ Test correct height being set
        """

        r1 = Rectangle(10, 2)
        r2 = Rectangle(30, 50)

        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.height, 50)

    def test_no_arguments(self):
        """ Test when width and height aren't passed
        """

        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_with_one_argument(self):
        """ Test when only width is passed
        """

        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def test_with_width_and_height(self):
        """ Test when width and height are passed
        """

        Base._Base__nb_objects = 0

        r1 = Rectangle(3, 4)
        r2 = Rectangle(10, 20)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 20)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_with_x_passed(self):
        """ Test when width, height, and x are passed
        """

        Base._Base__nb_objects = 0

        r1 = Rectangle(4, 3, 1)
        r2 = Rectangle(20, 10, 4)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 20)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 0)

    def test_with_up_to_y_passed(self):
        """ Test when width, height, x, and y are passed
        """

        Base._Base__nb_objects = 0

        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 1)

    def test_with_negative_width(self):
        """ Test when width is negative
        """

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(-5, 4, 3, 2)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_with_zero_width(self):
        """ Test when width is zero
        """

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(0, 50, 2, 3)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_wtih_negative_height(self):
        """ Test when height is negative
        """

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(2, -5, 4, 3)
        self.assertEqual(str(err.exception), "height must be > 0")

    def test_with_zero_height(self):
        """ Test when height is zero
        """

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(2, 0, 3, 4)
        self.assertEqual(str(err.exception), "height must be > 0")

    def test_with_negative_x(self):
        """ Test when x is negative
        """

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(1, 2, -3, 4)
        self.assertEqual(str(err.exception), "x must be >= 0")

    def test_with_negative_y(self):
        """ Test when y is negative
        """

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(1, 2, 3, -4)
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_with_all_arguments(self):
        """ Test with all argument fields passed
        """

        r1 = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_list_width(self):
        """ Test when width is passed a list
        """

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle([5], 4, 3, 2, 1)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_dict_width(self):
        """ Test when width is passed a dict
        """

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle({"width": 5}, 4, 3, 2, 1)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_float_width(self):
        """ Test when width is passed a float
        """

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5.5, 4, 3, 2, 1)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_tuple_width(self):
        """ Test when width is passed a tuple
        """

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle((3, 4), 4, 3, 2, 1)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_list_height(self):
        """ Test when height is passed a list
        """

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, [4], 3, 2, 1)
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_dict_height(self):
        """ Test when height is passed a dict
        """

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(4, {"height": 5}, 3, 2, 1)
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_float_height(self):
        """ Test when height is passed a float
        """

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, 4.5, 3, 2, 1)
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_tuple_height(self):
        """ Test when height is passed a tuple
        """

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(3, (4, 5), 3, 2, 1)
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_list_x(self):
        """ Test when x is passed a list
        """

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, 4, [3], 2, 1)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_dict_x(self):
        """ Test when x is passed a dict
        """

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(4, 3, {"x": 5}, 2, 1)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_float_x(self):
        """ Test when x is passed a float
        """

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, 4, 3.5, 2, 1)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_tuple_x(self):
        """ Test when x is passed a tuple
        """

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(3, 4, (3, 2), 2, 1)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_list_y(self):
        """ Test when y is passed a list
        """

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, 4, 3, [2], 1)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_dict_y(self):
        """ Test when y is passed a dict
        """

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(4, 3, 2, {"y": 5}, 1)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_float_y(self):
        """ Test when y is passed a float
        """

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, 4, 3, 2.5, 1)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_tuple_y(self):
        """ Test when y is passed a tuple
        """

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(3, 4, 3, (1, 2), 1)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_area(self):
        """ Test for correct output for area
        """

        r1 = Rectangle(3, 3, 0, 0, 10)
        r2 = Rectangle(4, 4)
        r3 = Rectangle(2, 2, 3)
        r4 = Rectangle(2, 1, 4, 3)

        self.assertEqual(r1.area(), 9)
        self.assertEqual(r2.area(), 16)
        self.assertEqual(r3.area(), 4)
        self.assertEqual(r4.area(), 2)

    def test_display_number_zero(self):
        """ Test if display of rectangle is correct
        """

        display = "##\n##\n##\n"
        capturedOutput = io.StringIO() #Create StringIO Object
        sys.stdout = capturedOutput #Redirect stdout

        r1 = Rectangle(2, 3)

        r1.display() #Call Function
        self.assertEqual(capturedOutput.getvalue(), display) #use .getvalue

        sys.stdout = sys.__stdout__ #Reset redirect
