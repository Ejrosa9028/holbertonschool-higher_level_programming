#!/usr/bin/python3
"""Lists cities of a state from the hbtn_0e_4_usa (SQL injection safe)"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Conectar a la base de datos
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],      # Usuario de MySQL
        passwd=sys.argv[2],    # Contraseña de MySQL
        db=sys.argv[3],        # Nombre de la base de datos
        port=3306
    )

    # Crear cursor
    cur = db.cursor()

    # Consulta segura con placeholder %s para evitar SQL Injection
    query = """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """
    cur.execute(query, (sys.argv[4],))  # Se pasa como una tupla

    # Obtener resultados y formatear la salida
    cities = [row[0] for row in cur.fetchall()]
    print(", ".join(cities))

    # Cerrar cursor y conexión
    cur.close()
    db.close()
