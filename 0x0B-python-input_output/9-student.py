#!/usr/bin/python3
"""Defines a class Student that defines a student
"""
import json


class Student:
    """ defines a student"""
    def __init__(self, first_name, last_name, age):
        """initialization of student
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrives a dictionary represantation of a student instance"""
        return self.__dict__
