#!/usr/bin/python3
""" a class Square that defines a square by (based on 4-square.py)"""


class Square:
    """ The square based on 4-square.py
"""
    def __init__(self, size=0):
        """ instantion of our objects
        Args:
            size (int): the  value of the size of an integer
"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter methid for the sze attribute of the square"""
        return self.__size

    @size.setter
    def size(self, new_val):
        """ setter for the size attribute
        Args:
            new_val (int): the value to set as size

"""
        if not isinstance(new_val, int):
            raise TypeError("size must be an integer")
        if new_val < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_val

    def area(self):
        """public instance method that finds the area of the current square

        Returns:
            int: The area of the square

"""
        a = self.size ** 2
        return (a)

    def my_print(self):
        """public instance method that prints the square with # character"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                for _ in range(self.size):
                    print("#", end='')
                print()
