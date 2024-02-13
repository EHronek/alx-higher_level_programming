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

    def area(self):
        """ calculates then retuns area of the rectangle"""
        return self.height * self.width

    def display(self):
        """ prints the rectangle to stdout with # symbol """
        [print("") for _ in range(self.y)]
        for _ in range(self.height):
            [print(" ", end='') for _ in range(self.x)]
            [print('#', end='') for _ in range(self.width)]
            print('')

    def __str__(self):
       """ for readable user friendly representation of an object"""
       return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ it updates the rectangle with the values in the variable args"""
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y == arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width,
                                 self.height,
                                 self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """returnsa dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }
