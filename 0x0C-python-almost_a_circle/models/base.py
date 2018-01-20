#!/usr/bin/python3
""" My Module for creating a base class
"""


class Base:
    """ A class that will be used as a base for all other classes

    Attributes:
        id (public): id of the instance
        __nb_objects (private): the number of objects
    """

    id = 0
    __nb_objects = 0

    def __init__(self, id=None):
        """ Assigns the value of id to public instance attribute id,
            otherwise assign the number of objects to
            public instance attribute id

        Args:
            id (int): The number to assign to self.id
        """

        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = __nb_objects
