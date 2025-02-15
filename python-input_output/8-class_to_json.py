#!/usr/bin/python3
"""
Este módulo proporciona una función para convertir un objeto
a una representación de diccionario serializable en JSON.
"""


def class_to_json(obj):
    """
    Devuelve la descripción del diccionario con una estructura de datos simple
    (lista, diccionario, cadena, entero y booleano) para la serialización JSON
    de un objeto.

    Args:
        obj: Una instancia de una clase.

    Returns:
        dict: diccionario que contiene los atributos serializables del objeto.
    """
    return obj.__dict__
