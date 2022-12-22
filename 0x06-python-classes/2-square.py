#!/usr/bin/python3
"""Class Square with size"""


def __init__(self, size=0):
    """Instantiation"""

    self.size = 0
    if size != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    return square_size
