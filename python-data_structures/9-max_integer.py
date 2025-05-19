#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_value = my_list[0]  # Iniciamos el valor máximo con el primer elemento
    for num in my_list:
        if num > max_value:
            max_value = num  # Actualizamos el valor máximo

    return max_value
