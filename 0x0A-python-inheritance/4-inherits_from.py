#!/usr/bin/python3
"""this module defines a function that returns True if the object is
an instance of a class that inherited (directly or indirectly) else false
"""


def inherits_from(obj, a_class):
    """ returns true if the object is an instance of a class that
    inherited(directly or indirectly) from specified class else false
    Args:
        obj (any): its the object to inspect
        a_class (type): the class to match the type of the object
    Returns:
        bool: returns true  if obj is inherited instance of a_class
        otherwise false
"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
