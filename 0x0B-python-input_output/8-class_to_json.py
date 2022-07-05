#!/usr/bin/python3
"""
This function returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """The class_to_json module"""
    return obj.__dict__
