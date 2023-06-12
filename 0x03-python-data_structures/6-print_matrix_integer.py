#!/usr/bin/python3
def print_matrix_integer(matrix):
    if not matrix:
        return None
    else:
        for row in matrix:
            for num in row:
                print("{:d}".format(num), end=" " if col < len(row) - 1 else '')
            print()
