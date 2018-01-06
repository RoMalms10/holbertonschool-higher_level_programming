#!/usr/bin/python3
"""This module performs math on matrices"""


def matrix_divided(matrix, div):
    """This method divides each element in a matrix

    Args:
        matrix (list or lists): the matrix
        div (int): the number to divide each element by
    """

    # Checks if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    # Checks if the first element in matrix is a list so len can be used
    if isinstance(matrix[0], list):
        rowlen = len(matrix[0])

    # Checking if matrix is formatted correctly
    for mtx in matrix:

        # Checks if mtx is a list
        if not isinstance(mtx, list):
            print("in the right error")
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

        # Checks if the length of each row is the same
        if len(mtx) != rowlen:
            raise TypeError("Each row of the matrix must have the same size")

        # Checks if the elements in the matrix are int or float
        for elmnt in mtx:
            if not isinstance(elmnt, int) and not isinstance(elmnt, float):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    # Checks if div is a number
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    # Checks if div is 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Dividing original matrix and creating a new matrix
    new_matrix = [[round(idx / div, 2) for idx in mtx] for mtx in matrix]

    return new_matrix
