#!/usr/bin/python3
"""Módulo que define la clase Student."""


class Student:
    """Representa a un estudiante con nombre, apellido y edad."""

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

    def to_json(self, attrs=None):
        """
        Obtiene una representación en forma de diccionario de la instancia.

        Si `attrs` es una lista de cadenas, solo se devuelven los atributos
        cuyos nombres estén en la lista. Si `attrs` no es una lista de cadenas,
        se devuelven todos los atributos.

        Args:
            attrs (list, opcional): Lista de nombres de atributos a recuperar.

        Returns:
            dict: El diccionario que representa al estudiante.
        """
        if isinstance(attrs, list) and all(
            isinstance(attr, str) for attr in attrs
        ):
            return {
                key: getattr(self, key) for key in attrs if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Reemplaza todos los atributos de instancia basándose en un diccionario.

        Args:
            json (dict): Diccionario con los nuevos valores de atributos.
        """
        for key, value in json.items():
            setattr(self, key, value)
