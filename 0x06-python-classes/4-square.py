#!/usr/bin/python3
""" a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """ a square based on( 3-square.py)"""
    def __init__(self, size=0):
        """The initialization of square class
        Args:
            size (int): the value of the size of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ Getter method for size attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method for the size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    def area(self):
        """ Calculates the area of the square"""
        a = self.size ** 2
        return (a)
