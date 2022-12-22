#!/usr/bin/python3
"""Class Square with the size, method of area and getter & setter"""


class Square:
    """Class named Square"""

    def __init__(self, size=0):
        """Instantiation of a square with the size"""
        if (type(size) is not int):
            raise TypeError(size must be an integer)
        elif (size < 0):
            raise ValueError(size must be >= 0)
        else:
            self.__size = size

    def area(self):
        """method that returns the current square area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Getter of the private attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for the size of private attribute"""
        if (type(size) is not int):
            raise TypeError(size must be an integer)
        elif (size < 0):
            raise ValueError(size must be >= 0)
        else:
            self.__size = value
