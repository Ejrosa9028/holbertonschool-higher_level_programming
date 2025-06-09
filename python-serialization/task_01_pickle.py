#!/usr/bin/env python3
"""
Módulo task_01_pickle.py

Este módulo contiene la definición de la clase `CustomObject`, la cual
permite serializar y deserializar objetos utilizando el módulo `pickle`.
Incluye métodos para guardar el estado del objeto en un archivo y
reconstruir el objeto desde un archivo serializado.

Clases:
    -CustomObject: Representa objeto con atributo `name`, `age` y `is_student`.
"""

import pickle


class CustomObject:
    """
    Clase personalizada que representa un objeto con nombre, edad y estado
    de estudiante.

    Atributos:
        - name (str): Nombre del objeto.
        - age (int): Edad del objeto.
        - is_student (bool): Indica si el objeto es estudiante.
    """

    def __init__(self, name, age, is_student):
        """
        Inicializa un objeto CustomObject con los atributos especificados.

        Args:
            name (str): Nombre del objeto.
            age (int): Edad del objeto.
            is_student (bool): Indica si el objeto es estudiante.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Muestra los atributos del objeto en un formato legible.

        Ejemplo de salida:
            Name: John
            Age: 25
            Is Student: True
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializa el objeto actual y lo guarda en un archivo usando pickle.

        Args:
            filename (str): Nombre del archivo donde se guardará el objeto.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializa un archivo para crear una instancia de CustomObject.

        Args:
            filename (str): Nombre del archivo desde el cual se cargará
            el objeto.

        Returns:
            CustomObject o None: La instancia deserializada o None si ocurre
            un error.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Deserialization error:: {e}")
            return None
