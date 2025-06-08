#!/usr/bin/python3
"""
Este script agrega todos los argumentos pasados al ejecutar el script
a una lista de Python y los guarda en un archivo JSON.
"""

import sys
import json
from os import path
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

# Nombre del archivo JSON donde se almacenará la lista
filename = "add_item.json"

# Si el archivo existe, carga la lista desde el archivo
if path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Agrega los argumentos pasados al script a la lista
items.extend(sys.argv[1:])

# Guarda la lista actualizada en el archivo JSON
save_to_json_file(items, filename)