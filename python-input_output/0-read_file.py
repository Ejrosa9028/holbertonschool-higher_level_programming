#!/usr/bin/python3
"""
Módulo que contiene la función read_file para leer y mostrar el contenido
de un archivo de texto codificado en UTF-8.
"""


def read_file(filename=""):
    """
    Lee un archivo de texto codificado en UTF-8 y muestra su contenido
    en la salida estándar.

    Args:
        filename (str): Nombre del archivo que se leerá.

    Este método imprime el contenido del archivo directamente en la consola.
    Si el archivo no existe o no se puede leer, se generará una excepción.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
