#!/usr/bin/python3
"""
This function reads a text file and prints to STDOUT
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
