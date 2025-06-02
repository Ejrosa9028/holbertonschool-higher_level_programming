#!/usr/bin/python3

"""
Este módulo contiene la clase BaseGeometry, que sirve como base para otras
clases relacionadas con geometría. La clase incluye un método llamado area()
que no está implementado y que debe ser sobrescrito en las clases derivadas.

Métodos:
    - area: Lanza una excepción indicando que el método no está implementado.
"""


class BaseGeometry:
    """
    Clase BaseGeometry que sirve como base para clases de geometría. El
    método area() debe ser implementado por las clases que hereden de esta
    clase.
    """

    def area(self):
        """
        Método que debe ser implementado en las subclases. Si se llama en
        una instancia de BaseGeometry, lanza una excepción con un mensaje.

        Raises:
            Exception: Si se llama sin ser implementado.
        """
        raise Exception("area() is not implemented")
