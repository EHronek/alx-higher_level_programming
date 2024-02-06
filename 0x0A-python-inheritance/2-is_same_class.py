#!/usr/bin/python3
"""This module defines a function that returns True if the object is
exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """This returns true if the object is exactly an instance of the
        of the specified class
    Args:
        obj: the object to check
        a_class: the object to compare with obj
    Returns:
        bool: Retruns true if the obj is an instance of a_clas
              otherwis otherwise false
"""
    result = isinstance(obj, a_class) and type(obj) == a_class
    if result:
        return True
    else:
        return False
