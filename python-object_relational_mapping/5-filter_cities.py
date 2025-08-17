#!/usr/bin/python3
"""
List all cities of a given state
from the database hbtn_0e_4_usa.
Usage: ./5-filter_cities.py
<mysql username> <mysql password> <database name> <state name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and state name from command-line arguments
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            user=mysql_user,
            passwd=mysql_passwd,
            db=mysql_db,
            port=3306
        )

        # Create a cursor object
        cursor = db.cursor()

        # Secure query using parameterized query to prevent SQL injection
        query = """SELECT cities.name FROM cities
                   JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id ASC;"""
        cursor.execute(query, (state_name,))

        # Fetch results and format them as a comma-separated string
        cities = [row[0] for row in cursor.fetchall()]
        print(", ".join(cities))

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
