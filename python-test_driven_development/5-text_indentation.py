#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Separamos el texto en partes usando los caracteres ., ?, y :
    special_chars = ['.', '?', ':']
    
    # Usamos un bucle para iterar sobre cada carácter en el texto
    temp = ""
    for char in text:
        temp += char
        if char in special_chars:
            # Imprimimos el texto temporal sin espacios extra al principio o al final
            print(temp.strip())
            print()  # Imprime una línea en blanco después
            temp = ""  # Reiniciamos la variable temporal
    
    # Si el último carácter no es de los que necesitamos, imprimimos lo que queda
    if temp:
        print(temp.strip())
