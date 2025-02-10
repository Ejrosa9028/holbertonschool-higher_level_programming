#!/usr/bin/python3

"""
Este módulo contiene la definición de la clase abstracta Animal y sus clases
derivadas, Dog y Cat.

La clase Animal es una clase base abstracta que define el método abstracto
sound. Las clases derivadas, Dog y Cat, implementan este método para devolver
el sonido característico de cada uno: "Bark" para Dog y "Meow" para Cat.

Clases:
    - Animal: Clase base abstracta que define el método abstracto sound.
    - Dog: Subclase de Animal que implementa el método sound y devuelve "Bark".
    - Cat: Subclase de Animal que implementa el método sound y devuelve "Meow".

Métodos:
    - sound: Método abstracto que debe ser implementado por las clases
      derivadas para devolver el sonido correspondiente.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Clase abstracta Animal que define un método abstracto sound.

    Esta clase sirve como base para las clases derivadas que necesitan
    implementar el método sound para producir el sonido correspondiente
    al animal.

    Métodos:
        - sound: Método abstracto que debe ser implementado por las
          clases derivadas.
    """

    @abstractmethod
    def sound(self):
        """
        Método abstracto que debe ser implementado por las clases
        derivadas para producir el sonido correspondiente al animal.

        No tiene implementación en esta clase base.
        """
        pass


class Dog(Animal):
    """
    Clase Dog que hereda de la clase Animal e implementa el método sound.

    Esta clase representa un perro y su método sound devuelve el sonido
    "Bark".

    Métodos:
        - sound: Implementación del método abstracto que devuelve
          "Bark".
    """

    def sound(self):
        """
        Método que devuelve el sonido característico de un perro.

        Devuelve:
            - str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Clase Cat que hereda de la clase Animal e implementa el método sound.

    Esta clase representa un gato y su método sound devuelve el sonido
    "Meow".

    Métodos:
        - sound: Implementación del método abstracto que devuelve
          "Meow".
    """

    def sound(self):
        """
        Método que devuelve el sonido característico de un gato.

        Devuelve:
            - str: "Meow"
        """
        return "Meow"
