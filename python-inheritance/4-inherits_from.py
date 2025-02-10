#!/usr/bin/python3

"""
Este módulo contiene la función inherits_from, que verifica si un objeto
es una instancia de una clase que hereda (directa o indirectamente) de la
clase especificada.

La función devuelve True si el objeto es una instancia de una clase que
hereda (directa o indirectamente) de la clase indicada, y False en caso
contrario.

Funciones:
    - inherits_from: Verifica si un objeto es una instancia de una clase
      que hereda de la clase especificada.
"""


def inherits_from(obj, a_class):
    """
    Verifica si el objeto es una instancia de una clase que hereda (directa
    o indirectamente) de la clase especificada.

    Args:
        obj: El objeto que se va a verificar.
        a_class: La clase contra la que se va a comprobar la herencia.

    Returns:
        bool: True si el objeto es una instancia de una clase que hereda de
              la clase especificada (directa o indirectamente), False de lo
              contrario.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
