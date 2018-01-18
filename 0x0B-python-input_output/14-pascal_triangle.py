#!/usr/bin/python3
""" My Module for pascal's triangle
"""


def pascal_triangle(n):
    """ Create a pascals triangle in a matrix

    Args:
        n (int): how many rows to make
    """
    pascal = [[] for _ in range(n)]

    pascal[0].append(1)
    for row in range(1, n):
        try:
            pascal[row].append(1)
            for elem in range(len(pascal[row - 1])):
                pascal[row].append(pascal[row - 1][elem] +
                                   pascal[row - 1][elem + 1])
        except:
            pascal[row].append(1)
    return pascal
