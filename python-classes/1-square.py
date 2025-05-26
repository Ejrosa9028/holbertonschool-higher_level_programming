#!/usr/bin/python3
"""Este módulo define una clase Square."""


class Square:
    """Representa un cuadrado con un atributo de tamaño privado."""

    def __init__(self, size):
        """Inicializar un nuevo cuadrado con un tamaño determinado."""
        self.__size = size
