#!/usr/bin/python3
def lookup(obj):
    """
    Devuelve una lista de los atributos y métodos disponibles de un objeto.

    Args:
        obj: El objeto del que se desean obtener los atributos y métodos.

    Returns:
        list: Una lista de cadenas que representan los atributos y métodos del objeto.

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
