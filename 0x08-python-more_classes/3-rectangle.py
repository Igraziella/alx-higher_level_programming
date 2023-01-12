#!/usr/bin/python3
""" Defines a Rectangle class """


class Rectangle:
    """ Represents a Rectangle """

    def __init__(self, width=0, height=0):
        """ Creates a new rectangle
        Args:
            size: length of each side
        """
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

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ returns the printable representation of the Rectangle """
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            for row in range(self.__height):
                result += "#" * self.__width
                if (row < self.__height - 1):
                    result += "\n"
            return result
