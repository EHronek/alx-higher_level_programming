#!/usr/bin/python3
""" Defines a class ``Rectangle`` that inherits from the ``Base`` class"""
from models.base import Base


class Rectangle(Base):
    """It inherits from the Base class
    Attributes:
        __width (int): the width of the rectangle
        __height (int): the height of the rectangle
        __x: x
        __y: y
"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instantion of the rectangle object
        Args:
            width (int): the value of the width
            height (int): the value of the height
            x (int): the x
            y (int): the y
"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter method for our rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ setter for the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for the x coodinates of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for the x coodinates of rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter method for the y coodinates """
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for the y coodinates of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
