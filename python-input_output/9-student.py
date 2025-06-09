#!/usr/bin/python3
"""Módulo que define la clase Student"""


class Student:
    """Representa a un estudiante con nombre, apellido y edad"""

    def __init__(self, first_name, last_name, age):
        """
        Inicializa una instancia de Student.

        Args:
            first_name (str): El nombre del estudiante.
            last_name (str): El apellido del estudiante.
            age (int): La edad del estudiante.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Obtiene una representación en forma de diccionario de la instancia.

        Returns:
            dict: El diccionario que representa al estudiante.
        """
        return self.__dict__
