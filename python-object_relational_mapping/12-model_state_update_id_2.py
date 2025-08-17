#!/usr/bin/python3
"""
Change the name of a State object
in the database hbtn_0e_6_usa.
Usage: ./12-model_state_update_id_2.py
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

    # Query the State object with id=2
    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()  # Commit changes to database

    # Close session
    session.close()
