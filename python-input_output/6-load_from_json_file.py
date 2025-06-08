#!/usr/bin/python3
"""
Este módulo contiene la función load_from_json_file, que crea un objeto
de Python a partir de un archivo con una representación JSON.
"""

import json


def load_from_json_file(filename):
    """
    Crea un objeto de Python desde un archivo con una representación JSON.

    Args:
        filename (str): El nombre del archivo que contiene el JSON.

    Returns:
        El objeto de Python correspondiente al JSON en el archivo.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
