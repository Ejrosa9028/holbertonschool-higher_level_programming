#!/usr/bin/python3

"""
Este módulo define dos mixins: SwimMixin y FlyMixin, que proporcionan métodos
para nadar y volar. Además, la clase Dragon hereda de ambos mixins y tiene
la capacidad de nadar, volar y rugir.
"""


class SwimMixin:
    """
    Mixin que proporciona la capacidad de nadar.
    """

    def swim(self):
        """
        Método que simula la acción de nadar.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin que proporciona la capacidad de volar.
    """

    def fly(self):
        """
        Método que simula la acción de volar.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Clase que representa un dragón. Hereda de SwimMixin y FlyMixin,
    lo que le otorga habilidades para nadar y volar.
    """

    def roar(self):
        """
        Método que simula el rugido de un dragón.
        """
        print("The dragon roars!")


# Prueba
if __name__ == "__main__":
    dragon = Dragon()
    dragon.swim()  # El dragón nada
    dragon.fly()   # El dragón vuela
    dragon.roar()  # El dragón ruge
