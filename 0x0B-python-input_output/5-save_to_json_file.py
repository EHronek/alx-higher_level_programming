#!/usr/bin/python3
"""Defines a function that write an object to a text file, using JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """writes a python object to a text file, using JSON
    Args:
        my_obj (any): the python object to write to file
        file: the file to write to
"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
