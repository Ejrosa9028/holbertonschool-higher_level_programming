#!/usr/bin/python3
"""
Script que elimina todos objetos State con nombre que contenga la letra 'a'
de la base de datos hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """ Función principal para eliminar los estados con 'a' en su nombre."""
    if len(sys.argv) != 4:
        return

    username, password, db_name = sys.argv[1:]

    # Crear el motor de base de datos
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}', pool_pre_ping=True)

    # Crear la sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Buscar todos los estados cuyo nombre contenga 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Eliminar los estados encontrados
    for state in states_to_delete:
        session.delete(state)

    # Confirmar los cambios
    session.commit()
    
    # Cerrar la sesión
    session.close()


if __name__ == "__main__":
    main()
