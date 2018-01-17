#!/usr/bin/python3
""" My module for turning objects into JSON
"""
import json


def to_json_string(my_obj):
    """ Turns an object into JSON

    Args:
        my_obj (object): object ot turn into JSON
    """
    return(json.JSONEncoder().encode(my_obj))
