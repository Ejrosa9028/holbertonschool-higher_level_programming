#!/usr/bin/python3
"""Este módulo define una clase Rectangle."""


class Rectangle:
    """Representa un rectángulo con ancho y alto."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Inicializa un nuevo rectángulo con el ancho y alto dados.

        Args:
            width (int): El ancho del rectángulo (por defecto es 0).
            height (int): El alto del rectángulo (por defecto es 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Obtiene el ancho del rectángulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """Establece el ancho del rectángulo con validación.

        Args:
            value (int): El nuevo ancho del rectángulo.

        Raises:
            TypeError: Si el ancho no es un número entero.
            ValueError: Si el ancho es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Obtiene el alto del rectángulo."""
        return self.__height

    @height.setter
    def height(self, value):
        """Establece el alto del rectángulo con validación.

        Args:
            value (int): El nuevo alto del rectángulo.

        Raises:
            TypeError: Si el alto no es un número entero.
            ValueError: Si el alto es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Devuelve el área del rectángulo."""
        return self.__width * self.__height

    def perimeter(self):
        """Devuelve el perímetro del rectángulo.

        Si el ancho o el alto es 0, el perímetro será 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Devuelve representación rect usando `print_symbol`."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol)*self.__width]*self.__height)

    def __repr__(self):
        """Devuelve representación con eval() y dar el rectángulo."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Imprime cuando la instancia del rectángulo es eliminada."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
