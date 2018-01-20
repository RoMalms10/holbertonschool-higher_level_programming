#!/usr/bin/python3
""" My Module for Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes values

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): how much to shift the rectangle when printing
            y (int): how much to shift the rectangle when printing
            id (int): number of instances of rectangles
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def integer_validator(var_name, value):
        """ Validates and handles all error messages

        Args:
            var_name (str): the variable name
            value (int): the value associated with var_name
        """

        err1 = ["width", "height"]
        err2 = ["x", "y"]

        if type(value) != int:
            raise TypeError("{} must be an integer".format(var_name))
        if var_name in err1 and value <= 0:
            raise ValueError("{} must be > 0".format(var_name))
        if var_name in err2 and value < 0:
            raise ValueError("{} must be >= 0".format(var_name))

    @property
    def width(self):
        """ Getter for width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width

        Args:
            value (int): the value to set to width
        """

        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """ Getter for height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height

        Args:
            value (int): the value to set to height
        """

        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """ Getter for x
        """

        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x

        Args:
            value (int): the value to assign to x
        """

        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """ Getter for y
        """

        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y

        Args:
            value (int): the value to assign to y
        """

        self.integer_validator("y", value)
        self.__y = value
