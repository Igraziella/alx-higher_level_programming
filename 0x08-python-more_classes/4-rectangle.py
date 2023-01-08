#!/usr/bin/python3
""" Class - rectangle """


class Rectangle:
    """ Defines a rectangle """
    __width = width
    __height = height

    def __init__(self, width=0, height=0):
        """ Initializes a new rectangle

        Args:

        width (int) = width of rectangle
        height (int) = height of rectangle """

    self.width = width
    self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        result = ""

        if self.height == 0 or self.width == 0:
            result += ''
        else:
            for row in range(self.height):
                result += "#" * self.width
                if (row < self.height - 1):
                    result += '\n'
        return result

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
