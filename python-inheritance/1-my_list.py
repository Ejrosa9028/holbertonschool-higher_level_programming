#!/usr/bin/python3
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
