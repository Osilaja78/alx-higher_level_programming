#!/usr/bin/python3
"""
Divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Function to divide all elements of a matrix by a given no. """

    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not\
            all(isinstance(row, list) for row in matrix):
        raise TypeError(message)

    row_sizes = [len(row) for row in matrix]
    if not all(size == row_sizes[0] for size in row_sizes):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(message)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []
    for row in matrix:
        divided_row = [round(element / div, 2) for element in row]
        divided_matrix.append(divided_row)

    return (divided_matrix)
