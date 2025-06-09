#!/usr/bin/env python3

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializa un diccionario de Python y lo guarda en un archivo JSON.

    Args:
        data (dict): Diccionario a serializar.
        filename (str): Nombre del archivo donde se guardará el JSON.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Carga, deserializa datos desde archivo JSON y recrear un diccio de Python.

    Args:
        filename (str): Nombre del archivo de entrada JSON.

    Returns:
        dict: Diccionario deserializado del archivo JSON.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == "__main__":
    # Datos de ejemplo para serializar
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Serializar los datos y guardarlos en un archivo
    serialize_and_save_to_file(data_to_serialize, 'data.json')
    print("Data serialized and saved to 'data.json'.")

    # Cargar y deserializar datos desde 'data.json'
    deserialized_data = load_and_deserialize('data.json')
    print("Deserialized Data:")
    print(deserialized_data)
