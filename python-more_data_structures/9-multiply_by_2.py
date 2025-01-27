#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Creamos un nuevo diccionario con los valores multiplicados por 2
    return {key: value * 2 for key, value in a_dictionary.items()}
