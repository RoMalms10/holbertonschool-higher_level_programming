#!/usr/bin/python3
"""The matrix multiplication module
"""


def matrix_mul(m_a, m_b):
    """Multiples two matrices

    Attributes:
        err_1a: error message 1
        err_1b: error message 2
        err_2a: error message 3
        err_2b: error message 4
        err_3a: error message 5
        err_3b: error message 6
        err_4a: error message 7
        err_4b: error message 8
        err_5: error message 9

    Args:
        m_a (list of lists containing ints or floats - matrix): matrix 1
        m_b (list of lists containing ints or floats - matrix): matrix 2

    Returns:
        New matrix
     """

    err_1a = "m_a must be a list"
    err_1b = "m_b must be a list"
    err_2a = "m_a should contain only integers or floats"
    err_2b = "m_b should contain only integers or floats"
    err_3a = "each row of m_a must should be of the same size"
    err_3b = "each row of m_b must should be of the same size"
    err_4a = "m_a can't be empty"
    err_4b = "m_b can't be empty"
    err_5 = "m_a and m_b can't be multiplied"

    if type(m_a) != list:
        raise TypeError(err_1a)
    if type(m_b) != list:
        raise TypeError(err_1b)
    if not isinstance(m_a[0], list):
        raise TypeError(err_1a)
    if not isinstance(m_b[0], list):
        raise TypeError(err_1b)
    if len(m_a[0]) == 0:
        raise ValueError(err_4a)
    if len(m_b[0]) == 0:
        raise ValueError(err_4b)

    rowlen_a = len(m_a[0])
    rowlen_b = len(m_b[0])

    if len(m_a[0]) != len(m_b):
        raise ValueError(err_5)

    # Checks m_a for errors
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError(err_1a)
        if len(row) != rowlen_a:
            raise TypeError(err_3a)
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(err_2a)

    # Checks m_b for errors
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError(err_1b)
        if len(row) != rowlen_b:
            raise TypeError(err_3b)
        for num in row:
                if not isinstance(num, (int, float)):
                    raise TypeError(err_2b)


    new = [[0 for _ in range(len(m_b[0]))] for i in range(len(m_a))]

    for row in range(len(m_a)):
        for col in range(len(m_a[0])):
            for col_b in range(len(m_b[0])):
                new[row][col_b] += m_a[row][col] * m_b[col][col_b]
    return new
