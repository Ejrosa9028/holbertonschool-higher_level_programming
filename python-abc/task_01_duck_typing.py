#!/usr/bin/python3

"""
Este módulo define una jerarquía de clases para representar formas geométricas.

Clases:
    - Shape (abstracta): Clase base para todas las formas, define los métodos
      abstractos `area` y `perimeter`.
    - Circle: Clase que representa un círculo, implementa los métodos `area`
      y `perimeter` para un círculo.
    - Rectangle: Clase que representa un rectángulo, implementa los métodos
      `area` y `perimeter` para un rectángulo.

Funciones:
    - shape_info: Imprime el área y el perímetro de cualquier objeto que
      implemente los métodos `area` y `perimeter`.

Este módulo aprovecha el concepto de "Duck Typing" para manejar objetos de
formas geométricas sin comprobar explícitamente su tipo.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Clase abstracta Shape que sirve como base para otras formas.

    Métodos abstractos:
        - area: Calcula el área de la forma.
        - perimeter: Calcula el perímetro de la forma.
    """

    @abstractmethod
    def area(self):
        """Método abstracto para calcular el área."""
        pass

    @abstractmethod
    def perimeter(self):
        """Método abstracto para calcular el perímetro."""
        pass


class Circle(Shape):
    """
    Clase Circle que representa un círculo, hereda de Shape.

    Atributos:
        - radius: radio del círculo.

    Métodos:
        - area: Calcula el área del círculo.
        - perimeter: Calcula el perímetro del círculo.
    """

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        """Calcula el área del círculo."""
        return math.pi * self.__radius ** 2

    def perimeter(self):
        """Calcula el perímetro del círculo."""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    Clase Rectangle que representa un rectángulo, hereda de Shape.

    Atributos:
        - width: ancho del rectángulo.
        - height: altura del rectángulo.

    Métodos:
        - area: Calcula el área del rectángulo.
        - perimeter: Calcula el perímetro del rectángulo.
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        """Calcula el área del rectángulo."""
        return self.__width * self.__height

    def perimeter(self):
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """
    Función que imprime el área y el perímetro de cualquier objeto Shape.

    Argumentos:
        - shape: Un objeto que debe comportarse como un Shape.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
