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

        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the Python version of a JSON string

        Args:
            json_string (str): string to turn into Python object
        """

        if json_string is None or len(json_string) == 0:
            json_string = []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Loads a list of objects, turns those objects into a list of
            dictionaries then sends them to a function that turns them into
            a JSON string, then saves it to a file, based on the name of a
            class.

        Args:
            list_objs (list of objects): objects to turn into 
        """

        filename = "{}.json".format(cls.__name__)
        obj_list = []

        if list_objs is not None:
            for obj in list_objs:
                obj_list += [obj.to_dictionary()]
        
        json_list = Base.to_json_string(obj_list)

        with open(filename, "w+", encoding="UTF-8") as f:
            f.write(json_list)

    @classmethod
    def create(cls, **dictionary):
        """ Creates a new instance of Square or Rectangle based off dictionary

        Args:
            dictionary (dict): dictionary of values to make into an instance of
                               Square or Rectangle
        """

        if "size" in dictionary:
            c1 = cls(1)
        else:
            c1 = cls(1, 1)

        c1.update(**dictionary)

        return c1

    @classmethod
    def load_from_file(cls):
        """
        """

        from_filename = "{}.json".format(cls.__name__)
        instance_list = []

        try:
            with open(from_filename, mode="r+", encoding="UTF-8") as f:
                raw_json = f.read()
            list_of_dicts = cls.from_json_string(raw_json)
            for d in list_of_dicts:
               instance_list += [cls.create(**d)]
        except FileNotFoundError:
            pass
        return instance_list
