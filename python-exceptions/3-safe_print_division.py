#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b  # Intentamos dividir a entre b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))  # imprimimos el resultado
        return result  # Devolvemos el resultado
