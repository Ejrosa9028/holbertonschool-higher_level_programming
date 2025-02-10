#!/usr/bin/python3

"""
Este módulo contiene la clase Rectangle, que hereda de BaseGeometry.
La clase Rectangle se encarga de representar un rectángulo, validando que
sus dimensiones sean enteros positivos mediante el validador integer_validator
de la clase BaseGeometry.

Métodos:
    - __init__: Inicializa el objeto Rectangle con los atributos width y height
      asegurándose de que son enteros positivos.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Clase que hereda de BaseGeometry y representa un rectángulo. Se asegura
    de que los atributos width y height sean enteros positivos.
    """

    def __init__(self, width, height):
        """
        Método de inicialización para el rectángulo.
        Valida que width y height sean enteros positivos utilizando el
        validador integer_validator de la clase base.

        Args:
            width (int): El ancho del rectángulo.
            height (int): La altura del rectángulo.

        Raises:
            TypeError: Si width o height no son enteros.
            ValueError: Si width o height son menores o iguales a 0.
        """
        self.integer_validator("width", width)  # Valida el width
        self.integer_validator("height", height)  # Valida el height
        self.__width = width
        self.__height = height
