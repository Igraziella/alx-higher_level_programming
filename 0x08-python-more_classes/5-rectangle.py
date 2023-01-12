#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ class Rectangle that defines a rectangle """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        result = ''

        if self.__height == 0 or self.__width == 0:
            result += ''
        else:
            for row in range(self.__height):
                result += "#" * self.__width
                if (row < self.__height - 1):
                    result += '\n'
        return result

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
