#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # Intentamos imprimir como entero
        return True  # Si no hay error, devolvemos True
    except (ValueError, TypeError):  # Capturamos errores si no es un entero
        return False  # Si ocurre un error, devolvemos False
