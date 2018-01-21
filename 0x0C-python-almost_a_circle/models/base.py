#!/usr/bin/python3
""" My Module for creating a base class
"""
import json


class Base:
    """ A class that will be used as a base for all other classes

    Attributes:
        __nb_objects (private): the number of objects
    """

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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Turns the dictionary representation of an instance into JSON

        Args:
            list_dictionaries (list): list of representations of an instances
        """

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        """

        filename = "{}.json".format(cls.__name__)
        obj_list = []

        if list_objs is not None:
            for obj in list_objs:
                obj_list += [obj.to_dictionary()]
        
        json_list = Base.to_json_string(obj_list)

        with open(filename, "w+", encoding="UTF-8") as f:
            f.write(json_list)
            
