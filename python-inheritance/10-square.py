#!/usr/bin/python3
"""
Module 10-square
Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class representing a square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """
        self.integer_validator("size", size)  # Validar size
        self.__size = size  # Asignar size como privado

        # Llamar a __init__ de Rectangle con width y height iguales
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size  # ✅ Implementación del área
