#!/usr/bin/python3
"""
Script que cambia el nombre objeto State en la base de datos hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """ Función principal para actualizar el estado con id=2 a "New Mexico"."""
    if len(sys.argv) != 4:
        return

    username, password, db_name = sys.argv[1:]

    # Crear el motor de base de datos
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}', pool_pre_ping=True)

    # Crear la sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Buscar el estado con id=2
    state = session.query(State).filter_by(id=2).first()

    if state:
        state.name = "New Mexico"
        session.commit()

    # Cerrar la sesión
    session.close()


if __name__ == "__main__":
    main()
