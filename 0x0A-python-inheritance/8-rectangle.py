#!/usr/bin/python3
""" Defines a class Rectangle that inherits from  the BAseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """it represents a rectangle using Basegeometry"""
    def __init__(self, width, height):
        """initialisation of the rectangle

        Args:
            width (int): the width of the rectangle
            height (int): the height of the new rectangle
"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
