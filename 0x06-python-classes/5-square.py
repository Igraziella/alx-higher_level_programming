#!/usr/bin/python3
"""Create a Class Square with:
- size property
- method of area and method of print_square
- getters & setters.
"""


class Square:
    """Class named Square"""

    def __init__(self, size=0):
        "Instantiation of a square with the size"""
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """method to get the current area of square"""
        (self.__size ** 2)

    def my_print(self):
        """method to print a square"""
        if (self.__size == 0):
            print()
        else:
            for rows in range(self.__size):
                print("#" * .__self)

    @property
    def size(self):
        """Getter of the private attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for the size private attribute"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
