#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ Defines a Rectangle """

    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        """ Creates a new rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.height

    def height(self, value):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if width == 0 or height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """ returns the printable representation of the Rectangle """
        if width == 0 or height == 0:
            return ("")
        else:
            for row in range(self.height):
                result += "#" * self.width
                if (row < self.height - 1):
                    result += "\n"
        return result
