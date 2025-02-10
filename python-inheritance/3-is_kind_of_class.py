#!/usr/bin/python3
"""
Este módulo contiene la función is_kind_of_class, que verifica si un objeto
es una instancia de una clase o si el objeto es una instancia de una clase
que hereda de la clase especificada.

La función devuelve True si el objeto es una instancia de la clase indicada,
o si el objeto es una instancia de una subclase, y False en caso contrario.

Funciones:
    - is_kind_of_class: Verifica si un objeto es una instancia especifica
      o de una clase que hereda de ella.
"""


def is_kind_of_class(obj, a_class):
    """
    Verifica si el objeto es una instancia de la clase especificada o si
    el objeto es una instancia que hereda de la clase especificada.

    Args:
        obj: El objeto que se va a verificar.
        a_class: La clase contra la que se va a comprobar el objeto.

    Returns:
        bool: True si el objeto es una instancia de la clase especificada
              o una instancia una subclase de esa clase, False de lo contrario.
    """
    return isinstance(obj, a_class)
