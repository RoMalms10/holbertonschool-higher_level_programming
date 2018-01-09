#!/usr/bin/python3
"""My module for Rectangles
"""


class Rectangle:
    """Class for rectangles
    """

    def __init__(self, width=0, height=0):
        """Calls getter and setters to initialize values
        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.width = width
        self.height = height

    def __repr__(self):
        """
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __str__(self):
        """Prints the rectangle
        """
        new_str = ""
        if self.width == 0 or self.height == 0:
            return new_str
        else:
            for num in range(self.height):
                for hsh in range(self.width):
                    new_str += "#"
                if num != self.height - 1:
                    new_str += "\n"
            return new_str

    def area(self):
        """Returns the area of the rectangle
        """
        return (self.width * self.height)

    def perimeter(self):
        """Returns the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width + self.height) * 2)

    @property
    def width(self):
        """Getter - gets the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter - sets the value of width
        Args:
            value (int): the value to set to width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter - gets the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter - sets the value of height
        Args:
            value (int): the value to set to height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
