#!/usr/bin/python3
""" the first class ``Base`` in the file base.py"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string representation of a list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the json string representation of a list_objs to a file"""
        if list_objs is None:
            list_objs = []
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as f:
            f.write(cls.to_json_string([objs.to_dictionary() for objs in list_objs]))
