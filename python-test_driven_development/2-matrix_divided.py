#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of list of int/float): Matrix to divide.
        div (int or float): Divisor.

    Raises:
        TypeError: If matrix elements are not int/float or rows differ in size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        new matrix with all elements divided by div rounded to 2 decimals.
    """
    # Vérification que matrix est une liste de listes d'entiers ou floats
    if (not isinstance(matrix, list) or
        any(not isinstance(row, list) for row in matrix) or
        any(any(not isinstance(elem, (int, float)) for elem in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Vérification que toutes les lignes ont la même taille
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Vérification que div est un int ou float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Vérification division par zéro
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Division et arrondi
    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
