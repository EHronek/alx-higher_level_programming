#!/usr/bin/python3
""" Defining a class Square that defines a square based on 0-square.py"""


class Square:
    """Defines a square size
    Attributes:
        __size (int): the size of a square
"""
    __size = None

    def __init__(self, value):
        """Defining the conctructor for the Square object
        Args:
            value (int): the value size of a square
"""
        self.__size = value
