#!/usr/bin/python3
"""3-Square"""


class Square:
    """snitialises Square with size as integer"""

    def __init__(self, size=0, position=(0, 0)):
        """size should be int"""
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """retrieves position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets positon"""

        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """prints in stdout the square with a character"""

    def my_print(self):
        val = self.__size
        pos = self.__position

        if val == 0:
            print()
        else:
            for i in range(pos[1]):
                print()
            for j in range(val):
                for k in range(val + pos[0]):
                    if k < pos[0]:
                        print(" ", end='')
                    else:
                        print("#", end='')
                print()
