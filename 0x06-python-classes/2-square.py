#!/usr/bin/python3
""" Defining a class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """ Defines a sqaure
    Attributes:
        size (int): the size of the sqaure
    """
    def __init__(self, size=0):
        """ definition of the __init__ method
        Args:
            size (int): the value size of a square
"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
