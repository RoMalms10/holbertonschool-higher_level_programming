#!/usr/bin/python3
"""My module for Rectangles
"""


class Rectangle:
    """Class for rectangles
    Attributes:
        number_of_instances (int): counts how many instances of rectangle
        print_symbol (str): the character to use when printing out rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Calls getter and setters to initialize values
           also increases the number of instances
        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    def __repr__(self):
        """Returns a string containing information about the rectangle
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
                    new_str += str(self.print_symbol)
                if num != self.height - 1:
                    new_str += "\n"
            return new_str

    def __del__(self):
        """Prints a statement when an instance is deleted
           and decreases the number of instances
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle…")

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Tests if the area of rectangle 1 is bigger or equal to rectangle 2

        Args:
            rect_1 (Rectangle): rectangle 1
            rect_2 (Rectangle): rectangle 2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

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
