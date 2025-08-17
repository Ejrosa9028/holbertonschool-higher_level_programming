#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa.
Usage: ./11-model_state_insert.py
<mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]

    # Create engine and bind it to the session
    engine = create_engine(
        f"mysql+mysqldb://{mysql_user}:{mysql_passwd}@localhost/{mysql_db}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State object for "Louisiana"
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()  # Commit changes to database

    # Print the id of the newly added state
    print(new_state.id)

    # Close session
    session.close()
