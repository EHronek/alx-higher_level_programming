#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ It inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiation of our Square class
        Args:
            size (int): the size of the square
            x (int): the x coordinate
            y (int): the y coordinate
            width (int): the width of the square
            height (int): the height of the square
"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square further"""
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """human readable representation of our object"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    def to_dictionary(self):
        """ returns the dictionary representation of the Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }

