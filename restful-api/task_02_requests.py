#!/usr/bin/python3
"""
Módulo: Interacción con una API RESTful usando requests

Este módulo obtiene datos de JSONPlaceholder y los muestra o guarda en CSV.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Obtiene y muestra los títulos de los posts desde JSONPlaceholder.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()  # Convierte la respuesta a JSON
        for post in posts:
            print(post["title"])  # Muestra solo los títulos


def fetch_and_save_posts():
    """
    Obtiene los posts y los guarda en un archivo CSV llamado posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()  # Convierte la respuesta a JSON
        
        # Abre el archivo CSV en modo escritura
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]  # Encabezados CSV
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Escribir los encabezados
            
            # Escribir cada post en el archivo CSV
            for post in posts:
                writer.writerow({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                })
        
        print("Archivo posts.csv creado correctamente.")
