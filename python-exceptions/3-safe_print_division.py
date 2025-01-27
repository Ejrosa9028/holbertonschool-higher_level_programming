#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b  # Intentamos dividir a entre b
    except ZeroDivisionError:
        result = None  # Si ocurre una excepción de división por cero, asignamos None
    finally:
        print("Inside result: {}".format(result))  # Siempre imprimimos el resultado dentro del finally
        return result  # Devolvemos el resultado (o None si hubo un error)
