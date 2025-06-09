#!/usr/bin/env python3
"""
Módulo task_02_csv.py

Este módulo define la función `convert_csv_to_json`, la cual convierte
un archivo CSV en un archivo JSON utilizando las bibliotecas `csv` y `json`.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convierte un archivo CSV en un archivo JSON y lo guarda en 'data.json'.

    Args:
        csv_filename (str): Nombre del archivo CSV a convertir.

    Returns:
        bool: True si la conversión fue exitosa, False si ocurrió un error.
    """
    try:
        # Abrir el archivo CSV y leer los datos usando DictReader
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        # Escribir los datos serializados en 'data.json'
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False

    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
