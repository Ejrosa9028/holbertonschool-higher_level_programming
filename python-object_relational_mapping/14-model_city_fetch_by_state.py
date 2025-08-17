#!/usr/bin/python3
"""
List all City objects from the database hbtn_0e_14_usa.
Usage: ./14-model_city_fetch_by_state.py
<mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Get command-line arguments
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]

    # Create engine and session
    engine = create_engine(
        f"mysql+mysqldb://{mysql_user}:{mysql_passwd}@localhost/{mysql_db}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities with their corresponding state names
    results = (
        session.query(City.id, City.name, State.name)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    # Print the results
    for city_id, city_name, state_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()
