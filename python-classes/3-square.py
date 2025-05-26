#!/usr/bin/python3
"""Este módulo define una clase Square."""


class Square:
    """Representa un cuadrado con un atributo privado de tamaño."""

    def __init__(self, size=0):
        """Inicializa un nuevo cuadrado con un tamaño dado.

        Args:
            size (int): El tamaño del cuadrado (por defecto es 0).

        Raises:
            TypeError: Si el tamaño no es un número entero.
            ValueError: Si el tamaño es menor que 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size ** 2
