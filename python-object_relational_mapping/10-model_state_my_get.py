#!/usr/bin/python3
"""
Script que imprime el objeto State con el nombre pasado como argumento
desde la base de datos hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """ Función principal para recuperar el ID de un estado por su nombre."""
    if len(sys.argv) != 5:
        return

    username, password, db_name, state_name = sys.argv[1:]

    # Crear el motor de base de datos
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}', pool_pre_ping=True)

    # Crear la sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Consultar el estado por su nombre
    state = session.query(State).filter(State.name == state_name).first()

    # Imprimir el resultado
    if state:
        print(state.id)
    else:
        print("Not found")

    # Cerrar la sesión
    session.close()


if __name__ == "__main__":
    main()
