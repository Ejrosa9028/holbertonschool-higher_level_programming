#!/usr/bin/python3
"""
List all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
Usage: ./9-model_state_filter_a.py
<mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create the database engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states containing letter 'a', ordered by id
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(
        State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
