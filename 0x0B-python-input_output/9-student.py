#!/usr/bin/python3
"""
class Student: Defines a student
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """The init: Initialises methods and attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """The to_json module"""
        return self.__dict__
