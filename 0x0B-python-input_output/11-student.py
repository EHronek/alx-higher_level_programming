#!/usr/bin/python3
""" Defines a class student based on 10-student.py"""


class Student:
    """ Class student based on 10-student.py """

    def __init__(self, first_name, last_name, age):
        """ Instance of  the class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self, attrs=None):
        """ Retrives the dictionary representation of Student object """
        if attrs is None:
            return self.__dict__
        else:
            obj_dict = {}
            if isinstance(attrs, list):
                for attr in attrs:
                    if hasattr(self, attr):
                        obj_dict[attr] = getattr(self, attr)
                return obj_dict

    def reload_from_json(self, json):
        """ Replaces all attributes of the student instance """
        for k, v in json.items():
            setattr(self, k, v)
