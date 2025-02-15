#!/usr/bin/python3
"""
Este módulo contiene la función to_json_string, que convierte
un objeto a su representación en formato JSON (cadena).
"""

import json


def to_json_string(my_obj):
    """
    Convierte un objeto a su representación en formato JSON (cadena).

    Args:
        my_obj: El objeto a convertir a JSON.

    Returns:
        str: La representación en formato JSON del objeto.
    """
    return json.dumps(my_obj)
