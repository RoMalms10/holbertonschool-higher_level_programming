#!/usr/bin/python3
"""This module performs math on matrices"""


def matrix_divided(matrix, div):
    """This method divides each element in a matrix

    Args:
        matrix (list or lists): the matrix
        div (int): the number to divide each element by

    Attributes:
        err_1 (str): error message 1
        err_2 (str): error message 2
        err_3 (str): error message 3
        err_4 (str): error message 4
    """
    
    err_1 = "matrix must be a matrix (list of lists) of integers/floats"
    err_2 = "Each row of the matrix must have the same size"
    err_3 = "div must be a number"
    err_4 = "division by zero"


    # Checks if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError(err_1)

    # Checks if the first element in matrix is a list so len can be used
    if isinstance(matrix[0], list):
        rowlen = len(matrix[0])

    # Checking if matrix is formatted correctly
    for mtx in matrix:

        # Checks if mtx is a list
        if not isinstance(mtx, list):
            raise TypeError(err_1)

        # Checks if the length of each row is the same
        if len(mtx) != rowlen:
            raise TypeError(err_2)

        # Checks if the elements in the matrix are int or float
        for elmnt in mtx:
            if not isinstance(elmnt, int) and not isinstance(elmnt, float):
                raise TypeError(err_1)

    # Checks if div is a number
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(err_3)

    # Checks if div is 0
    if div == 0:
        raise ZeroDivisionError(err_4)

    # Dividing original matrix and creating a new matrix
    new_matrix = [[round(idx / div, 2) for idx in mtx] for mtx in matrix]

    return new_matrix
