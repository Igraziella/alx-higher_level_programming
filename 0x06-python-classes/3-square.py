#!/usr/bin/python3
"""Class square with size and method of area"""


class Square:
    """Class named Square"""

    def __init__(self, size=0):
        """Instantiation of a square with the size"""
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """method that returns the current square area"""
        return (self.__size ** 2)
