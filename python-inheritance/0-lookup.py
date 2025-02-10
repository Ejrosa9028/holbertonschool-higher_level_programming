#!/usr/bin/python3

"""
Este módulo contiene una función llamada `lookup`, que devuelve una lista de
los atributos y métodos disponibles de un objeto.

La función `lookup` utiliza la función incorporada `dir()` para obtener los
atributos y métodos de cualquier objeto pasado como argumento.

Funciones:
    lookup(obj): Devuelve una lista de atributos y métodos de un objeto.
"""


def lookup(obj):
    """
    Devuelve una lista de los atributos y métodos disponibles de un objeto.

    Args:
        obj: El objeto del que se desean obtener los atributos y métodos.

    Returns:
        list: Una lista de cadenas que representan los atributos y métodos
              del objeto.

    Ejemplo:
        class MyClass:
            def __init__(self):
                self.attr = 42
            def method(self):
                pass

        print(lookup(MyClass))
        # Devuelve una lista con los atributos y métodos de MyClass,
        # incluyendo 'attr' y 'method'.
    """
    return dir(obj)
