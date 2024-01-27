#!/usr/bin/python3
""" Defining a class Square that defines a square by: (based on 2_square.py)"""


class Square:
    """ Defining a template for a square"""
    def __init__(self, size=0):
        """ The constructor for the square objects
        Args:
            size (int): valuefor the size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ This function should find the area of a square
        Returns: the current square area
"""
        self.t_area = self.__size ** 2
        return (self.t_area)
