#!/usr/bin/python3
def matrix_divided(matrix, div):
    # Check if matrix is a list of lists of integers/floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(item, (int, float)) for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if each row has the same size
    row_length = len(matrix[0])  # Get the length of the first row
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Create the new matrix with divided values rounded to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = [round(item / div, 2) for item in row]
        new_matrix.append(new_row)
    
    return new_matrix
