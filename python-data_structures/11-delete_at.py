#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list  # Si el índice es inválido, no hacemos cambios
    # Modificamos la lista directamente eliminando
    del my_list[idx]
    return my_list  # Devolvemos la lista modificada
