#!/usr/bin/python3
def best_score(a_dictionary):
    # Verificamos si el diccionario es None o está vacío
    if not a_dictionary:
        return None
    # Encontramos la clave con el valor máximo
    return max(a_dictionary, key=a_dictionary.get)
