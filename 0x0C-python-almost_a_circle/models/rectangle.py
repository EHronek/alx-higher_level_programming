#!/usr/bin/python3
""" Defines a class ``Rectangle`` that inherits from the ``Base`` class"""


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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
