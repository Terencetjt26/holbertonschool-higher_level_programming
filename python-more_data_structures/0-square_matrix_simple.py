#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix where each element is the square of the corresponding element in the input matrix
    return [[item ** 2 for item in row] for row in matrix]
