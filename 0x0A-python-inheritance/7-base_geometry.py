#!/usr/bin/python3
"""This module defines an based on 6-base_geometry
"""


class BaseGeometry:
    """ a class based of 5-base_geometry"""

    def area(self):
        """a public instance method that raise Exception
"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates ``value`` if value is not integer raise TypeError
        if value is less or equal to 0, raise valueError exception
        Args:
            name (str): name argument
            value (any): must be an integer
"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
