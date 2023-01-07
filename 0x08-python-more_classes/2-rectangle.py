#!/usr/bin/python3
""" Class - rectangle """


class Rectangle:
    """ Defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Instantiates a new rectangle

        Args:
            width (int) = width of rectangle
            height (int) = height of rectangle """

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    """ sets the width of the rectangle """
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError(width must be >= 0)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    """ sets the height of the rectangle """
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
