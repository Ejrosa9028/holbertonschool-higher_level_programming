#!/usr/bin/python3
""" Lists states from hbtn_0e_0_usa where name matches the argument """

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

    # Construir y ejecutar la consulta SQL con el nombre proporcionado
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(sys.argv[4])
    cur.execute(query)

    # Obtener y mostrar los resultados
    for row in cur.fetchall():
        print(row)

    # Cerrar cursor y conexión
    cur.close()
    db.close()
