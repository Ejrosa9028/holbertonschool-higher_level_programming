#!/usr/bin/python3
"""
Script que agrega el objeto State "Louisiana" a la base de datos hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """ Función principal para agregar estado "Louisiana" y mostrar ID."""
    if len(sys.argv) != 4:
        return

    username, password, db_name = sys.argv[1:]

    # Crear el motor de base de datos
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}', pool_pre_ping=True)

    # Crear la sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Crear el nuevo estado "Louisiana"
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Imprimir el ID del nuevo estado
    print(new_state.id)

    # Cerrar la sesión
    session.close()


if __name__ == "__main__":
    main()
