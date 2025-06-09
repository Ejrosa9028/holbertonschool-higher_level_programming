#!/usr/bin/env python3
"""
Módulo task_03_xml.py

Este módulo proporciona funciones para serializar un diccionario a XML
y deserializar datos XML a un diccionario.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializa un diccionario a XML y guarda el contenido en un archivo.

    Args:
        dictionary (dict): Diccionario a serializar.
        filename (str): Nombre del archivo de salida XML.
    """
    # Crear el elemento raíz
    root = ET.Element("data")

    # Añadir cada elemento del diccionario como un subelemento
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Crear el árbol XML y escribirlo en el archivo
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializa datos XML de un archivo y los convierte a un diccionario.

    Args:
        filename (str): Nombre del archivo XML de entrada.

    Returns:
        dict: Diccionario deserializado del archivo XML.
    """
    try:
        # Parsear el archivo XML
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruir el diccionario a partir de los elementos XML
        result = {child.tag: child.text for child in root}
        return result

    except FileNotFoundError:
        print(f"Error: Archivo '{filename}' no encontrado.")
        return {}

    except Exception as e:
        print(f"Error durante la deserialización: {e}")
        return {}
