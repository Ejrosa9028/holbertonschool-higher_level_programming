#!/usr/bin/python3
"""
Este módulo contiene la función append_write, que agrega texto
al final de archivo (UTF-8). Si el archivo no existe,
se crea automáticamente.
"""


def append_write(filename="", text=""):
    """
    Agrega una cadena de texto al final de un archivo (UTF-8).
    Si el archivo no existe, se crea automáticamente.

    Args:
        filename (str): El nombre del archivo donde se agregará el texto.
        text (str): El texto a agregar al archivo.

    Returns:
        int: Número de caracteres añadidos al archivo.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
