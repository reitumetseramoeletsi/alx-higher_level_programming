#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
This module has class BaseGeometry
"""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialized the attrubutes"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method to redefine a area method in the parent class"""

        return self.__width * self.__height

    def __str__(self):
        """method to return the next string"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
