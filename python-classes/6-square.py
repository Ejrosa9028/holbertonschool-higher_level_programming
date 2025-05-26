#!/usr/bin/python3
"""Este módulo define una clase Square."""


class Square:
    """Representa un cuadrado con un atributo privado de tamaño y posición."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa un nuevo cuadrado con un tamaño y una posición dados.

        Args:
            size (int): El tamaño del cuadrado (por defecto es 0).
            position (tuple): La posición del cuadrado (por defecto es (0, 0)).

        Raises:
            TypeError: Si el tamaño no es número entero.
            ValueError: Si el tamaño es menor que 0 o si los elementos.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Obtiene el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamaño del cuadrado con validación.

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

    @property
    def position(self):
        """Obtiene la posición del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece la posición del cuadrado con validación.

        Args:
            value (tuple): La nueva posición del cuadrado.

        Raises:
            TypeError: Si la posición no es una tupla de 2 enteros positivos.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
           not all(isinstance(i, int) for i in value) or
           not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado con el carácter '#', utilizando la posición.

        Si el tamaño es 0, imprime una línea vacía.
        La posición se utiliza para agregar espacios antes de dibujar cuadrado.
        """
        if self.__size == 0:
            print("")
        else:
            # Imprime las filas de espacios según la posición
            for i in range(self.__position[1]):
                print()
            # Imprime el cuadrado con espacios al principio de cada fila
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
