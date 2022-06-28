#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """Creates a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a rectangle with height and width"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieves width"""
        return self.__width

    @property
    def height(self):
        """retrieves height"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """Returns string"""
        if not self.width or not self.height:
            return ""
        return (("#" * self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        """representation of rectangle that can be used by eval()"""
        str_repr = "Rectangle(" + str(self.width) + ","
        str_repr += str(self.height) + ")"
        return str_repr
