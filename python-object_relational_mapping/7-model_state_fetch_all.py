#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Conectar a la base de datos MySQL
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}", pool_pre_ping=True)

    # Crear una sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Consultar todos los objetos State ordenados por id
    states = session.query(State).order_by(State.id).all()

    # Imprimir los resultados en el formato esperado
    for state in states:
        print(f"{state.id}: {state.name}")

    # Cerrar la sesión
    session.close()
