#!/usr/bin/python3
"""
Deletes all State objects with a
names containing the letter 'a'
from the database hbtn_0e_6_usa.
Usage: ./13-model_state_delete_a.py
<mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command-line arguments
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]

    # Create engine and bind it to session
    engine = create_engine(
        f"mysql+mysqldb://{mysql_user}:{mysql_passwd}@localhost/{mysql_db}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and delete states containing 'a'
    states_to_delete = session.query(
        State).filter(State.name.like("%a%")).all()
    for state in states_to_delete:
        session.delete(state)

    session.commit()  # Commit changes to the database
    session.close()
