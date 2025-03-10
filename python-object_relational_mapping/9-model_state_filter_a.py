#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Conectar a la base de datos MySQL
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}", pool_pre_ping=True)

    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Obtener estados que contienen la letra 'a' y ordenarlos por id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Imprimir los resultados
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Cerrar sesión
    session.close()
