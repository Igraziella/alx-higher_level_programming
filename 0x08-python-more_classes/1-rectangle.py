#!/usr/bin/python3
""" Defines a Rectangle class """


class Rectangle:
    """ Represents a rectangle """

    def __init__(self, width=0, height=0):
        """initializes a rectangle

        Args:

        width (int): The width of the new rectangle
        height (int): The height of the new rectangle
        """

        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
