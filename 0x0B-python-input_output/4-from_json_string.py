#!/usr/bin/python3
"""Defines a function that returns an object( python data structure
) repesented by a json string"""
import json


def from_json_string(my_str):
    """ returns an object python datastructure represented by a JSON string
    Args:
        my_str (any): string to return as a python object
"""
    return json.loads(my_str)
