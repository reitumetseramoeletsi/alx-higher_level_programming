#!/usr/bin/python3
"""
this module has a class BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """method for area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate if a num is integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
