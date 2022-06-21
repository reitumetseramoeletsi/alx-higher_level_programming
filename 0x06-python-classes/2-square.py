#!/usr/bin/python3
"""2-Square with an instance"""


class Square:
    """snitialises Square with size as integer"""

    def __init__(self, size=0):
        """size should be int"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
