#!/usr/bin/python3
"""2-Square with an instance"""


class Square:
    """Initialises Square with size as integer"""

    def __init__(self, size=0):
        """Size should be int"""

        if isinstance(size, int) is False:
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
