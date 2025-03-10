#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """

import sys
import MySQLdb

if __name__ == "__main__":
    # Conexión a la base de datos
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],      # Usuario de MySQL
        passwd=sys.argv[2],    # Contraseña de MySQL
        db=sys.argv[3],        # Nombre de la base de datos
        port=3306
    )

    # Crear cursor para ejecutar consultas
    cur = db.cursor()

    # Ejecutar la consulta SQL
    cur.execute("SELECT * FROM states ORDER BY id ASC;")

    # Obtener y mostrar los resultados
    for row in cur.fetchall():
        print(row)

    # Cerrar cursor y conexión
    cur.close()
    db.close()
