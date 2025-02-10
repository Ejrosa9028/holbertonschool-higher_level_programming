#!/usr/bin/env python3
"""
Este módulo define tres clases: Fish, Bird y FlyingFish, que demuestran
el concepto de herencia múltiple en Python.

La clase FlyingFish hereda de Fish y Bird, y sobrecarga los métodos
heredados para adaptarlos a su comportamiento específico.
"""


class Fish:
    """
    Clase que representa un pez, con métodos para nadar y mostrar su hábitat.
    """

    def swim(self):
        """
        Método que simula el nado de un pez.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Método que muestra el hábitat natural del pez.
        """
        print("The fish lives in water")


class Bird:
    """
    Clase que representa pájaro, con métodos para volar y mostrar su hábitat.
    """

    def fly(self):
        """
        Método que simula el vuelo de un pájaro.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Método que muestra el hábitat natural del pájaro.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Clase que representa un pez volador, que hereda de Fish y Bird.
    Sobrescribe los métodos heredados para comportarse de acuerdo a su
    naturaleza híbrida de nadar y volar.
    """

    def swim(self):
        """
        Método sobrescrito que simula el nado del pez volador.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Método sobrescrito que simula el vuelo del pez volador.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Método sobrescrito que muestra el hábitat del pez volador.
        """
        print("The flying fish lives both in water and the sky!")


# Prueba
if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()  # El pez volador nada
    flying_fish.fly()   # El pez volador vuela
    flying_fish.habitat()  # El hábitat del pez volador

    # Ver la orden de resolución de métodos
    print(FlyingFish.mro())
