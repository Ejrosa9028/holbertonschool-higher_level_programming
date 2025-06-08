#!/usr/bin/python3
"""
Módulo que contiene la función write_file para escribir texto en un archivo.

Este módulo define una función que permite escribir una cadena de texto
en un archivo codificado en UTF-8 y devuelve cantidad de caracteres escritos.
"""


def write_file(filename="", text=""):
    """
    Escribe una cadena de texto en un archivo (UTF-8) y devuelve la cantidad
    de caracteres escritos.

    Si el archivo ya existe, su contenido se sobreescribirá.
    Si el archivo no existe, se creará uno nuevo.

    Args:
        filename (str): Nombre del archivo donde se guardará el texto.
        text (str): El texto que se escribirá en el archivo.

    Returns:
        int: Número de caracteres escritos en el archivo.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
