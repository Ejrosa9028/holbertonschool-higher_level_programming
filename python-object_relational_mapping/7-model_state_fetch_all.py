#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
Usage: ./7-model_state_fetch_all.py
<mysql username> <mysql password> <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]

    # Create engine to connect to MySQL
    engine = create_engine(
        f"mysql+mysqldb://{mysql_user}:{mysql_passwd}@localhost/{mysql_db}",
        pool_pre_ping=True
    )

    # Bind the engine to a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects sorted by id
    states = session.query(State).order_by(State.id).all()

    # Print each state in the format "id: name"
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
