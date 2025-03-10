#!/usr/bin/python3
""" Lists states from hbtn_0e_0_usa where name matches the argument safely """

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

    # Crear cursor para ejecutar consultas
    cur = db.cursor()

    # Consulta segura contra inyección SQL
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"
    cur.execute(query, (sys.argv[4],))

    # Obtener y mostrar los resultados
    for row in cur.fetchall():
        print(row)

    # Cerrar cursor y conexión
    cur.close()
    db.close()
