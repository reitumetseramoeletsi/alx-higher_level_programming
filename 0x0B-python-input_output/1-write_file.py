#!/usr/bin/python3
"""
This function writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """ The write_file module
    """
    with open(filename, 'w') as f:
        return f.write(text)
