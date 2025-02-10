#!/usr/bin/python3

"""
Este módulo define una clase llamada VerboseList, que extiende la clase
lista de Python para agregar comportamientos personalizados con notificaciones
cuando se modifican los elementos de la lista.

Clases:
    - VerboseList: Una clase que hereda de la clase `list` de Python. Esta
      clase sobrescribe los métodos `append`, `extend`, `remove`, y `pop` para
      imprimir mensajes de notificación cada vez que se modifica la lista.

Métodos sobrescritos:
    - append: Agrega un elemento a la lista e imprime una notificación con el
      mensaje "Added [item] to the list."
    - extend: Extiende la lista con varios elementos e imprime una notificación
      con mensaje "Extended the list with [x] items.", donde [x] es el número
      de elementos agregados.
    - remove: Elimina un elemento de la lista e imprime una notificación con el
      mensaje "Removed [item] from the list."
    - pop: Elimina un elemento de la lista y lo imprime con el mensaje "Popped
      [item] from the list." Si no se especifica un índice, elimina el último
      elemento.

Este módulo sobrescribe los métodos de una lista estándar de Python para
proporcionar notificaciones al agregar o eliminar elementos, lo que permite
hacer un seguimiento de las modificaciones en la lista.
"""


class VerboseList(list):
    """
    Esta clase extiende la funcionalidad de la lista estándar de Python.
    Proporciona notificaciones al agregar o eliminar elementos de la lista.
    """

    def append(self, item):
        """
        Sobrescribe el método append para agregar un elemento a la lista
        e imprimir una notificación.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Sobrescribe el método extend para extender la lista con varios
        elementos e imprimir una notificación con la cantidad de elementos
        añadidos.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """
        Sobrescribe el método remove para eliminar un elemento de la lista
        e imprimir una notificación antes de hacerlo.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Sobrescribe el método pop para eliminar un elemento de la lista
        e imprimir una notificación antes de hacerlo.
        Si no se especifica un índice, elimina el último elemento.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
