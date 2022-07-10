#!/usr/bin/python3
"""
Rctangle = __import__('9-rectangle').Rectangle
"""
This module has a class: BaseGeometry
"""


class Square(Rectangle):
    """Square class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """Initializing the attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """rectangle area"""

        return self.__size ** 2
