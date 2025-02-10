#!/usr/bin/python3
"""
Este módulo contiene la clase MyList, que hereda de la clase list de Python.

La clase MyList tiene un método llamado print_sorted, que imprime la lista
ordenada de manera ascendente sin modificar la lista original.

Métodos:
    - print_sorted: Imprime la lista ordenada de menor a mayor sin modificarla.
"""


class MyList(list):
    """
    Clase MyList que hereda de list y tiene un método print_sorted
    que imprime la lista ordenada de manera ascendente.
    """

    def print_sorted(self):
        """
        Método que imprime la lista ordenada en orden ascendente sin modificar
        la lista original.
        """
        print(sorted(self))
