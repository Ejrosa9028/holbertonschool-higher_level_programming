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
        self.size = size  # Llamamos al setter para la validación

    @property
    def size(self):
        """Obtiene el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamaño del cuadrado, con validación.

        Args:
            value (int): El nuevo tamaño del cuadrado.

        Raises:
            TypeError: Si el tamaño no es un número entero.
            ValueError: Si el tamaño es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size ** 2
