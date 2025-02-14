#!/usr/bin/python3

# Escribe un texto en un archivo y devuelve el número de caracteres escritos.

def write_file(filename="", text=""):
    """
    Escribe una cadena de texto en un archivo (UTF-8) y devuelve la cantidad
    de caracteres escritos.

    Args:
        filename (str): Nombre del archivo donde se guardará el texto.
        text (str): El texto que se escribirá en el archivo.

    Returns:
        int: Número de caracteres escritos en el archivo.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
