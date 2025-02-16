#!/usr/bin/python3
"""Módulo que genera el triángulo de Pascal."""


def pascal_triangle(n):
    """
    Genera lista de listas que representa el triángulo de Pascal de tamaño n.

    Args:
        n (int): El número de filas del triángulo de Pascal.

    Returns:
        list: Una listas, donde cada lista representa una fila del triángulo.
              Devuelve una lista vacía si n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Primera fila del triángulo

    for i in range(1, n):
        # Cada fila comienza y termina con 1
        row = [1]

        # Genera elementos internos sumando los elemento adya de fila anterior
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # Añadir el último 1 a la fila
        row.append(1)

        # Agregar la nueva fila al triángulo
        triangle.append(row)

    return triangle
