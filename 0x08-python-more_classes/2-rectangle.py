#!/usr/bin/python3
""" Class - rectangle """


class Rectangle:
    """ Defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Instantiates a new rectangle

        Args:
            width (int) = width of rectangle
            height (int) = height of rectangle """

        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area of a rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns the perimeter of a rectangle """
        if self.__width == 0 or self.__height = 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @property
    def width(self):
        return self.__width

    @width.setter
    """ sets the width of a rectangle """
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
