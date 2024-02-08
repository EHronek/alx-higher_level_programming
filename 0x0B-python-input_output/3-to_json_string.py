#!/usr/bin/python3
"""defines a function that returns the json representation of an object(string
"""
import json


def to_json_string(my_obj):
    """returns the json representation of an object(string)
    Args:
        my_obj (any): the object to return astring represents
"""
    return json.dumps(my_obj)
