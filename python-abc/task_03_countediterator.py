#!/usr/bin/env python3
"""
Este módulo define la clase CountedIterator, que extiende el comportamiento
de un iterador de Python para realizar un seguimiento de cuántos elementos
han sido iterados.

La clase cuenta la cantidad de veces que se ha llamado a la función `next()`
sobre el iterador, proporcionando un contador accesible a través de un
método `get_count()`.

Clase:
    - CountedIterator: Una subclase de un iterador estándar que mantiene
      un contador de elementos iterados.

Métodos:
    - __init__(self, iterable): Inicializa el iterador y el contador.
    - __next__(self): Devuelve el siguiente elemento del iterador y
      aumenta el contador.
    - get_count(self): Devuelve el número de elementos iterados hasta ahora.
"""


class CountedIterator:
    """
    Clase que extiende el comportamiento de un iterador estándar, manteniendo
    un contador de los elementos que se han iterado.
    """

    def __init__(self, iterable):
        """
        Inicializa el iterador y el contador.

        Args:
            iterable: Cualquier objeto iterable del que se quiera obtener los
                      elementos.
        """
        self.iterator = iter(iterable)  # Convertimos el iterable en iterador
        self.counter = 0  # Inicializamos el contador de elementos iterados

    def __next__(self):
        """
        Devuelve el siguiente elemento del iterador e incrementa el contador.

        Si no quedan elementos, lanza una excepción StopIteration.
        """
        try:
            # Obtener el siguiente elemento del iterador
            item = next(self.iterator)
            # Incrementar el contador
            self.counter += 1
            # Devolver el siguiente elemento
            return item
        except StopIteration:
            # Si no quedan elementos, lanza la excepción StopIteration
            raise StopIteration

    def get_count(self):
        """
        Devuelve el número de elementos que se han iterado hasta el momento.
        """
        return self.counter
