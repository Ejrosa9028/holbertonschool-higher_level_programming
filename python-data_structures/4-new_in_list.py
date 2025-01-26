#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()  # Devuelve una copia de la lista original
    new_list = my_list.copy()  # Crea una copia de la lista original
    new_list[idx] = element  # Reemplaza el elemento en la posición idx
    return new_list
