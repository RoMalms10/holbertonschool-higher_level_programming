#!/usr/bin/python3
"""
"""


def print_square(size):
    """
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        print("#"*size)
