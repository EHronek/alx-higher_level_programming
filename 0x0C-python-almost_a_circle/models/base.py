#!/usr/bin/python3
""" the first class ``Base`` in the file base.py"""


class Base:
    """ Represents the base model
    Represents the Base for all other classes in this project
    Attributes:
        __nb_objects (int): number of instantiated bases"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation of our class object
        Args:
            id (any): the id

"""
        self.__nb_objects = 0
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
