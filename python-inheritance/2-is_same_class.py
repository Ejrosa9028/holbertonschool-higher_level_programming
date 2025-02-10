#!/usr/bin/python3

"""
Este módulo contiene la función is_same_class, que verifica si un objeto
es una instancia exacta de una clase especificada.

La función devuelve True si el objeto es exactamente una instancia de la
clase indicada, y False en caso contrario.

Funciones:
    - is_same_class: Verifica si un objeto es instancia exacta de una clase.
"""


def is_same_class(obj, a_class):
    """
    Verifica si el objeto es una instancia exacta de la clase especificada.

    Args:
        obj: El objeto que se va a verificar.
        a_class: La clase contra la que se va a comprobar el objeto.

    Returns:
        bool: True si el objeto es exactamente una instancia de la clase
              especificada, de lo contrario, False.
    """
    return type(obj) is a_class
