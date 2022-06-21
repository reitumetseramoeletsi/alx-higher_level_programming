#!/usr/bin/python3
"""3-Square"""


class Square:
    """snitialises Square with size as integer"""

    def __init__(self, size=0):
        """size should be int"""
        self.__size = size

    """returns the area of a square"""

    def area(self):
        return self.__size ** 2
    
    @property
    def size(self):
        """retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size"""
        
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
