#!/usr/bin/python3
"""Prints a square with #"""


def print_square(size):
    """Prints sqaure of size"""
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
