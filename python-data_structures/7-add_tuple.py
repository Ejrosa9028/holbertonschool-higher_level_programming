#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Asegurarse de que ambas tuplas tengan al menos 2 elementos
    # Si falta algún elemento, agregamos 0 como valor predeterminado
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    # Retornar una nueva tupla con la suma de los respectivos elementos
    return (a1 + b1, a2 + b2)
