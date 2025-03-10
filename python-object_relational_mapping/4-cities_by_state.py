#!/usr/bin/python3
""" Lists all cities from the database hbtn_0e_4_usa """

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

    # Consulta para obtener ciudades con su estado (JOIN con states)
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
    """
    cur.execute(query)  # Solo se permite usar execute() una vez

    # Mostrar los resultados
    for row in cur.fetchall():
        print(row)

    # Cerrar cursor y conexión
    cur.close()
    db.close()
