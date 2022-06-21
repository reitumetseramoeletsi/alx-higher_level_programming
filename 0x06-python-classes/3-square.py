#!/usr/bin/python3
"""3-Square"""


class Square:
    """snitialises Square with size as integer"""

    def __init__(self, size=0):
        """size should be int"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """returns the area of a square"""

    def area(self):
        return self.__size ** 2
