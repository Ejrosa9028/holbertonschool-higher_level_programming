#!/usr/bin/python3
def read_file(filename=""):
    """Lee un archivo de texto UTF-8 y lo imprime en la salida estándar"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
