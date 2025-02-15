#!/usr/bin/python3
"""
Este módulo contiene la función save_to_json_file, que escribe un
objeto de Python en un archivo de texto usando una representación JSON.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Escribe un objeto de Python en un archivo de texto usando JSON.

    Args:
        my_obj: El objeto a escribir en el archivo.
        filename (str): El nombre del archivo donde se guardará el objeto.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
