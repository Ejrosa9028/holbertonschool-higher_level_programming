#!/usr/bin/python3
"""
Script que imprime ciudades junto con sus estados de hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


def main():
    """Función para listar las ciudades con estado correspondiente."""
    if len(sys.argv) != 4:
        return

    username, password, db_name = sys.argv[1:]

    # Crear el motor de base de datos
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}', pool_pre_ping=True)

    # Crear la sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Consultar todas las ciudades con su estado
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Imprimir resultados en el formato requerido
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Cerrar la sesión
    session.close()


if __name__ == "__main__":
    main()
