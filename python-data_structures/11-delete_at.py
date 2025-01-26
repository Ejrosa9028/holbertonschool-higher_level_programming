def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list  # Si el índice es inválido, no hacemos cambios y devolvemos la lista original
    
    # Modificamos la lista directamente eliminando el elemento en la posición idx
    del my_list[idx]
    
    return my_list  # Devolvemos la lista modificada
