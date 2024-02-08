#!/usr/bin/python3
"""defines a function that returns the dictionary representation of
a simple data structure."""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure
"""
    return obj.__dict__
