#!/usr/bin/python3

"""
Este módulo contiene la función from_json_string, que convierte
una cadena JSON a un objeto de estructura de datos de Python.
"""

import json


def from_json_string(my_str):
    """
    Convierte una cadena JSON en un objeto de datos de Python.

    Args:
        my_str (str): La cadena en formato JSON que se va a convertir.

    Returns:
        object: El objeto de datos de Python representado por la cadena JSON.
    """
    return json.loads(my_str)
