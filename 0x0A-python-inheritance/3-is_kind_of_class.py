#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """check if an object is an instance or inherited instance of a class
    Args:
        obj (any): the object to inspect
        a_class (type): the class to match the type of obj
    Returns:
        bool: returns true if obj is an instance or inherited
        instance of a class Otherwise False
"""
    bool_result = isinstance(obj, a_class) or issubclass(type(obj), a_class)
    if bool_result:
        return True
    else:
        return False
