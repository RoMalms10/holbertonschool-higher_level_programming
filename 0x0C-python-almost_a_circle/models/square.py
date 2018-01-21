#!/usr/bin/python3
""" My module for Squares
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize an instance of a square

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): how much to shift the rectangle when printing
            y (int): how much to shift the rectangle when printing
            id (int): number of instances of rectangles
        """

        super().__init__(size, size, x, y, id)


    def update(self, *args, **kwargs):
        """ Updates attributes of a square

        Args:
            args (non-keyword arguments): non-specified amount of arguments
            kwargs (key-word arguments): non-specified amount of arguments
        """

        attrs_sq = ["id", "size", "x", "y"]

        for position_sq, var in enumerate(args):
            setattr(self, attrs_sq[position_sq], var)

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ Returns the informal representation of the Square
        """

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, 
                                                 self.y, self.size)

    def to_dictionary(self):
        """
        """

        new_dict = {}
        attrs = ["id", "size", "x", "y"]

        for att in attrs:
            new_dict[att] = getattr(self, att)

        return new_dict

    @property
    def size(self):
        """ Getter for size
        """

        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size

        Args:
            value (int): the value to assign to width/height
        """
        
        self.width = value
        self.height = value
