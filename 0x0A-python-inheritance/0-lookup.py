#!/usr/bin/python3
""" This module writes a functuin that returns the list of available attributes and methods of an object"""


def lookup(obj):
    """ This function returns the list of available attributes and methods of an object

    Args:
        obj: the object to inspect

    Returns:
        list: a list of available attributes and methods of an object"""
    return dir(obj)
